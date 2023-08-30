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
    
    
class PreformaDB(Base):
    __tablename__ = 'preforma'
    
    preforma_id = Column(Integer, primary_key=True, nullable=False)
    numer_form = Column(String, nullable=False)
    gwint = Column(String, nullable=False)
    gramatura = Column(Integer, nullable=False)
    indeks = Column(String, nullable=False)
    maszyna = Column(String, nullable=False)
    koszt = Column(Integer, nullable=False)
    ilosc_gniazd = Column(Integer, nullable=False)
    czas_cyklu = Column(Integer, nullable=False)
    wydajnosc_na_godzinu = Column(Integer, nullable=False)
    material = Column(String, nullable=False)
    p1_p3 = Column(Integer, nullable=False)
    dlugosc_preformy = Column(Integer, nullable=False)
    