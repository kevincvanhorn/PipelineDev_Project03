#!/usr/bin/env python
#SETMODE 777

#----------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------ HEADER --#

"""
:author:
    Kevin VanHorn

:synopsis:
    Contains the logic to apply PipeContext data to the path formulas.

:description:
    Turns pipe context info into a real path on disk via the path formula information.
    PathContext references the imported FormulaManager class and adjusts the output path
    based on received parameters.

:applications:
    N/A

:see_also:
    Implements formula_manager.py
"""

#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------- IMPORTS --#

# Built-in and Third Party
import re                           # Handles regular expressions.

# Modules Written by You
from pd_path_lib.formula_manager import FormulaManager  # Handles project formulas.

#----------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------- FUNCTIONS --#

#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------- CLASSES --#
class PipeContext(object):
    """
    Contains the pipe context object, which stores path variables.
    """
    def __init__(self, **kwargs):
        """
        Stores all of the variables mentioned in the header of the
        project_formulas document.

        :param kwargs: The keyword arguments of path variables.
        :type: str
        """
        # Assign Defaults to None
        self.drive = kwargs.setdefault('drive', None)
        self.disk_type = kwargs.setdefault('disk_type', None)
        self.project = kwargs.setdefault('project', None)
        self.sequence = kwargs.setdefault('sequence', None)
        self.shot = kwargs.setdefault('shot', None)
        self.cycle = kwargs.setdefault('cycle', None)
        self.context_type = kwargs.setdefault('context_type', None)
        self.asset = kwargs.setdefault('asset', None)
        self.asset_type = kwargs.setdefault('asset_type', None)
        self.assembly = kwargs.setdefault('assembly', None)
        self.discipline = kwargs.setdefault('discipline', None)
        self.work_area = kwargs.setdefault('work_area', None)
        self.version = kwargs.setdefault('version', None)
        self.wa_version = kwargs.setdefault('wa_version', None)

        # Assign Asset Defaults to None
        self.rig_type = kwargs.setdefault('rig_type', None)
        self.size = kwargs.setdefault('size', None)


    def eval_path(self, path, **kwargs):
        """
        Passes itself to the PathContext class, along with any kwargs and returns a
        completed path on disk.

        :param path: The label for a given path.
        :type: str

        :param kwargs: Additional arguments to specify path vars.
        :type: str

        :return: A string of  the completed path on disk.
        :type: str
        """
        # Create a reference to PathContext and return the result of get_path()
        return PathContext(self).get_path(path, **kwargs)


class PathContext(object):
    """
    Takes a PipeContext object and option arguments to create a valid path on disk.
        Passed in arguments override PipeContext attributes.
    """
    def __init__(self, pipe_context):
        """
        Stores the PipeContext instance received and references the FormulaManager class.

        :param pipe_context: PipeContext instance
        """
        self.pipe_context = pipe_context
        self.formula = FormulaManager()

    def get_path(self, path, **kwargs):
        """
        Accepts formula path and kwargs to return a completed path on disk.

        :param path: The path label.
        :type: str

        :param kwargs: Additional arguments to specify path vars.
        :type: str

        :return: The output path.
        :type: str
        """
        output_path = ""
        # Get the formula for the given path:
        formula_pieces = self.formula.get_formula(path)

        if not formula_pieces:
            print("ERROR: formula is invalid.")
            return output_path

        # Replace path references:
        for entry in formula_pieces:
            entry = re.sub(r'[\{\}]', "", entry)  # Remove braces from entry.
            if entry in self.pipe_context.__dict__.keys():
                # Append entry defined in kwargs to output_path:
                if entry in kwargs:
                    output_path += '/' + kwargs[entry]
                # Append entry defined in pipe_context to output_path:
                else:
                    print(entry)
                    print(self.pipe_context.__dict__[entry])
                    output_path += '/' + self.pipe_context.__dict__[entry]
            # Append entries that do not need to be replaced:
            else:
                output_path += '/' + entry
        output_path = output_path[1:]  # Remove first backslash

        return output_path
