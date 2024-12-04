from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

# Database setup
DATABASE_URL = 'sqlite:///../../databases/economic_database.db'

engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    code = Column(String(3), nullable=False)


class Macro(Base):
    __tablename__ = 'macro_indicator'

    id = Column(Integer, primary_key=True)
    country_id = Column(Integer, ForeignKey('countries.id'))
    name = Column(String(50), nullable=False)
    country = relationship('Country', back_populates='macro_indicator')


Country.macro_indicator = relationship('Macro', back_populates='country')

Base.metadata.create_all(bind=engine)