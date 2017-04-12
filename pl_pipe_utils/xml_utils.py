#!/usr/bin/env python
#SETMODE 777

#----------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------ HEADER --#

"""
:author:
    Kevin VanHorn

:synopsis:


:description:


:applications:
    N/A

:see_also:
    Implemented by pipe_object. Implements utils.
"""

#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------- IMPORTS --#

# Built-in and Third Party
import os                                         # For file IO.
import xml.etree.ElementTree as et                # XML Element Tree.

# Modules Written by You
from pl_pipe_utils.utils import IO                # Handles IO.
from pl_pipe_utils.utils import Autovivification  # AutoVivification for dict.

#----------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------- FUNCTIONS --#

#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------- CLASSES --#

class ReadObjectXML(object):
    """
        Reads the context of the XML, if it exists, and gives the contents back as a
        dictionary.
    """
    def __init__(self, xml_filepath):
        """
        Takes the path to an XML document.

        :param xml_filepath: the file path to an XML document.
        :type: str
        """
        self.xml_filepath = xml_filepath

    def read_xml(self):
        """
        Reads the XML document, stores the contents into a nested dictionary,
        and returns it.

        :return: the dictionary read from the XML document.
        :type: dict
        """
        # Verify file exists.
        if not os.path.isfile(self.xml_filepath):
            IO.file_error(self.xml_filepath)
            return None

        xml_dict = Autovivification()
        xml_file = et.parse(self.xml_filepath)
        root = xml_file.getroot()  # Read level 1 of XML

        # Find children (level 2) under root:
        xml_nodes = root.getchildren()
        if not xml_nodes:
            IO.warning("No nodes were found under the root.")
            return None

        # Read level 3 of XML:
        for xml_node in xml_nodes:
            child_nodes = xml_node.getchildren()
            if not child_nodes:
                IO.warning("Could not find any child nodes.")
                continue
            for child_node in child_nodes:
                # Read level 4 of XML:
                child_sub_nodes = child_node.getchildren()
                if not child_sub_nodes:
                    IO.warning("Could not find any child sub nodes.")
                    continue  # Skip to next iteration.
                for child_sub_node in child_sub_nodes:
                    # Add entry to dictionary.
                    value = child_sub_node.attrib['value']
                    child_sub_node = child_sub_node.tag               # Get tag name only.
                    xml_dict[child_node.tag][child_sub_node] = value  # Add entry.
        return xml_dict
