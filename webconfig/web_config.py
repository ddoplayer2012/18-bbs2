
# -*- coding: utf-8 -*-
import configparser
import os,sys
BASE_DIR = os.path.dirname(__file__)
'''
通过设置配置文件来标记是否初始化插入数据库数据，由view来读取
'''


def init_db():
    #初始化配置
    if not os.path.exists(BASE_DIR + '/web.ini'):
        config = configparser.ConfigParser()
        # set a number of parameters
        config.add_section("INITDB")
        config.set("INITDB","inited","no")
        # write to file
        config.write(open(BASE_DIR + '/web.ini', "w"))

def inited_db():
    #修改配置
    config = configparser.ConfigParser()
    config.read(BASE_DIR + '/web.ini')
    config.set("INITDB", "inited", "yes")
    config.write(open(BASE_DIR + '/web.ini', "w"))

def init_check():
    #检查读取配置
    config = configparser.ConfigParser ()
    config.read (BASE_DIR + '/web.ini')
    a = config.get ("INITDB", "inited")
    return a

