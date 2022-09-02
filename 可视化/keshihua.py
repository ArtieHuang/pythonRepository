import random

import pandas as pd
import numpy as np
from d3graph import d3graph, vec2adjmat
import json

from pyecharts import options as opts
from pyecharts.charts import Graph
from matplotlib import pyplot as plt

PATH="35_分类_result_105词_词汇表.xlsx"



def randomcolor():
    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color = ""
    for i in range(6):
        color += colorArr[random.randint(0,14)]
    print(color)
    return "#"+color

def get_colorlist():
    colorList = []
    for i in range(100):
        colorList.append(randomcolor())
    print(colorList)
    return colorList

def xlsx_to_array():
    wordMatrix= pd.read_excel(PATH,sheet_name="page_1")
    wordMatrix=wordMatrix.iloc[:, [0,1]]
    word=np.array(wordMatrix.iloc[:,0])
    number=np.array(wordMatrix.iloc[:,1])
    colorList=get_colorlist()

    nodes=[]
    category=[]
    j=0
    for i in word:
        nodes.append({"name":i, "category": number[j],"symbolSize":str(random.random()*30),"itemStyle": {"normal": {"color": colorList[number[j]]}}
                      })

        j=j+1


    for j in range(35):
        category.append({"name": str(j)})
    print(category)

    ii = 0
    links=[]
    ans=[0]*len(number)
    for i in nodes:
        jj = 0
        for j in nodes:
            #ans[ii]!=2:
            if number[ii]==number[jj] and ii>jj and ans[ii]!=1:
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
            layout="force",
            repulsion=50,
            is_rotate_label=True,

            #itemstyle_opts=opts.ItemStyleOpts(color=randomcolor()),

            linestyle_opts=opts.LineStyleOpts(color="source", curve=0.3),
            label_opts=opts.LabelOpts(position="right"),
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="词汇关系图"),
            legend_opts=opts.LegendOpts(orient="vertical", pos_left="2%", pos_top="20%"),
        )
            .render("graph_les_miserables8.html")
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
    xlsx_to_array()
