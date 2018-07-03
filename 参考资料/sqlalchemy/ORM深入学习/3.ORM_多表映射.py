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
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
#print(sqlalchemy.__version__)  #本机安装的版本，1.2.5
'''
ForeignKey的含义是这一列的值范围在另外一列的取值范围之内
'''
base = declarative_base()
from sqlalchemy import Column,Integer,String
class address(base):
    __tablename__ = 'addresses'
    id = Column(Integer,primary_key=True)
    email_address = Column(String,nullable=False)
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship('user',back_populates='addresses')

    def __repr__(self):
        return "<address(email_address='%s')>" % (self.email_address)

class user(base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<user(name='%s',fullname ='%s',password='%s')>" % (self.name,self.fullname,self.password)

'''
relationship理解
指向：即定义一张表中的数据条目指向另一张表的中的条目，建立这种有向的指向可以让表以字段的方式查询到被指向的条目，所以要双向查询就需要双向指向
backref:可以通过 user.address   和 address.user 双向访问
back_populates: 只能单向访问 
class A{b = relationship('c')}
class C{}
A可以通过b访问C
b = relationship('c',backref='d')
定义backref后，C也可以通过d访问A


'''
user.addresses =relationship('address',order_by=address.id,back_populates='user')
jack = user(name='jack',fullname='jack ma',password='gjffdd')

jack.addresses = [address(email_address='ma@123.com'),address(email_address='li@4.com')]
print(jack.addresses[1].user)
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///test.db',echo=True)
base.metadata.create_all(engine)
Session = sessionmaker(bind=engine) #定义数据库的会话类
session = Session()
session.add(jack)
session.commit()