#_*_ coding:utf-8 _*_


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
import sys,os
BASE_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def create_db(debug=False):
    '''
    如果数据库文件不存在，则初始化数据库
    debug = True打印ORM输出信息，默认False
    :return:
    '''
    str = "sqlite:///%s/db/database.db"%(BASE_DIR)
    engine = create_engine(str,encoding='utf-8',echo = debug)
    base = declarative_base()

    class user(base):
        __tablename__ = 'user' #表名
        id = Column(Integer,primary_key=True)
        name = Column(String(32))
        password = Column(String(64))

    base.metadata.create_all(engine)

DB_FILE_PATH = os.path.join(BASE_DIR, 'db', 'database.db')
if not os.path.exists(DB_FILE_PATH):
    create_db()