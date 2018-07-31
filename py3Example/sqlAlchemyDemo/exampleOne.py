# -*- encoding:utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker

__author__ = 'bida'

from sqlalchemy import create_engine

# engine = create_engine('sqlite:///:memory:', echo=False)
engine = create_engine('sqlite:///demo.db', echo=False)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='{0}',fullname='{1}',password='{2}')>".format(self.name, self.fullname, self.password)

print(User.__tablename__)
print(User)
Base.metadata.create_all(engine)
ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
print(ed_user.name)
print(ed_user.password)
print(str(ed_user.id))

Session = sessionmaker(bind=engine)
session = Session()
session.add(ed_user)

session.add_all([
    User(name='Wendy', fullname='Wendy Willmax', password='fooar'),
    User(name='mary', fullname='Mary Contrary', password='xxg427'),
    User(name='fred', fullname='Fred flinstone', password='blss')
])
session.commit()
# session.rollback()
# print(session.query(User).all())
# our_user = session.query(User).filter_by(name='mary').first()
# our_users = session.query(User).order_by(User.password).all()
# print(our_user)
# print(our_user is ed_user)
# print(our_users)
#
# ed_user.password='f8s7ccs'
# print(ed_user.password)
# print(session.dirty)
# print(session.query(User).filter_by(name='ed').first().password)
