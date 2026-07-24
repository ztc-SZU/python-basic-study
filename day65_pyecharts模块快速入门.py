# 导包
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts
# 创建一个折线图对象
line=Line()

# 给折线图对象添加x轴数据
line.add_xaxis(['中国','英国','美国'])

# 给折线图对象添加y轴数据
line.add_yaxis("GDP",[30,20,10])

# 设置全局配置项来设置
line.set_global_opts(
    title_opts=TitleOpts("GDP展示",pos_left="center",pos_bottom="1"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)

# 通过render方法将代码生成为对象
line.render()