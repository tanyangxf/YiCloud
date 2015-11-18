# -*- coding: utf-8 -*-

import libvirt, sys
from vm_xml import CreateXML, DelXML
from xml.etree.ElementTree import ElementTree, Element, fromstring

sys.path.append("..")
from yicloud.config import DefaultConfig

host = libvirt.open(DefaultConfig.hostUri)

def CreateVM(VMname, VMcpu, VMmem, VMdisk):
    VMFile = CreateXML(VMname, VMcpu, VMmem, VMdisk)
    if VMFile:
        with open(VMFile) as f:
            domainXMLString = f.read()
            domain = host.defineXML(domainXMLString)
        return True
    else:
        return False


def ShutdownVM(VMname):
    domain = host.lookupByName(VMname)
    if domain.state()[0] == libvirt.VIR_DOMAIN_RUNNING:
        domain.destroy()
        return True
    else:
        return False 

def StartVM(VMname):
    domain = host.lookupByName(VMname)
    domain.create()
    if domain.state()[0] == libvirt.VIR_DOMAIN_RUNNING:
        return True
    else:
        return False

def GetVNCPort(VMname):
    domain = host.lookupByName(VMname)
    if domain.state()[0] == libvirt.VIR_DOMAIN_RUNNING:
        XMLContent = domain.XMLDesc()
        XMLStr = fromstring(XMLContent)
        for display_source in  XMLStr.iter('graphics'):
            display_dict = display_source.attrib
        VNCPort = display_dict['port']
        return VNCPort
    else:
        return False

def RebootVM(VMname):
    domain = host.lookupByName(VMname)
    if domain.state()[0] == libvirt.VIR_DOMAIN_RUNNING:
        domain.reboot()
        return True
    else:
        return  False


def DelVM(VMname):
    domain = host.lookupByName(VMname)
    if domain.state()[0] == libvirt.VIR_DOMAIN_SHUTOFF:
        domain.undefine() 
        DelXML(VMname)
        return True
    elif domain.state()[0] == libvirt.VIR_DOMAIN_RUNNING:
        domain.destroy() 
        domain.undefine()
        DelXML(VMname)
        return True
    else:
        print domain.state()
        return False
    



#print CreateVM('yicloud', 2, 200, '/home/tanyang/yivm1.qcow2')
#print StartVM('yicloud')
#print RebootVM('yicloud')
print GetVNCPort('yicloud')
'''
print "start vm...."
print StartVM('yicloud')
print "start vm successed "

#GetVNCPort('yicloud')

print "shutdown vm..."
print ShutdownVM('yicloud')
print "shutdown vm successed"

print "del vm...."
print DelVM('yicloud')
print "del vm successed..."
'''
