#!/usr/bin/env python
#SETMODE 777

#----------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------ HEADER --#

"""
:author:
    username

:synopsis:
    A one line summary of what this module does.

:description:
    A detailed description of what this module does.

:applications:
    Any applications that are required to run this script, i.e. Maya.

:see_also:
    Any other code that you have written that this module is similar to.

"""

#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------- IMPORTS --#

# Built-in and Third Party
import os
import re                           # Handles regular expressions.

# Modules Written by You
from pd_pipe_core.pipe_context import PipeContext
from pd_path_lib.formula_manager import FormulaManager  # Handles project formulas.
from pl_pipe_utils.pl_pipe_enums import OS
from pl_pipe_utils.utils import Autovivification
from pl_pipe_utils.pl_pipe_enums import DiskTypes

#----------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------- FUNCTIONS --#

def get_pipe_context(path):
    """
    Uses the PathContext examine_path class method to get help decoding the path.

    :param path: the path to the PipeObject
    :type:

    :return: a PipeContext Object.
    :type: PipeContext
    """
    # Uses get_pipe_context to do the work
    pipe_context = PipeContext()
    PathContext.examine_path(path)
    return pipe_context
#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------- CLASSES --#

class PathContext(object):
    def __init__(self):
        pass

    @classmethod
    def examine_path(cls, path, **kwargs):
        formula = FormulaManager()
        pipe_context = PipeContext()
        validKeys = Autovivification()

        # Load into formula dictionary from the formulas.txt documents depending on the path provided.
        if "assets" in path:
            formula.create_formulas("as_")
        else:
            formula.create_formulas("")

        formula_pieces = formula.get_formula('pr_base_dir')

        # WORKING - add all things from enums into this dictionary - make sure 'disk' is the correct format
                #ie. not {disk} or something
        validKeys['drive'] = OS.drive
        #validKeys['disk_type'] = DiskTypes.get_all()


        # Replace path references:
        for entry in formula_pieces:
            entry = re.sub(r'[\{\}]', "", entry)  # Remove braces from entry.
            if entry in validKeys.keys():
                # WORKING, PUT FOR THE ARRAY CASE IN DISKTYPE FROM GET ALL
                if not path.startswith(validKeys[entry], 0, len(validKeys[entry])):
                    # Invalid String
                    print("Result: Unable to find valid context information for this formula ")
                    return False
                length =len(validKeys[entry])+1
                path = path[length:] #remove length of string read from beginning of path.


some_path = '//infinity/atec/class/atec3370.001.16f/work/finding_nemo/assets/character/dory'
context = get_pipe_context(some_path)
#context.eval_path('as_pub_dir', discipline='ani')
