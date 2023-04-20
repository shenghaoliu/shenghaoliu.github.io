# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 02:17:46 2023

@author: liush
"""
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Map

# 2022年全国各省份经济数据
data ={
"广东省":129118,
"江苏省":122875,
"山东省":87435,
"浙江省":77715,
"河南省":61345,
"四川省":56749,
"湖北省":53734,
"福建省":53109,
"湖南省":48670,
"安徽省":45045,
"上海市":44652,
"河北省":42370,
"北京市":41610,
"陕西省":32772,
"江西省":32074,
"重庆市":29129,
"辽宁省":28975,
"云南省":28954,
"广西壮族自治区":26300,
"山西省":25642,
"内蒙古自治区":23159,
"贵州省":20164,
"新疆维吾尔自治区":17741,
"天津市":16311,
"黑龙江省":15901,
"吉林省":13070,
"甘肃省":11201,
"海南省":6818,
"宁夏回族自治区":5069,
"青海省":3610,
"西藏自治区":2132,
"香港特别行政区":24279,
"澳门特别行政区":1478,
"台湾省":51298,
}


map_data = list(data.items()) 

c = (
    Map()
    .add("2022年各省经济GDP（单位：亿元）", 
         data_pair=map_data, 
         maptype="china",
         is_map_symbol_show=False, # 不描点             
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="2022年全国经济数据分级设色图"),
        visualmap_opts=opts.VisualMapOpts(min_=0, max_=150000, is_piecewise=True),
    )
)

c.render('./output/全国各省经济数据地图_map.html')