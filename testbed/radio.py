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


def set_channel(dc, nodes):
    '''Set the WiFi channel for a group of nodes

    e.g. Set all the nodes to channel 11.
    '''
    return

def get_channel(dc, nodes):
    '''Get the WiFi channel for a group of nodes

    e.g. Get all the nodes' channel.
    '''
    return

def set_mode(dc, nodes):
    '''Set the WiFi mode for a group of nodes

    e.g. Set all the nodes to ad-hoc mode.
    '''
    return

def get_mode(dc, nodes):
    '''Get the WiFi mode for a group of nodes

    e.g. Get all the nodes' mode.
    '''
    return

def set_tx_power(dc, nodes):
    '''Set the WiFi tx power for a group of nodes

    e.g. Set all the nodes to 14dbm.
    '''
    return

def get_tx_power(dc, nodes):
    '''Get the WiFi tx power for a group of nodes

    e.g. get all the nodes' power
    '''
    return
