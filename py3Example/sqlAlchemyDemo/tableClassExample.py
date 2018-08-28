# -*- coding: utf-8 -*-
# Created by bida on 2018/8/1
from datetime import datetime

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, ForeignKey, UniqueConstraint, \
    DateTime, Index, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker

engine = create_engine('sqlite:///demo.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
# metadata = MetaData(bind=engine)
#
# # method one
# users = Table('users', metadata,
#               Column('id', Integer, primary_key=True, autoincrement=True),
#               Column('name', String(50), nullable=False, unique=True, comment='姓名'),
#               Column('fullname', String(50)),
#               Column('password', String(12)),
#               Column('graduated', Float)
#               )
#
# addresses = Table('addresses', metadata,
#                   Column('id', Integer, primary_key=True),
#                   Column('user_id', None, ForeignKey('users.id')),
#                   Column('email_address', String(64), nullable=False)
#                   )
#
#
# userPost = Table('user_post', metadata,
#                  Column('id', Integer, primary_key=True, autoincrement=True),
#                  Column('user_id', Integer),
#                  Column('post_id', Integer),
#                  Column('insert_time', DateTime),
#                  UniqueConstraint('user_id', 'post_id', name='uix_user_post_user_id_post_id'),
#                  Index('uix_user_post_user_id_post_id', 'user_id', 'post_id')
#                  )
# metadata.create_all()

# method two


# 1vs1
# class User(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True)
#     address = relationship('address', backref=backref("user", uselist=False))
#
#
# class Address(Base):
#     __tablename__ = 'address'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(None, ForeignKey('user.id'))

# n vs n
def nToN():
    Base = declarative_base()

    class UserInfo(Base):
        __tablename__ = 'userinfo'
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String(64), unique=True)
        ctime = Column(DateTime, default=datetime.now())

    association_table = Table('association', Base.metadata,
                              Column('parent_id', Integer, ForeignKey('parent.id')),
                              Column('child_id', Integer, ForeignKey('child.id'))
                              )

    class Parent(Base):
        __tablename__ = 'parent'
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String(32), unique=True)
        children = relationship("Child", secondary=association_table, back_populates="parents")

    class Child(Base):
        __tablename__ = 'child'
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String(32), unique=True)
        parents = relationship("Parent", secondary=association_table, back_populates="children")

    Base.metadata.create_all(engine)

    parent = Parent(name='Parent')
    parent2 = Parent(name='Parent2')

    session.add(parent)
    session.add(parent2)

    child = Child(name='child')
    child2 = Child(name='child2')

    parent.children = [child, child2]
    parent2.children = [child, child2]
    child.parents = [parent, parent2]
    child2.parents = [parent, parent2]

    my_parent = session.query(Parent).filter(Parent.id==1).first()
    my_child = my_parent.children[0]
    # session中已更新，在commit后更新至数据库
    my_child.name = 'child3'

    # 删除对象时自动解绑
    session.delete(my_parent)
    session.commit()
    session.close()


def oneToN():
    class Teacher(Base):
        __tablename__ = 'teacher'
        id = Column(Integer, primary_key=True)
        name = Column(String(32))
        students = relationship('Student', backref='teacher')

    class Student(Base):
        __tablename__ = 'student'
        id = Column(Integer, primary_key=True)
        teacher_id = Column(Integer, ForeignKey('teacher.id'))
        # teacher = relationship('Teacher', backref='students')
        name = Column(String(32))

    Base.metadata.create_all(engine)

    teacher = Teacher(name='Teacher')
    session.add(teacher)

    student = Student(name='student')
    student2 = Student(name='student2')

    teacher.students = [student, student2]
    session.commit()
    print(teacher.students)
    print(student.teacher)
    session.close()


def nTo1():
    class School(Base):
        __tablename__ = 'school'
        id = Column(Integer, primary_key=True)
        city_id = Column(Integer, ForeignKey('city.id'))
        city = relationship('City', backref='school')
        name = Column(String(32))

    class City(Base):
        __tablename__ = 'city'
        id = Column(Integer, primary_key=True)
        name = Column(String(32))

    Base.metadata.create_all(engine)

    city = City(name='harbin')

    school = School(name='school', city=city)
    school2 = School(name='school2', city=city)
    session.add(school)
    session.add(school2)
    session.commit()
    # 同时删除school中的外键
    # session.delete(city)
    # session.commit()
    session.close()

def oneToOne():
    class Husband(Base):
        __tablename__ = 'husband'
        id = Column(Integer, primary_key=True)
        name = Column(String(32))
        wife = relationship('Wife', uselist=False, back_populates='husband')

    class Wife(Base):
        __tablename__ = 'wife'
        id = Column(Integer, primary_key=True)
        name = Column(String(32))
        husband_id = Column(Integer, ForeignKey('husband.id'))
        husband = relationship('Husband', uselist=False, back_populates='wife')

    Base.metadata.create_all(engine)
    husband = Husband(name='Bob')
    wife2 = Wife(name='Eva', husband=husband)
    wife = Wife(name='lily', husband=husband)
    session.add(wife)
    session.add(wife2)
    session.commit()


    session.close()

if __name__ == '__main__':
    nToN()
    # oneToN()
    # nTo1()
    # oneToOne()