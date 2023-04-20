# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 18:17:28 2023

@author: liush
"""

import re
from collections import Counter
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from pyecharts.charts import WordCloud
import pyecharts.options as opts


# 读取文本文件
with open(r'C:\Users\liush\OneDrive\桌面\python\作业\Systematic_Trading.txt', "r", encoding="utf-8") as f:
    text = f.read()

# 将文本转换为小写
text = text.lower()

# 剔除标点符号和数字
text = re.sub("[^a-z ]", "", text)

# 分词
tokens = word_tokenize(text)

# 词性标注
pos_tags = pos_tag(tokens)

# 剔除副词、连接词和停用词
stop_words = set(stopwords.words("english"))
filtered_tokens = []
for word, pos in pos_tags:
    if pos.startswith("N") and word not in stop_words:
        filtered_tokens.append(word)
words = [word for word in tokens if word.isalpha() and word not in stop_words]

# 计算单词频率
word_freq = Counter(words)
top_words = word_freq.most_common(40)

# 构建词云图
wordcloud = WordCloud()
wordcloud.add("", top_words)

# 设置词云图参数
wordcloud.set_global_opts(title_opts=opts.TitleOpts(title="Systematic trading WordCloud"))
wordcloud.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))

# 显示词云图
wordcloud.render("Systematic trading wordcloud.html")

