#!/usr/bin/env python
#SETMODE 777

#----------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------ HEADER --#

"""
:author:
    Kevin VanHorn

:synopsis:
    Contains the Project and Asset classes for storing and acting on project and assest
    data.

:description:
    The Project class reads data from the projects.xml document, creating a project object
    for each block of project data. The Asset class reads data from the assets.xml
    document, creating an asset object for each block of asset data it finds.
    Contains the ProjectObject class for storing and acting on project data.
    Contains the AssetObject class for storing and acting on asset data.

:applications:
    N/A

:see_also:
    Implements xml_utils.py and utils.py for reading an XML, IO, and AutoVivification.
"""

#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------- IMPORTS --#

# Built-in and Third Party
import os                                           # File IO.

# Modules Written by You
from pl_pipe_utils.utils import IO                  # For printing.
from pl_pipe_utils.utils import Autovivification    # Dictionary AutoVivification.
from pl_pipe_utils.xml_utils import ReadObjectXML   # Reads an XML.
from pl_pipe_utils.pl_pipe_enums import OS

#----------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------- FUNCTIONS --#

#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------- CLASSES --#


class Project(object):
    """
        Reads data from the projects.xml document. For each block of project data found,
        creates a project object.
    """
    def __init__(self):
        """
        The class takes no arguments as it will find the documents it needs in the same
        directory that is located in.
        """
        self.xml_file = "projects.xml"      # XML file name.
        self.xml_dict = Autovivification()  # Dictionary from projects.xml.

    def find_xml(self):
        """
        This method finds and verifies the XML document on disk.

        :return: The success of the operation.
        :type: bool
        """
        # Create full file path:
        self.xml_file = OS.drive + '\\' + self.xml_file
        print(self.xml_file)

        # Verify file exists on disk.
        if not os.path.isfile(self.xml_file):
            IO.file_error(self.xml_file)
            return None
        return True

    def read_xml(self):
        """
        Creates an instance of ReadObjectXML, giving it the XML document path,
        and gets back a dictionary.

        :return: The success of the operation.
        :type: bool
        """
        self.find_xml()                              # Verify XML file.
        read_obj_xml = ReadObjectXML(self.xml_file)  # ReadObjectXML object.
        self.xml_dict = read_obj_xml.read_xml()      # Get Dictionary.

    def get_project_objects(self):
        """
        Uses the dictionary from read_xml to create instances of ProjectObject's,
        returns them as a list

        :return: a list of project objects.
        :type: list
        """
        project_list = []  # List of Project objects.
        self.read_xml()
        for project in self.xml_dict.keys():
            # Pass dictionary as **kwargs:
            project_obj = ProjectObject(**self.xml_dict[project])
            project_list.append(project_obj)
        return project_list


class Asset(object):
    """
        Reads data from the assets.xml document. For each block of asset data found,
        creates an asset object
    """
    def __init__(self):
        """
        The class takes no arguments as it will find the documents it needs in the
        same directory that is located in.
        """
        self.xml_file = "assets.xml"
        self.xml_dict = Autovivification()

    def find_xml(self):
        """
        This method will find and verify the XML document on disk.

        :return: The success of the operation.
        :type: bool
        """
        # Create full file path:
        self.xml_file = str(os.path.dirname(__file__)) + self.xml_file

        # Make sure the file exists on disk.
        if not os.path.isfile(self.xml_file):
            IO.file_error(self.xml_file)
            return None
        return True

    def read_xml(self):
        """
        Creates an instance of ReadObjectXML, giving it the XML document path,
        and gets back a dictionary.

        :return: The success of the operation.
        :type: bool
        """
        self.find_xml()
        read_obj_xml = ReadObjectXML(self.xml_file)
        self.xml_dict = read_obj_xml.read_xml()
        return True

    def get_asset_objects(self):
        """
        Uses the dictionary from read_xml to create instances of AssetObject's,
        returns them as a list

        :return: a list of Asset Objects
        :type: list
        """
        asset_list = []  # A list of Asset Objects.
        self.read_xml()  # Read Dictionary.
        for asset in self.xml_dict.keys():
            # Pass dictionary as **kwargs:
            asset_obj = ProjectObject(**self.xml_dict[asset])
            asset_list.append(asset_obj)
        return asset_list


class ProjectObject(object):
    """
        For storing and acting on project data.
    """
    def __init__(self, **kwargs):
        """
        Store several expected values in class attribute, like the PipeContext class does.

        :param kwargs: properties of a Project object.
        :type: str
        """
        # Assign Defaults to None
        self.modified_date = kwargs.setdefault('modified_date', None)
        self.modified_by = kwargs.setdefault('modified_by', None)
        self.description = kwargs.setdefault('description', None)
        self.created_by = kwargs.setdefault('created_by', None)
        self._id = kwargs.setdefault('_id', None)
        self.name = kwargs.setdefault('name', None)

    def get_assets(self):
        """
        Uses what information it has to find the assets XML that belongs to it, then makes objects of them.
        :return:
        """

class AssetObject(object):
    """
        For storing and acting on asset data.
    """
    def __init__(self, **kwargs):
        """
        Store several expected values in class attribute, like the PipeContext class does.

        :param kwargs: properties of an Asset object.
        :type: str
        """
        # Assign Defaults to None
        self.modified_date = kwargs.setdefault('modified_date', None)
        self.modified_by = kwargs.setdefault('modified_by', None)
        self.description = kwargs.setdefault('description', None)
        self.created_by = kwargs.setdefault('created_by', None)
        self.creation_date = kwargs.setdefault('creation_date', None)
        self.asset_type = kwargs.setdefault('asset_type', None)
        self._id = kwargs.setdefault('_id', None)
        self.name = kwargs.setdefault('name', None)

project = Project()
print(project.find_xml())