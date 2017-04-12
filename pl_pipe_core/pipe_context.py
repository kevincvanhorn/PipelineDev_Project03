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

# Modules Written by You
from pd_pipe_core.pipe_context import PipeContext
from pd_path_lib.formula_manager import FormulaManager  # Handles project formulas.

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

        # Get the formula for the given path:
        #formula_pieces = formula.get_formula(path)

        #if not formula_pieces:
        #    print("ERROR: formula is invalid.")
        #    return None


some_path = '//infinity/atec/class/atec3370.001.16f/work/finding_nemo/assets/character/dory'
context = get_pipe_context(some_path)
context.eval_path('as_pub_dir', discipline='ani')
