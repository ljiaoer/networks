# -*- coding: utf-8 -*-
"""
Created on Mon May 13 13:38:06 2021

@author: lijiaojiao

社会网络分析之中凝聚子群、派系：

"""

import networkx as nx
import matplotlib.pyplot as plot

nx.connected_components

x = [len(c) for c in sub_groups_list]
plot.hist(x)

def trim_deges(g,weight =1):
    g2 = nx.Graph() # 创建空图
    for f,to,edata in g.edges(data = True):
        if edata["weight"]>weight:
            g2.add_edge(f,to,edata)
    return g2


import csv
x.add_edge