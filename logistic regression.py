#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 12:27:43 2017

@author: nanshiqi
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
#matplotlib inline

np.random.seed(12)
num_observations = 5000

x1 = np.random.multivariate_normal([0, 0],[[1, 0.75],[0.75, 1]], num_observations)
x2 = np.random.multivariate_normal([4, 2],[[1, 0.75],[0.75, 1]], num_observations)

simulated_separableish_features = np.vstack((x1,x2)).astype(np.float32)
simulated_labels = np.hstack((np.zeros(num_observations),
                              np.ones(num_observations)))

plt.figure(figsize=(12,8))
plt.scatter(simulated_separableish_features[:, 0],simulated_separableish_features[:, 1],
            c = simulated_labels, alpha = .4)

clf = LogisticRegression(C = 0.4, solver = 'sag', warm_start = True)
clf.fit(simulated_separableish_features, simulated_labels)

print(simulated_separableish_features)
'''
print(clf.score(simulated_separableish_features, simulated_labels))
#print(clf.get_params([True]))
print(simulated_separableish_features[:, 0])
print(simulated_separableish_features[:, 1])
#print(simulated_separableish_features)
print(simulated_labels)
print(clf.intercept_, clf.coef_)
print(clf.get_params([True]))

plt.figure(figsize = (12, 8))
plt.scatter(simulated_separableish_features[:, 0], simulated_separableish_features[:, 1], c = simulated_labels - 1, alpha = .8, s = 50)
'''