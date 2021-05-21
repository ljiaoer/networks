# -*- coding: utf-8 -*-
"""
Created on Mon May 13 13:38:06 2021

@author: lijiaojiao

社会网络分析之中凝聚子群、派系：

"""

import networkx as nx
import matplotlib.pyplot as plot
import pandas as pd
import csv
from collections import defaultdict

# 读取数据
e = nx.read_pajek("egypt_retweets.net")
#print("该图的节点数：",len(e)) # 该图共有 25178节点


"""
 组元和子图
"""

sub_groups=nx.connected_components(e)
sub_groups_list = list(sub_groups)
#print("该图的组元子图：",len(sub_groups_list))  #该图被分成3122个组元子图

#统计各组元子图的频数
x = [len(c) for c in sub_groups_list]
x_counts = pd.value_counts(x) # 统计各组元子图的频数
print("子图及其节点数：\n",x_counts)  #  最大的子图包含17762 个节点，包含2个节点的子图有2429个

#筛选出度数大于1的节点，并重新构建网络图
def trim_edges(g,weight =1):
    g2 = nx.Graph() # 创建空图
    for f,to,edata in g.edges(data = True):
        if edata["weight"]>weight:     #edge attribute (by default `weight`)
            g2.add_edge(f,to,edata)
    return g2

# 网络中的岛屿方法
def island_method(g, iterations=5):
    weights = [edata["weight"] for f, to, edata in g.edges(data=True)]
    mn = int(min(weights))
    mx = int(max(weights))
    step = int((mx - mn) / iterations)
    return [[threshold, trim_edges(g, threshold)] for threshold in range(mn, mx, step)]


cc = list(nx.connected_components(e))[0]

islands = island_method(cc)
for i in islands:
    print(i[0],len(i[1]),len(list(nx.connected_components(i[1]))))


