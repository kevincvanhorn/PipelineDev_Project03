#!/usr/bin/env python
#SETMODE 777

#----------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------ HEADER --#

"""
:author:
    Kevin VanHorn

:synopsis:
    This module contains all the enumerators for pipeline, as globals are not allowed.

:description:
    Empty module for future definition of pipeline enumerator.

:applications:
    N/A

:see_also:
    N/A

"""

#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------- IMPORTS --#

# Built-in and Third Party
import os
import platform
import sys

# Modules Written by You

#----------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------- FUNCTIONS --#
def enum(**enums):
    return type('Enum', (), enums)

OSDrive = enum(WINDOWS='C:/', LINUX='//home/', MAC='//home/')
#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------- CLASSES --#
class BaseEnumOS(object):
    """
    This should evaluate the OS and get the drive.
    """
    def __init__(self):
        self.os    = None
        self.drive = None
        self.eval_os()
        self.eval_drive()

    def eval_os(self):
        """
        Get the operating system type and set it here.
        """
        self.os = platform.system()

    def eval_drive(self):
        """
        Set the value of drive here.
        """
        if self.os == 'Windows':
            self.drive = "C:/Users/Kevin/OneDrive/School/17s/Python/tempdir/"#"//infinity/atec/class/atec4371.002.17s"
        elif self.os == 'Linux':
            self.drive = OSDrive.LINUX
        elif self.os == 'DARWIN':
            self.drive = OSDrive.MAC

class OSTypeEnum(object):
    """
    This should create an instance of BaseEnumOS and set drive.
    """
    def __init__(self):
        os_info    = BaseEnumOS()
        self.os    = os_info.os
        self.drive = os_info.drive
OS = OSTypeEnum()

class DiskTypesEnum(object):
    CODE    = 'code'
    CONFIG  = 'config'
    DATA    = 'data'
    RENDER  = 'render'
    STORE   = 'store'
    WORK    = 'work'
    ALL     = [CODE, CONFIG, DATA, RENDER, STORE, WORK]

    def get_all(self):
        return self.ALL
DiskTypes = DiskTypesEnum()