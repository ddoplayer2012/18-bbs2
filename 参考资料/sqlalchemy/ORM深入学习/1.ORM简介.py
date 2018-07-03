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

#第三步：创建一个模式
'''
通过declarative系统构建好我们的user类之后，与之同时，关于表的信息也已经创建好了，
我们称之为table metadata（表的元数据），描述这些信息的类为table,可以通过__table__这个类变量来查看表信息。
table是metadata的一部分，可以用base.metaclass属性来看 base.metadata.create_all(engine)
metadata是我们与数据库打交道的接口
'''
#base.metadata.create_all(engine)
print(user.__table__)

#第四步：实例化映射类
ed_user = user(name='ed',fullname='ed jones',password='edspassword')
print(ed_user.name)

#第五步：创建会话
'''session是数据库连接的入口，定义一个session来连接数据库

'''
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine) #定义数据库的会话类
session = Session()                 #实例化该类
'''
或者
session = sessionmaker()
session.configure(bind=engine)
'''


#第六步：增改
'''
session需要提交，session.add()只会让user实例的状态pending(等待)，数据库还不会存在这一行
此时如果query数据--flush过程，pending状态会被优先flush,然后负责查询的sql语音会再次之后立即被执行
这种理念称之为identify map,目的是保证在添加的时候，不会出现初始化多个主键相同的行
'''
session.add(ed_user) #如果注释这一行，ed_user不是our_user
#print(ed_user is our_user)#
#多重添加行

ed_user.password='hehehe'
print(session.dirty) #查看当前会话变更的数据
session.add_all([ user(name='ed1',fullname='ed jones',password='edspassword'), user(name='ed2',fullname='ed jones',password='edspassword'),
                  user(name='ed', fullname='ed jones', password='edspassword')
                  ])


print(session.new)   #查看当前会话更新的数据
session.commit()

our_user = session.query(user).filter_by(name='ed').all()
print(our_user)