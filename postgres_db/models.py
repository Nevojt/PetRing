from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()
class Post(Base):
    __tablename__ = 'kurs'
    
    kurs_id = Column(Integer, primary_key=True, nullable=False)
    surowiec = Column(String, nullable=False)
    cena_za_kg = Column(String, nullable=False)
    date_time = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    