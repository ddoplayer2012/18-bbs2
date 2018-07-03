#_*_ coding:utf-8 _*_


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey,DATE,Table
from sqlalchemy.orm import relationship,sessionmaker
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
    book2author = Table('book2author',base.metadata,
                        Column('book_id',Integer,ForeignKey('books.id')),
                        Column('author_id',Integer,ForeignKey('authors.id')),
                        )
    class book(base):
        __tablename__ = 'books' #表名
        id = Column(Integer,primary_key=True)
        name = Column(String(64))
        pub_date = Column(DATE)
        authors = relationship('Author',secondary=book2author,backref='books')
        def __repr__(self):
            return self.name
    class author(base):
        __tablename__ = 'authors'
        id = Column(Integer,primary_key=True)
        name = Column(String(32))
        def __repr__(self):
            return self.name

    base.metadata.create_all(engine)
    session_class = sessionmaker(bind=engine)
    s = session_class()
    b1 = book(name='book1')
    b2 = book(name='book2')
    b3 = book(name='book3')
    b4 = book(name='book4')
    a1 =author(name='zhao')
    a2 = author(name='qian')
    a3 = author(name='sun')
    b1.authors = [a1,a2]
    b2.authors = [a1,a2,a3]
    s.add_all([b1,b2,b3,b4,a1,a2,a3])
    s.commit()

    #base.metadata.create_all(engine)

DB_FILE_PATH = os.path.join(BASE_DIR,'db','database.db')
if not os.path.exists(DB_FILE_PATH):
    create_db(True)