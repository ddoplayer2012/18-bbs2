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
    继承declarative_base类，用来操作数据库连接对象,这个用来存储表对象。。
    '''
    __tablename__ = 'user_hehe2' #表名
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        #查询语句的返回值作调整
        return "<user(name='%s',password='%s')>" % (self.name,self.password)
session_class = orm.sessionmaker(bind=engine)
session = session_class()

#ser_obj = user(name = 'c1',id = 5,password='hahaha')   #插入的核心代码

try:
    # my_user = session.query(user).filter_by(name='c1').first() #查询
    # print(my_user)
    # #修改---修改该实例，然后提交会话
    # my_user.name = 'hehe'
    # session.commit()
   # my_user1 = session.query(user).filter_by(name='hehe').first() #修改后查询
    #print(my_user1)
    #回滚
    #session.rollback()
    #查询所有数据
    #print(session.query(user).all())
    #多条件查询
    #objs = session.query(user).filter(user.id>0).filter(user.id<7).all()
    #print(objs)
    #统计和分组
    #s = session.query(user).filter(user.name.like('he%')).count()
    #print(s)
    #分组
    # from sqlalchemy import func
    # x = session.query(func.count(user.name),user.name).group_by(user.name).all()
    # print(x)
    pass
except Exception as e:
    print(e)
