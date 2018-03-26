#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 20:03:34 2018

@author: nanshiqi
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 10:21:56 2017

@author: nanshiqi
"""

import scipy.io as sio
import random
import numpy

def select_case(casenum):
    """
    input: the number of a case
    output: a array of a case data
    """
    
    DATA_PATH = "/Users/nanshiqi/Documents/MATLAB/case"
 
    grid_data = sio.loadmat(DATA_PATH+str(casenum)+".mat")
    return grid_data['grid_data_'+str(casenum)][0][0]


sc = select_case
#print(sc(14))

def select_case_number(casenum,num):
    '''
    to get morecase
    '''
    DATA_PATH = "/Users/nanshiqi/Documents/MATLAB/case"
    grid_data = sio.loadmat(DATA_PATH+str(casenum)+num+".mat")
    return grid_data['mpc_new'][0][0]
print(select_case_number(14,"__999"))  
 
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
        
    def getPMUList(self):
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
    def __init__(self, casenum):
        self.casenum = casenum
        
    def getGridList(self):
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
    
        
    
   

    
case14_PMU = PMU_meas(14)
case14_grid = grid_line(14)
case14_gen = gen(14) 
   
#print(case14_gen.getGenList())
##print(case14_PMU.getLoadQ())
#print(case14_gen.getList())
#print(case14_gen.getLoadP())
#print(case14_gen.getLoadQ())
def busgenload(casenum):
    '''
    to get integrated data of buses, generators, loads
    :input: case number
    :return: integrated data
    '''
    List = []
    for e in case14_PMU.getPMUList():
        List.append([e[0],e[7],e[8],e[2],e[3]])
    i = 0
    for e in case14_gen.getGenList():
        while i<len(List):
            if e[0]==List[i][0]:
                List[i].append(e[1])
                List[i].append(e[2])
            else:
                List[i].append(0)
                List[i].append(0)
            i = i+1
    return List

#print(busgenload(14))

def loadSum(casenum):
    loadPSum = 0
    loadQSum = 0
    for e in busgenload(14):
        loadPSum += e[3]
        loadQSum += e[4]
    loadSum = [loadPSum, loadQSum]
    return loadSum

#print(loadSum(14))

def generateIn(num, item):
    i = 0
    loadList = []
    while i < num: 
        a = random.gauss(loadSum(14)[0], 40)
        b = loadSum(14)[1]*a/1.0/loadSum(14)[0]
        loadList.append([a,b])
        i = i+1
    return sorted(loadList)

a = generateIn(1000,busgenload(14))
#print(a)

#numpy.savetxt('loadS.txt',a)
'''
def generateData(num):
    #gGenp = generateIn(num,case14_gen.getGenP()) 
    #gGenQ = generateIn(num,case14_gen.getGenQ())
    gLoadP = generateIn(num,case14_PMU.getLoadP())
    gLoadQ = generateIn(num,case14_PMU.getLoadQ())
#print(generateIn(1,case14_gen.getGenP()))    
#print(generateIn(1,case14_gen.getGenQ()))
#print(generateIn(1,case14_PMU.getLoadP()))
#print(generateIn(1,case14_PMU.getLoadQ()))
'''
'''
i = 0
PMUVolPha = []
while i < 1000:
    #a = PMU_meas("14__"+str(i)).getVolMag
    a = PMU_meas("14__"+str(i))
    b = a.getVolPha
    PMUVolPha.append(b)
    i = i+1
    
print(PMUVolPha)
'''

