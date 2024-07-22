"""
    CONFIG THE DATABASE
"""
from api.configs.config import Setting
from redis import Redis
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session
from sqlalchemy_utils import create_database, database_exists


engine = create_engine(Setting.DATABASE_URL)

 
# redisDB: Redis|None = None
# if Setting.REDIS_DATABASE_URL:
#     redisDB = Redis.from_url(Setting.REDIS_DATABASE_URL, db=0)


def get_db():
    with Session(engine, autoflush=True) as session:
        yield session



#-------------- Dans ce bloc sera importés tous les models 

from .basetemplate import BaseTemplate
from .models import Base, User, Task

#-------------------------------------------------
        
def init_database(engine:Engine):
    if not database_exists(engine.url):
        create_database(engine.url) 
    from .models import Base
    Base.metadata.create_all(engine)