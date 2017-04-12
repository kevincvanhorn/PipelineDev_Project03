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
from pl_pipe_utils.utils import IO

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
    drivestr = str('drive=' + OS.drive)
    PathContext.examine_path(path)
    pipe_context = PipeContext(disk_type='work', drive=OS.drive)
    return pipe_context
#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------- CLASSES --#

class PathContext(object):
    def __init__(self):
        pass

    @classmethod
    def examine_path(cls, path):
        formula = FormulaManager()
        #pipe_context = PipeContext()
        validKeys = Autovivification()

        # Load into formula dictionary from the formulas.txt documents depending on the path provided.
        if "assets" in path:
            formula.create_formulas("as_")
        else:
            formula.create_formulas("")

        formula_pieces = formula.get_formula('pr_base_dir')
        print(formula_pieces)

        # Add valid Entries to cross check with path.
        validKeys['drive'] = OS.drive
        validKeys['disk_type'] = DiskTypes.get_all()

        # Replace path references:
        for entry in formula_pieces:
            entry = re.sub(r'[\{\}]', "", entry)  # Remove braces from entry.
            if entry in validKeys.keys():
                matchcount = 0
                if entry == 'disk_type':
                    for i in range(len(validKeys[entry])):
                        if path.startswith(validKeys[entry][i], 0, len(validKeys[entry][i])):
                            matchcount += 1
                    if matchcount != 1:
                        print("Result: Unable to find valid context information for this formula ")
                        return False
                elif not path.startswith(validKeys[entry], 0, len(validKeys[entry])):
                    # Invalid String
                    print("Result: Unable to find valid context information for this formula ")
                    return False
                length =len(validKeys[entry])+1
                path = path[length:] #remove length of string read from beginning of path.


some_path = '//infinity/atec/class/atec4371.002.17s/work/finding_nemo/assets/character/dory'
context = get_pipe_context(some_path)
#IO.info(context.project)
context.eval_path('as_pub_dir', discipline='ani')
