# coding:utf-8
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import pymysql
pymysql.install_as_MySQLdb()

DB_URI = "mysql+mysqldb://root:1234@192.168.1.2:3306/myweb?charset=utf8"


engine = create_engine(DB_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()

# 创建一个多对多的关系(老师与学生的关系)需要创建一个中间表
# 创建一个中间表
teacher_classes = Table(
    "teacher_classes",
    Base.metadata,
    Column("teacher_id", Integer, ForeignKey("teacher.id"), nullable=False, primary_key=True),
    Column("classes_id", Integer, ForeignKey("classes.id"), nullable=False, primary_key=True)
)


# 创建老师的映射
class Teacher(Base):
    __tablename__ = "teacher"
    id = Column(Integer, primary_key=True, autoincrement=True)
    teacher_name = Column(String(100))
    classes = relationship("Classes", secondary=teacher_classes)

    def __repr__(self):
        return "<Teacher id='%s' teacher_name='%s'>" % (self.id, self.teacher_name)


# 创建学生的映射
class Classes(Base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    classes_name = Column(String(100))
    teacher = relationship("Teacher", secondary=teacher_classes)

    def __repr__(self):
        return "<Classes id='%s' classes_name='%s'>" % (self.id, self.classes_name)


# 创建数据库
Base.metadata.create_all()

#创建两个老师
teacher1 = Teacher(id=1,teacher_name='admin')
teacher2 = Teacher(id=2,teacher_name='grunt')
teacher3 = Teacher(id=3,teacher_name='shuihen')

# 创建两门课程
classes1 = Classes(id=1,classes_name="java")
classes2 = Classes(id=2,classes_name="python")

# 添加数据
teacher1.classes = [classes1,classes2]
teacher2.classes = [classes1,classes2]
teacher3.classes = [classes1]
session.add(teacher1)
session.add(teacher2)
session.add(teacher3)
session.commit()

# 查询下数据(根据老师查询课程)
teacher = session.query(Teacher).first()
print(teacher.classes)

# 根据课程查询老师
classes = session.query(Classes).get(1)
print(classes.teacher)

# 根据老师查询课程
teacher = session.query(Teacher).get(3)
print(teacher.classes)