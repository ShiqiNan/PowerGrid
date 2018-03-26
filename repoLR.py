#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 16:29:28 2018

@author: nanshiqi
"""
import scipy.io as sio
import random
import numpy

def select_case_number(casenum,num):
    '''
    to get morecase
    '''
    DATA_PATH = "/Users/nanshiqi/Documents/MATLAB/case"
    grid_data = sio.loadmat(DATA_PATH+str(casenum)+num+".mat")
    return grid_data['mpc_new'][0][0]
#print(select_case_number(14,"__999")) 


sc = select_case_number

def get_array(casenum, array_name,num):
    """
    input: the number of a case, name of an array in one case like "bus", "gen"
    output: a list of data in "bus" or others
    """
    
    array_names = ['version', 'baseMVA', 'bus', 'gen', 'branch', 'gencost', 'bus_name']
    for e in array_names:
        if e==array_name:
            array_pos = array_names.index(e)
            return sc(casenum, num)[array_pos]
        
print(get_array(14,'bus', "__999"))
       
class PMU_meas(object):
    '''
    to get the data in PMU measurement
    one attribute: number of a case
    '''
    
    def __init__(self, casenum,num):
        self.casenum = casenum
        self.num = num
        
    def getPMUList(self):
        """
        to get the whole data in 'bus'
        :return:list of nodes
        """
        nodeList = get_array(self.casenum, self.num, 'bus')
        self.nodeList = nodeList
        return nodeList
   
    def getNodeNum(self):
        """
        :return: number of nodes
        """
        self.nodeNum = len(self.getPMUList())
        return self.nodeNum
    
    def getVolMag(self):
        """
        :return: list of voltage magnitudes
        """
        volMList = []
        for e in self.getPMUList():
            volMList.append(e[7])
        self.volMag = volMList
        return self.volMag
    
    def getVolPha(self):
        volPList = []
        for e in self.getPMUList():
            volPList.append(e[8])
        self.volPha = volPList
        return self.volPha
    
    def getLoadP(self):
        loadPList = []
        for e in self.getPMUList():
            loadPList.append(e[2])
        self.loadP = loadPList
        return self.loadP
    
     
    def getLoadQ(self):
        loadQList = []
        for e in self.getPMUList():
            loadQList.append(e[3])
        self.loadQ = loadQList
        return self.loadQ
    
    

class grid_line(object):
    """
    to get the data in grid lines
    one attribute: number of a case
    """
    def __init__(self, casenum, num):
        self.casenum = casenum
        self.num = num
        
    def getGridList(self):
        """
        to get the whole list of grid line data
        """
        lineList = get_array(self.casenum, self.num, 'branch')
        self.lineList = lineList
        return lineList
    
    def getLineNum(self):
        """
        :return: number of lines
        """
        self.lineNum = len(self.getGridList())
        return self.lineNum
    
    def getFBus(self):
        """
        :return:list of "from" bus numbers
        """
        FBus = []
        for e in self.getGridList():
            FBus.append(e[0])
        self.FBus = FBus
        return self.Bus
    
    def getTBus(self):
        """
        :return: list of "to" bus numbers
        """
        TBus = []
        for e in self.getGridList():
            TBus.append(e[1])
        self.TBus = TBus
        return self.TBus

class gen(object):
    def __init__(self, casenum):
        self.casenum = casenum
        
    def getGenList(self):
        """
        to get the whole list of grid line data
        """
        genList = get_array(self.casenum, 'gen')
        self.genList = genList
        return genList
    
    def getGenP(self):
        genPList = []
        for e in self.getGenList():
            genPList.append(e[1])
        self.genP = genPList
        return self.genP
    
     
    def getGenQ(self):
        genQList = []
        for e in self.getGenList():
            genQList.append(e[2])
        self.genQ = genQList
        return self.genQ
    
        
    
   

    
case14_PMU = PMU_meas(14,'__999')

#case14_grid = grid_line(14)
#case14_gen = gen(14) 
   