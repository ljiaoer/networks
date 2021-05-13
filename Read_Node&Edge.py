# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

"""
从livejournal读取节点和边。P45
"""


import networkx as nx
import urllib


# =============================================================================
# g = nx.Graph()
# g.add_edge("a","b")
# g.add_edge("b","c")
# g.add_edge("a","c")
# print (nx.draw(g))
# =============================================================================



def read_lj_friends(g,name):
    #抽取朋友列表从live1journal
    response = urllib.request.urlopen("https://www.livejournal.com/misc/fdata.bml?user=" + name)
    #遍历，并抽取边和节点
    for line in response.readlines():
        #如果以#开头，则是注释，跳过
        if line.startswith(b"#"):
            continue
        #确保没有空行
        parts = line.split()
        if len(parts)==0:
            continue
         # 如果是“<name”的样式，则是入度，如果是“>name”的样式，则是出度
        if parts[0] == "<":
            g.add_edge(parts[1],name)
        else:
            g.add_edge(name,parts[1])

g = nx.Graph()
read_lj_friends(g,"valerois")
lens = len(g) #计算节点数量
print(lens)
print(nx.draw(g))



"""
滚雪球抽样法
"""

def snowball_sampling(g,center,max_depth = 1, current_depth =0,taboo_list = []):
    print(center,current_depth,max_depth,taboo_list)
    if current_depth == max_depth:
        print("out of depth")
        return taboo_list
    if center in taboo_list:
        print("taboo")
        return taboo_list
    else:
        taboo_list.append(center)

    read_lj_friends(g,center)

    for node in g.neighbors(center):
        taboo_list = snowball_sampling(g,node,max_depth =max_depth,current_depth= current_depth+1,taboo_list =taboo_list)
    return taboo_list

g1 = nx.Graph()
print(snowball_sampling(g1,"kozel_na_sakse"))



"""
保存和加载文件中的数据
通常采用pajek格式
"""
save_pajek = nx.write_pajek(g1,"lj_friends.net")
print(save_pajek)







