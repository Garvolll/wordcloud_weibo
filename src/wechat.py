# coding:utf-8;
import requests
from PIL import Image, ImageSequence
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import jieba.analyse
from time import sleep
from collections import OrderedDict
import sys
import itchat
from echarts import Echart, Legend, Pie

itchat.login()

friends = itchat.get_friends(update=True)[0:]

male = female = other = 0

for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1

total = len(friends[1:])


chart = Echart(u'%s的微信好友性别比例' % (friends[0]['NickName']), 'from WeChat')
chart.use(Pie('WeChat',
              [{'value': male, 'name': u'男性 %.2f%%' % (float(male) / total * 100)},
               {'value': female, 'name': u'女性 %.2f%%' % (float(female) / total * 100)},
               {'value': other, 'name': u'其他 %.2f%%' % (float(other) / total * 100)}],
              radius=["50%", "70%"]))
chart.use(Legend(["male", "female", "other"]))
del chart.json["xAxis"]
del chart.json["yAxis"]
chart.plot()