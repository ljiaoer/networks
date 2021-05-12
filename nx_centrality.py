# -*- coding: utf-8 -*-
"""
Created on Mon May 10 13:38:06 2021

@author: lijiaojiao

degree centrality
度数中心性（degree centrality）、接近中心性（clonessness centrality）、中介中心性（betweenness centrality）、特征向量中心性（eigenvector_centrality）以及PageRank

"""
from operator import itemgetter
import networkx as nx
import matplotlib.pyplot as plot

######## 1. 读取数据 ##########
g = nx.read_pajek("D:\\program\\networks\data\\russians.net")
lens = len(g) # 读取图的节点数
# print(lens)

# 各节点中心性（度数中心性、接近中心性、中介中心性）值的排序
def sorted_map(map):
    ms = sorted(map.items(),key= lambda d:d[1],reverse=True)   # lambda d:d[1]按照字典中的值排序，reverse=True降序排序
    return ms


######## 2.度数中心性（degree centrality）计算 ##########

#度数中心性的计算
d1 = nx.degree(g)  #  d1为网络图的数据，主要是节点及边的数量，其类型为networkx.classes.reportviews.MultiDegreeView，是Iterator类型。
d = dict(d1)     #deg 是Iterator类型，需要转换为dict类型，才可以进行进一步计算
#度数中心性的最大最小值
d_min = min(d.values()) #度数中心性（degree centrality）的最小值
d_max = max(d.values()) #度数中心性（degree centrality）的最大值
#度数中心性的排序
ds = sorted_map(d)   #各节点的度数中心性（degree centrality）的列表，降序排序
print("度数中心性前10的节点为：" )
print(ds[0:10])
#各节点度数中心性的分布情况
h = plot.hist(dict(d).values(),100)
print(plot.loglog(h[1][1:],h[0]))

# 删除指定节点（例如，度数为1的节点），返回新的网络图
def trim_degrees(g,degree):
    g2 = g.copy()
    d = nx.degree(g2)
    for n in list(g2.nodes()):
        if d[n] <= degree:
            g2.remove_node(n)
    return g2

# 删除度数为1的节点
core1 = trim_degrees(g,1)

# 删除度数为10 的节点
core10 = trim_degrees(g,10)
len(core10)

#绘制度数大于10 的节点的网络图（中心性网络图）
print(nx.draw(core10,with_labels=True))


######## 3.接近中心性（clonessness centrality）计算 ##########

c = nx.closeness_centrality(core10)  #计算接近中心性
cs = sorted_map(c)   #对结果进行排序
print("接近中心性前10的节点为：" )
print(cs[0:10])

print(plot.hist(dict(c).values()) ) #接近中心性的分布

######## 4.中介中心性 betweenness centrality计算 ##########

core11 = nx.DiGraph(core10) #数据类型转化
b = nx.betweenness_centrality(core11) # 计算中介中心性
bs = sorted_map(b)  #排序
print("中介中心性前10的节点为：" )
print(bs[:10])


######## 5. 三种中心性的合并 ##########
#创建列表，存储三种不同中心性测量值的前10
name1 = [x[0] for x in ds[:10]]
name2 = [x[0] for x in cs[:10]]
name3 = [x[0] for x in bs[:10]]
# 使用Python的set函数将三组列表拼到一起
names = list(set(name1) | set(name2) | set(name3))
#创建中心性列表。 d,c,b分别为对应的字典
table = [[name,d[name],c[name],b[name]] for name in names]
print("该网络图度数中心性（degree centrality）、接近中心性（clonessness centrality）、接近中心性（clonessness centrality）、中介中心性（betweenness centrality）为：" )
print(table)


######## 6. 特征向量中心性（eigenvector_centrality）计算 ##########
e = nx.eigenvector_centrality(core11) #计算特征向量中心性
es = sorted_map(e) #排序
print("特征向量中心性前10的节点为：" )
print(es[:10])


######## 7. PageRank 算法  ##########
p = nx.pagerank(core11)
pr = sorted_map(p)
print("PageRank 算法计算得前10的节点为：" )
print(pr[:10])

######## 5. 五种中心性的合并 ##########
#创建列表，存储五种不同中心性测量值的前10
name1 = [x[0] for x in ds[:10]]
name2 = [x[0] for x in cs[:10]]
name3 = [x[0] for x in bs[:10]]
name4 = [x[0] for x in es[:10]]
name5 = [x[0] for x in pr[:10]]
# 使用Python的set函数将五组列表拼到一起
names = list(set(name1) | set(name2) | set(name3) | set(name4) | set(name5))
#创建中心性列表。
table = [[name,d[name],c[name],b[name],e[name],p[name]] for name in names]
print("五种中心性列表为：" )
print(table)