from django.db import models
#_*_ coding:utf-8 _*_

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey,DATE,Table
from sqlalchemy import orm
from sqlalchemy.orm import relationship
import pymysql
pymysql.install_as_MySQLdb()

DB_URI = "mysql+mysqldb://root:1234@192.168.1.2:3306/myweb?charset=utf8"


engine = create_engine(DB_URI,encoding='utf-8',echo = False,isolation_level="READ UNCOMMITTED")
base = declarative_base()

session_class = orm.sessionmaker(bind=engine)
session = session_class() #session 留着有用


user2groups = Table(
    "user2groups",
    base.metadata,
    Column("user_name", String(64), ForeignKey("users.username"), nullable=False, primary_key=True),
    Column("group_name", String(64), ForeignKey("groups.groupname"), nullable=False, primary_key=True)
)

class Groups(base):
    __tablename__ = 'groups'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    host = relationship("Hosts",  backref="Groups")

    groupname = Column (String (64), unique=True)
    users = relationship('Users',secondary='user2groups')

class Hosts(base):
    __tablename__ = 'hosts' #表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    ipaddr =  Column(String(32),unique=True)#,comment='IP地址')
    port = Column(String(32))
    login_username = Column(String(32))
    login_password = Column(String(64))
    group = Column(String(64), ForeignKey('groups.groupname'))
    is_online = Column(String(64))#,comment='是否在线')
    add_time = Column(String(32))#,comment='添加日期')
    describtion = Column(String(64))#,comment='描述')

class Users(base):
    __tablename__ = 'users'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column (String (64), unique=True)
    password = Column (String (64))
    group = relationship('Groups',secondary='user2groups')
    describtion = Column (String (64))#,comment='描述')

def init_create_table():
    #初始化创建表
    base.metadata.create_all(engine)

