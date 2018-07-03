#_*_ coding:utf-8 _*_


#sqlacldemy 是一个ORM（对象关系映射）的著名python 框架。


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy import orm

def create_engine_str(db_name = 'orcl',db_user = 'system',db_pass = 'Hello123',db_ip = '192.168.67.124',db_port = '1521'):
    engine_str = "oracle+cx_oracle://" + db_user +  ":" + db_pass + '@' + db_ip + ':' + db_port + '/' +db_name
    return engine_str

db_name = 'orcl'
db_user = 'system'
db_pass = 'Hello123'
db_ip = '192.168.67.124'
db_port = '1521'
a = create_engine_str(db_name,db_user,db_pass,db_ip,db_port)
engine = create_engine(a,encoding='utf-8',echo = False)
base = declarative_base()
class user(base):
    '''
    继承declarative_base类，用来操作数据库连接对象
    '''
    __tablename__ = 'user_hehe2' #表名
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):

        return "<user(name='%s',password='%s')>" % (self.name,self.password)
session_class = orm.sessionmaker(bind=engine)
session = session_class()

user_obj = user(name = 'c1',id = 5,password='hahaha')   #插入的核心代码
#user_obj = user()
print(user_obj.name,user_obj.id)

session.add(user_obj)  #把插入的事务添加到会话里
try:
    session.commit() #提交

except Exception as e:
    print(e)
print(user_obj.name,user_obj.id)
