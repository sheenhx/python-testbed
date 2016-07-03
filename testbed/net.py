__author__ = "Xin Hu"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{xin}@tkn.tu-berlin.de"

'''
    The API definition of the testbed control interface for configuration/monitoring of the specific applications

    CC3200 family based
'''
import logging
import sys
from time import *
import datetime, string
import os
import consul


def connect_to_network(dc, nodes, ifaces):
    '''Connect a wifi network for the a group of nodes

    e.g. Let all the nodes connet to TKN wifi.
    '''
    return

def disconnect_device(dc, nodes, ifaces):
    '''Disconnect a device for a group of nodes

    e.g. Let the node disconnect your mobile phone.
    '''
    return

