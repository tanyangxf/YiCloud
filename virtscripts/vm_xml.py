# -*- coding: utf-8 -*-
import libvirt
import sys
import os
import string
sys.path.append("..")
from yicloud.config import DefaultConfig

from xml.etree.ElementTree import ElementTree, Element

XMLTree = ElementTree()
XMLTree.parse(DefaultConfig.XMLPath)
XMLRoot = XMLTree.getroot()

def CreateXML(VMname, VMcpu, VMmem, VMdisk):
    XMLRoot.find('name').text = str(VMname)
    XMLRoot.find('vcpu').text = str(VMcpu)
    XMLRoot.find('memory').text = str(VMmem*1024)
    XMLName = VMname + '.xml'
    XMLFile = DefaultConfig.XMLOutput + '/' + XMLName

    #Change the disk name

    for disk_source in XMLRoot.iter('source'):
        disk_dict = disk_source.attrib
        for file_name in disk_source.attrib.keys():
            disk_dict[file_name] = str(VMdisk)

    #Create XML file
    XMLTree.write(XMLFile)
    return XMLFile

def DelXML(VMname):
    XMLName = VMname + '.xml'
    XMLFile = DefaultConfig.XMLOutput + '/' + XMLName
    if os.path.isfile(XMLFile):
        os.remove(XMLFile)

