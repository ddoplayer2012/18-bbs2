'''
所谓ORM实例，就是建立pyhton类到数据库表的映射关系，一个Python实例(INSTANCE)对应数据库中一个一行(ROW),
作用1：实现对象和与之关联的行的数据同步
作用2：涉及数据库的query操作，表达为python类的相互关系
'''

'''
使用范围：
ORM是封装好的sql表达式，适用于一般的sql应用，涉及到定制化程度高的功能时，就需要使用到sql表达式
'''

import sqlalchemy
from sqlalchemy import create_engine
print(sqlalchemy.__version__)  #本机安装的版本，1.2.5

#第一步：建立连接引擎
'''
当第一次执行engine.execute()或者engine.connect(),才会建立连接，一般不会直接使用engine
'''
engine = create_engine('sqlite:///test.db',echo=True)

#第二步：定义映射关系
'''
1.描述要处理的数据库表的信息
2.将python类映射到这些表上
这两个过程是一起完成的，这个过程称之为declarative
declarative base class是含有ORM映射中相关的类和表的信息，通过declarative_base来创建
需要派生这个基类来自定义我们需要操作的用户类。
__tablename__是必须的属性，加上至少一个Column来给出表的主键primary Key
当类声明完成后，declarative会将所有的column成员替换成特殊的python访问器，我们称之为descriptors,这个过程称之为instrumentation(手段)，经过instrumentation的映射类可以让我们能够读取数据库的表和列
'''
from sqlalchemy.ext.declarative import declarative_base
base = declarative_base()
from sqlalchemy import Column,Integer,String
class user(base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<user(name='%s',fullname ='%s',password='%s')>" % (self.name,self.fullname,self.password)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine) #定义数据库的会话类
session = Session()                 #实例化该类
'''
查询遍历方法1：
'''
# for instance in session.query(user).order_by(user.id):
#     print(instance.name,instance.fullname)
# '''
# 查询遍历方法2：与关系，多条件过滤
# '''
# for user in session.query(user).filter(user.name=='ed').filter(user.fullname == 'ed jones'):
#     print(user)

'''
Like    query(user).filter(user.name.like'%ed%')
In      query(user).filter(user.name.in_(['ed','jones','jack']))
not IN  query(user).filter(~user.name.in_(['ed','jones','jack']))
is NOT NULL query(user).filter(user.name != None)
and     query(user).filter(and_(user.name == 'ed',user.fullname =='ed jones'))
match   query(user).filter(user.name.match('ed'))
'''
'''
query().all() 返回一个列表，包含所有匹配结果
query().first() 最多返回一列
query().one()    返回且仅返回一个查询结果，当结果数量不足一个或多于一个的时候会报错

'''
'''

可以嵌入sql 语句：for user in session.query(user).filter(text("id<224")).order_by(text('id')).all()   
嵌入sql2:    session.query(user).filter(text('id<:value and name=:name')).params(value=224,name='fred').order_by(user.id).one()
嵌入sql3:  session.query(user).from_statement(text('select * from users where name=:name')).params(name='ed').all()
session.query(user).count()  跟select count(*)一样
实现最简单的select count(*):   session.query(func.count('*')).select_from(user).scalar()
'''
