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
from pykafka import KafkaClient


def start(dc, nodes):
    '''start the actions for the a group of nodes
    '''
    return

def stop(dc, nodes):
    '''Stop actions for a group of nodes
    '''
    return

def get_data(dc, nodes):
    '''Get data from a group of nodes using kafka consumer

    e.g. Let the nodes run wifi sniffer project and get data from all the nodes.
    '''
    return

def change_instance(dc, nodes):
    '''Change the application for a group of nodes

    e.g. Let the nodes change to wifi smart channel selection from wifi sniffer.
    '''
    return
