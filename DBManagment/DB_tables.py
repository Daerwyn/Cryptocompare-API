from sqlalchemy import String, Column, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base

DB_url = 'mysql+mysqlconnector://root:12344321@127.0.0.1:3307/Cryptocompare'
engine = create_engine(DB_url, echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(String(36), primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    api_creds = relationship("ApiCreds", back_populates="user", uselist=False)


class ApiCreds(Base):
    __tablename__ = 'api_creds'

    id = Column(String(36), ForeignKey('user.id'), primary_key=True)
    api_key = Column(String(255), unique=True, nullable=False)

    user = relationship("User", back_populates="api_creds", uselist=False)
