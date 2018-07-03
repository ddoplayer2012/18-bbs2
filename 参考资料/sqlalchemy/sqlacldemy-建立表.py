#_*_ coding:utf-8 _*_


#sqlacldemy 是一个ORM（对象关系映射）的著名python 框架。

#ORM 优点：隐藏了数据访问细节，使得通用数据库的交互变得简单。不用考虑该死的sql语句。
#ORM使得构造固化数据结构变得简单易行
#缺点：自动化会影响性能


#cx_oracle连接方式

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String

def create_engine_str(db_name = 'orcl',db_user = 'system',db_pass = 'Hello123',db_ip = '192.168.67.124',db_port = '1521'):
    engine_str = "oracle+cx_oracle://" + db_user +  ":" + db_pass + '@' + db_ip + ':' + db_port + '/' +db_name
    return engine_str

db_name = 'orcl'
db_user = 'system'
db_pass = 'map'
db_ip = '192.168.1.108'
db_port = '1521'
a = create_engine_str(db_name,db_user,db_pass,db_ip,db_port)
engine = create_engine(a,encoding='utf-8',echo = True)
base = declarative_base()
print(type(engine))
class user(base):
    __tablename__ = 'user_hehe2' #表名
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

base.metadata.create_all(engine)