from snapshot_selenium import snapshot as driver

from pyecharts import options as opts
from pyecharts.charts import Graph
from pyecharts.render import make_snapshot
from pyecharts.globals import CurrentConfig,NotebookType

CurrentConfig.NOTEBOOK_TYPE=NotebookType.JUPYTER_LAB



class Graph(
    # 初始化配置项，参考 `global_options.InitOpts`
    init_opts: opts.InitOpts = opts.InitOpts()
)