#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 10:21:56 2017

@author: nanshiqi
"""

import scipy.io as sio

def select_case(casenum):
    """
    input: the number of a case
    output: a array of a case data
    """
    
    DATA_PATH = "/Users/nanshiqi/Documents/MATLAB/case"
 
    grid_data = sio.loadmat(DATA_PATH+str(casenum)+".mat")
    return grid_data['grid_data_'+str(casenum)][0][0]


sc = select_case


def get_array(casenum, array_name):
    """
    input: the number of a case, name of an array in one case like "bus", "gen"
    output: a list of data in "bus" or others
    """
    
    array_names = ['version', 'baseMVA', 'bus', 'gen', 'branch', 'gencost', 'bus_name']
    for e in array_names:
        if e==array_name:
            array_pos = array_names.index(e)
            return sc(casenum)[array_pos]

class PMU_meas(object):
    '''
    to get the data in PMU measurement
    one attribute: number of a case
    '''
    
    def __init__(self, casenum):
        self.casenum = casenum
        
    def getList(self):
        """
        to get the whole data in 'bus'
        :return:list of nodes
        """
        nodeList = get_array(self.casenum, 'bus')
        self.nodeList = nodeList
        return nodeList
   
    def getNodeNum(self):
        """
        :return: number of nodes
        """
        self.nodeNum = len(self.getList())
        return self.nodeNum
    
    def getVolMag(self):
        """
        :return: list of voltage magnitudes
        """
        volMList = []
        for e in self.getList():
            volMList.append(e[7])
        self.volMag = volMList
        return self.volMag
    
    def getVolPha(self):
        volPList = []
        for e in self.getList():
            volPList.append(e[8])
        self.volPha = volPList
        return self.volPha

def grid_line(object):
    """
    to get the data in grid lines
    one attribute: number of a case
    """
    def __init__(self, casenum):
        self.casenum = casenum
        
    def getList(self):
        """
        to get the whole list of grid line data
        """
        lineList = get_array(self.casenum, 'branch')
        self.lineList = lineList
        return lineList
    
    def getLineNum(self):
        """
        :return: number of lines
        """
        self.lineNum = len(self.getList())
        return self.lineNum
    
    def getFBus(self):
        """
        :return:list of "from" bus numbers
        """
        FBus = []
        for e in self.getList():
            FBus.append(e[0])
        self.FBus = FBus
        return self.Bus
    
    def getTBus(self):
        """
        :return: list of "to" bus numbers
        """
        TBus = []
        for e in self.getList():
            TBus.append(e[1])
        self.TBus = TBus
        return self.TBus

    
case14 = PMU_meas(14)
    
print(case14.getVolMag())
print(case14.getVolPha())
#print(grid_lines_fcn("14"))    