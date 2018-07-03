#_*_ coding:utf-8 _*_
from hh import models

#初始化目录

obj1 = models.Catalog(name='新闻',catalog_url='news')
obj1.save()


obj2 = models.Catalog(name='社会',catalog_url='social')
obj2.save()


obj2 = models.Catalog(name='八卦',catalog_url='gossip')
obj2.save()

