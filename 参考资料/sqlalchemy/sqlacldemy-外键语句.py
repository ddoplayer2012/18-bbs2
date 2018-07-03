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
from sqlalchemy import orm
from sqlalchemy import ForeignKey


def create_engine_str(db_name = 'orcl',db_user = 'admin',db_pass = 'admin',db_ip = '192.168.67.124',db_port = '1521'):
    engine_str = "oracle+cx_oracle://" + db_user +  ":" + db_pass + '@' + db_ip + ':' + db_port + '/' +db_name
    return engine_str

db_name = 'orcl'
db_user = 'admin'
db_pass = 'admin'
db_ip = '127.0.0.1'
db_port = '1521'
a = create_engine_str(db_name,db_user,db_pass,db_ip,db_port)
engine = create_engine(a,encoding='utf-8',echo = True)
base = declarative_base()
class Hosts(base):
    '''
    继承declarative_base类，用来操作数据库连接对象,这个用来存储表对象。。
    Foreign key associated with column 'addresses.user_id' could not find table 'user_hehe2' with which to generate a foreign key to target column 'id'
    '''
    __tablename__ = 'ADDRESSES' #表名user_hehe2
    id = Column(Integer,primary_key=True)
    email = Column(String(32),nullable=False)
    user_id = Column(Integer,ForeignKey('USER_HEHE2.ID'))
    user =orm.relationship('USER_HEHE2',backref='ADDRESSES') #这个可以通过backref字段反向查出所有它在addresses表里的关联项

    def __repr__(self):
        #查询语句的返回值作调整
        return "<user(email='%s')>" % (self.email)


# class user(base):
#     '''
#     继承declarative_base类，用来操作数据库连接对象
#     '''
#     __tablename__ = 'user_hehe2' #表名
#     id = Column(Integer,primary_key=True)
#     name = Column(String(32))
#     password = Column(String(64))
#
#     def __repr__(self):
#
#         return "<user(name='%s',password='%s')>" % (self.name,self.password)


session_class = orm.sessionmaker(bind=engine)
session = session_class()
base.metadata.create_all(engine)
#ser_obj = user(name = 'c1',id = 5,password='hahaha')   #插入的核心代码

try:
    pass

except Exception as e:
    print(e)
