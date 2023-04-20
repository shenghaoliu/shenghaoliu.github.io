# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 14:14:25 2023

@author: liush
"""

from pyecharts import options as opts
from pyecharts.charts import Bar, Line
from pyecharts.faker import Faker

v1 = [4.33,4.56,4.53,4.14,4.13,4.65,4.30,5.68,6.10]
v2 = [3.30,7.96,8.31,1.49,5.23,6.75,3.79,6.88,3.88]
v3 = [38.13,31.16,24.83,21.52,21.99,24.55,20.90,25.83,23]


bar = (
    Bar()
    .add_xaxis(["2014","2015","2016","2017","2018", "2019", "2020", "2021", "2022"])
    .add_yaxis("净利润", v1)
    .add_yaxis("净现金流", v2)
    .extend_axis(
        yaxis=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(formatter="{value} %"), interval=10
        )
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="承德露露财报分析"),
        yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value}亿元")),
        datazoom_opts=opts.DataZoomOpts(),
        toolbox_opts=opts.ToolboxOpts(), # 显示工具栏
        legend_opts=opts.LegendOpts(is_show=True) #是否显示图例
    )
)
bar.set_colors(['red','darkblue'])

line = (
        Line()
        .add_xaxis(["2014","2015","2016","2017","2018", "2019", "2020", "2021", "2022"])
        .add_yaxis("ROE", v3, yaxis_index=1)# 使用的 y 轴的 index，在单个图表实例中存在多个 y 轴的时候有用
)
line.set_series_opts(
    linestyle_opts={
        'color': 'yellow',  # 折线颜色
        'width': 3,      # 折线宽度
    }
)

bar.overlap(line)
bar.render("./output/承德露露基本面分析.html")