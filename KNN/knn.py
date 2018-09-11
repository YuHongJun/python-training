#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Demi Yu'
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.metrics as metrics
import numpy as np
from sklearn.neighbors import NearestNeighbors
from scipy.spatial.distance import correlation, cosine
import ipywidgets as widgets
from IPython.display import display, clear_output
from sklearn.metrics import pairwise_distances
from sklearn.metrics import mean_squared_error
from math import sqrt
import sys, os, time
from contextlib import contextmanager
import numpy as np
import math
def createDataset():
    # 构建训练集数据
    dataset = [[0.26547727, 0.27892898,0],
           [0.1337869 , 0.08356665,0],
           [0.02771102, 0.36429227,0],
           [0.81783834, 0.86542639,1],
           [0.99240191, 0.87950623,1],
           [0.99240191, 0.77950623,1]]
    return np.array(dataset)


def getDistance(instance1,instance2):
    #  计算两点间的距离
    distance=0
    length = len(instance1)
    for i in range(length):
        distance += math.pow(instance1[i]-instance2[i],2)
    return math.sqrt(distance)


def getNeighbors(trainingSet,testInstance,k):
    # 计算未知实例与所有已知实例的距离。返回最近的K个已知实例
    features = createDataset()[:,:2]
    labels =  createDataset()[:,-1]
    distance_list = []
    for i in range(len(features)):
        distance = getDistance(testInstance,features[i])
        distance_list.append((distance,labels[i]))
    sorted_distance_list = sorted(distance_list)
    neighbors = sorted_distance_list[:k]
    return neighbors


def countClass(neighbors):
    # 对返回最近的K个已知实例，进行统计分类，根据少数服从多数，让未知实例归类为K个最邻近样本中最多数的类别。
    class_num_dict = {}
    for n in neighbors:
        if n[1] in class_num_dict:
            class_num_dict[n[1]] += 1
        else:
            class_num_dict[n[1]] = 1
    return class_num_dict

def main():
    trainingSet = createDataset()
    testSet = [[0,0],[1,1],[1.1,1.2]]
    result = []
    for test in testSet:
        # 计算未知实例与所有已知实例的距离。返回最近的K个已知实例
        neighbors = getNeighbors(trainingSet,test,4)
        # 对返回最近的K个已知实例，进行统计分类。
        class_num_dict = countClass(neighbors)
        # 根据少数服从多数，让未知实例归类为K个最邻近样本中最多数的类别。
        result.append(sorted(class_num_dict.items(),key = lambda x:x[1],reverse=True)[0][0])
    print(testSet)
    print(result)

if __name__ == '__main__':
    main()