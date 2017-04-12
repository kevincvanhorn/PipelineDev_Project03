#!/usr/bin/env python
#SETMODE 777

#----------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------ HEADER --#

"""
:author:
    Kevin VanHorn

:synopsis:
    Contains AutoVivification and IO helper class.

:description:
    AutoVivification, to be implemented by the ReadObjectXML class.
    IO, which will be used to print out information via various class methods.

:applications:
    N/A

:see_also:
    Implemented by pipe_object and xml_utils.

"""

#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------- IMPORTS --#

# Built-in and Third Party

# Modules Written by You

#----------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------- FUNCTIONS --#

#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------- CLASSES --#

# A class that only uses class methods.
class IO(object):
    """
    This class is used to print a bunch of stuff.
    """
    @classmethod
    def warning(cls, message):
        """
        This class method prints a warning.

        :param message: A warning message.
        :type: str
        """
        print "WARNING: %s" % message

    @classmethod
    def file_error(cls, file_name):
        """
        This class method prints an error message.

        :param file_name: The pieces of the message to print.
        :type: str
        """
        print "ERROR: The file provided, '%s', does not exist." % file_name

    @classmethod
    def info(cls, message):
        """
        This class method prints given information.

        :param message: The message to print.
        :type: str
        """
        print message


class Autovivification(dict):
    """
    This in a Python implementation of autovivification.
    """
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value
