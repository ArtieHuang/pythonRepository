import random

import pandas as pd
import numpy as np
from d3graph import d3graph, vec2adjmat
import json

from pyecharts import options as opts
from pyecharts.charts import Graph
from matplotlib import pyplot as plt

PATH="35_分类_result_105词_词汇表.xlsx"





def randomColor(color):
    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

    for i in range(2):
        color =  colorArr[random.randint(0,14)] +color
    print(color)
    return "#"+color

def getColdColor():
    colorList = ["#FFFFCC","#FFCC00","#663300","#FF6600","#663333","#FFCC33",
                 "#CC6666","#FF6666","#FFCC66","#FF9900","#FF9966","#CC3300",
                 "#996666","#FFCCCC","#660000","#FF3300","#CC6600","#FF6633",
                 "#996633","#CC9999","#FF3333","#990000","#CC9966","#FFFF33",
                 "#FF9933","#330000","#993333","#CC3333","#CC0000","#FFCC99",
                 "#FFFF00","#996600","#993300","#FF0000","#CC6633","#CC9933"]
    return colorList
def getWarmColor():
    colorList = ["#660099","#9933CC","#666699","#660066","#333366","#0066CC",
                 "#99CCFF","#9933FF","#330099","#6699FF","#9966CC","#3300CC",
                 "#003366","#330033","#663399","#3333FF","#006699","#6633CC",
                 "#3333CC","#3399CC","#6600CC","#0066FF","#0033FF","#66CCFF",
                 "#330066","#3366FF","#3399FF","#6600FF","#3366CC","#6699CC",
                 "#0099FF","#CCCCFF","#000033","#33CCFF","#9999FF","#0000FF"]
    return colorList
def getNormalColor():
    colorList=["#669900","#99CC66","#99FF66","#00FF99","#33FF99","#66FF99",
               "#CCFF99","#669900","#99CC66","#99FF66","#00FF99","#33FF99",
               "#66FF99","#CCFF99","#669900","#99CC66","#99FF66","#00FF99",
               "#33FF99","#66FF99","#CCFF99",
               "#669900","#99CC66","#99FF66","#00FF99","#33FF99","#66FF99","#CCFF99"]
    return colorList
def get_colorlist(key):

    colorList = []
    if key ==-1:
        for i in range(20):
            colorList.append(randomColor("99"))
    elif  key==0:
        for i in range(20):
            colorList.append(randomColor("99"))
    print(colorList)
    return colorList

def xlsx_to_array(layout,control,path):
    wordMatrix= pd.read_excel(PATH,sheet_name="page_1")
    wordMatrix=wordMatrix.iloc[:, [0,1,2,3]]
    print(wordMatrix)
 #   wordMatrix=wordMatrix.take(np.random.permutation(103))
    print(wordMatrix)
    word=np.array(wordMatrix.iloc[:,0])
    number=np.array(wordMatrix.iloc[:,1])
    size=np.array(wordMatrix.iloc[:,2])
    color=np.array((wordMatrix.iloc[:,3]))

    ColdColor=getColdColor()
    color1=0

    WarmColor=getWarmColor()
    color2=0

    NormColor=getNormalColor()
    color3=0

    colorlist=[]
    nodes=[]
    category=[]
    j=0

    #防止报错
    number=np.append(number,24)
    print(number)
    for i in color:
        if i ==-1:
            colorlist.append(ColdColor[1])
            
        if i ==1:
            colorlist.append(WarmColor[2])

        if i ==0:
            colorlist.append(NormColor[3])

        j = j + 1




    j=0
    for i in word:
        nodes.append({"name":i, "category": number[j],"symbolSize":str((size[j]-2)*10),"itemStyle": {"normal": {"color": colorlist[j]}}
                      })

        j=j+1

    for j in range(23):
        category.append({"name": str(j)})
    print(category)

    ii = 0
    links=[]
    ans=[0]*len(number)
    for i in nodes:
        jj = 0
        for j in nodes:
            #ans[ii]!=2:
            if number[ii]==number[jj] and ii>jj and ans[ii]!=control:
                links.append({"source": i.get("name"), "target": j.get("name")})
                ans[ii]=1
            jj=jj+1
        ii=ii+1
    print(links)




    c = (
        Graph(init_opts=opts.InitOpts(width="2000px", height="1200px"))
            .add(
            "",
            nodes=nodes,
            links=links,
            is_roam=True,
            is_focusnode=True,
            categories=category,
            #none,force,circular
            layout=layout,
            repulsion=80,
            is_rotate_label=True,

            #itemstyle_opts=opts.ItemStyleOpts(color=randomcolor()),

            linestyle_opts=opts.LineStyleOpts(color="source", curve=0.3),
            label_opts=opts.LabelOpts(position="right"),
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="词汇关系图"),
            legend_opts=opts.LegendOpts(orient="vertical", pos_left="2%", pos_top="20%"),
        )
            .render(path+".html")
    )


def array_to_chart():
    with open("les-miserables.json", "r", encoding="utf-8") as f:
        j = json.load(f)
        nodes = j["nodes"]
        links = j["links"]
        categories = j["categories"]

    c = (
        Graph(init_opts=opts.InitOpts(width="1000px", height="600px"))
        .add(
            "",
            nodes=nodes,
            links=links,
            categories=categories,
            layout="circular",
            is_rotate_label=True,
            linestyle_opts=opts.LineStyleOpts(color="source", curve=0.3),
            label_opts=opts.LabelOpts(position="right"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Graph-Les Miserables"),
            legend_opts=opts.LegendOpts(orient="vertical", pos_left="2%", pos_top="20%"),
        )
        .render("graph_les_miserables.html")
    )




def example():
    source = ['Penny', 'Penny', 'Amy', 'Bernadette', 'Bernadette', 'Sheldon', 'Sheldon', 'Sheldon', 'Rajesh']
    # Target node names
    target = ['Leonard', 'Amy', 'Bernadette', 'Rajesh', 'Howard', 'Howard', 'Leonard', 'Amy', 'Penny']
    # Edge Weights
    weight = [5, 3, 2, 2, 5, 2, 3, 5, 2]

    # Convert the vector into a adjacency matrix
    adjmat = vec2adjmat(source, target, weight=weight)

    # Initialize
    d3 = d3graph()
    d3.graph(adjmat)
    d3.show()

'''
from communities.algorithms import louvain_method
from communities.visualization import draw_communities
adj_matrix = [...]
communities, frames = louvain_method(adj_matrix)
draw_communities(adj_matrix, communities)
'''

if __name__ == "__main__":
    # layout
    # none,force,circular
    # control
    # path

    xlsx_to_array(layout="force",control=2,path="排序4")
