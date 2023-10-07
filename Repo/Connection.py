import sqlalchemy as orm
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session

# engine = orm.create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/ab")
engine = orm.create_engine("postgresql+psycopg2://postgres:hqoimvzaxhftiu:8857665ab8200572647dc7c9aecbf85ec7713de38448fd6bc1c1f1aba208a095@ec2-44-213-228-107.compute-1.amazonaws.com:5432/dbjntf8oshmfl1")
db = scoped_session(sessionmaker(bind=engine))
# Base.query= db.query_property()
class _Base(object):
    query= db.query_property()
Base = declarative_base(cls=_Base)

Base.metadata.create_all(engine)