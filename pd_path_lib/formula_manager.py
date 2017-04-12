#!/usr/bin/env python
#SETMODE 777

#----------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------ HEADER --#

"""
:author:
    Kevin VanHorn

:synopsis:
    This module contains the logic for dealing with path formulas.

:description:
    The FormulaManager class receives input from a file and reads the elements into
    a dictionary. The elements are cleaned and stored with the appropriate characters,
    available for the get_formula() method which returns the altered formula such that
    all references are replaced.

:applications:
    N/A

:see_also:
    Implemented by pd_pipe_core.pipe_context.py

"""

#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------- IMPORTS --#

# Built-in and Third Party
import os                            # For file I/O.
import re                            # For regular expressions.
from collections import OrderedDict  # Ordered Dictionary.

# Modules Written by You

#----------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------- FUNCTIONS --#

#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------- CLASSES --#

class FormulaManager(object):
    """
    Reads the project_formulas.txt document and expands all the formulas found therein,
    making this data available to the calling instance.
    """
    def __init__(self):
        """
        The class takes no arguments as it will find the documents it needs in the
        same directory that is located in.
        """
        self.formulas_path_project = "pl_path_lib\project_formulas.txt"
        self.formulas_path_asset = "pl_path_lib\\asset_formulas.txt"
        self.formula_dict = OrderedDict()  # Dictionary to hold lines of project_formulas.
        self.formula_list = []                     # A list of lines in the formulas.
        self.loaded = False                # True if file is loaded and dictionary made.

    def read_formulas(self, formula_name):
        """
        Reads the appropriate formulas text file of disk and stores the relevant lines.

        :return: The success of the operation.
        :type: bool
        """

        # Create full file path:
        base_path = str(os.path.dirname(__file__))  # + '\\' + formulas_path
        if base_path != "":
            os.chdir(base_path)
        self.formulas_path_project = os.path.abspath(os.path.join(base_path, "..", self.formulas_path_project))

        # Validate file path:
        if not os.path.isfile(self.formulas_path_project):
            print("ERROR: Invalid formulas_path.")
            return None

        # Read a file from disk:
        with open(self.formulas_path_project, 'r') as fh:
            for line in fh:
                if line[:1] != '#' and line[:1] != '\n':  # Avoid blank/commented lines.
                    self.formula_list.append(line)                # Store lines in list.

        # If Asset Formula:
        if formula_name.startswith("as_"):
            self.formulas_path_asset = os.path.abspath(os.path.join(base_path, "..", self.formulas_path_asset))

            # Validate file path:
            if not os.path.isfile(self.formulas_path_asset):
                print("ERROR: Invalid formulas_path.")
                return None

            # Read a file from disk:
            with open(self.formulas_path_asset, 'r') as fh:
                for line in fh:
                    if line[:1] != '#' and line[:1] != '\n':  # Avoid blank/commented lines.
                        self.formula_list.append(line)  # Store lines in list.
        return True #self.formula_list

    def split_formulas(self):
        """
        Splits up the save formula lines into a dictionary.

        :return: The success of the operation.
        :type: bool
        """
        count = 0  # Tracks the index in the list of lines.
        # Store formulas in dictionary:
        for line in self.formula_list:
            parts = line.split()                # Array of parts in a line.
            self.formula_dict[parts[0]] = line  # Line is stored under first word as key.
            count += 1
        return True

    def clean_formulas(self):
        """
        Removes unnecessary characters from the 'value' dictionary entries.

        :return: The success of the operation.
        :type: bool
        """
        for key in self.formula_dict:
            # Put elements in single quotes into a list at this key in the formula_dict.
            # Element example: ['{pr_data_dir}', 'assets.xml']
            self.formula_dict[key] = re.findall(r'\'(.*?)\'', self.formula_dict[key])
        return True

    def expand_formulas(self):
        """
        Substitutes Actual values for any 'xx_' values in a 'value' dictionary entry.

        :return: The success of the operation.
        :type: bool
        """
        for key in self.formula_dict:  # Key looks like: pr_data_dir.
            for entry in self.formula_dict[key]:
                # Only check entries in brackets:
                if entry[0] == '{':
                    entry_clean = re.sub(r'[\{\}]', "", entry) # Remove braces from entry.
                    # Switch out bracketed values:
                    if entry_clean in self.formula_dict:
                        # self.formula_dict[entry] ex: ['{pr_base_dir}', 'data']
                        # Index of entry to be replaced
                        index = self.formula_dict[key].index(entry)
                        self.formula_dict[key][index:index+1] = \
                            self.formula_dict[entry_clean]
        return True

    def create_formulas(self, formula_name):
        """
        Loads the dictionary by reading file and calling appropriate functions.

        :return: The success of the operation.
        :type: bool
        """
        self.read_formulas(formula_name)
        self.split_formulas()
        self.clean_formulas()
        self.expand_formulas()
        self.loaded = True
        return self.formula_dict

    def get_formula(self, formula_name):
        """
        Accepts a formula name and then runs the necessary commands to return
        the pieces of a given formula.

        :param formula_name: The path label for a given formula.
        :return: A list of the expanded elements in the formula.
        """
        # Call methods to create formula.
        if not self.loaded:
            self.create_formulas(formula_name)

        if formula_name in self.formula_dict:
            return self.formula_dict[formula_name]
        else:
            print("ERROR: Formula name not Found.")
            return None
