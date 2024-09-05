import uuid

from sqlalchemy import String, Column, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

DB_url = 'mysql+mysqlconnector://root:12344321@127.0.0.1:3307/Cryptocompare'
engine = create_engine(DB_url, echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(String(36), primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    api_creds = relationship("ApiCreds", back_populates="user", uselist=False)

    # def create(self, username, password):
    #     id = str(uuid.uuid4())
    #     self.session.add(User(id, username, password))
    #     self.session.flush()
    #     self.session.commit()
    #     return id


class ApiCreds(Base):
    __tablename__ = 'api_creds'

    id = Column(String(36), ForeignKey('user.id'), primary_key=True)
    api_key = Column(String(255), unique=True, nullable=False)

    user = relationship("User", back_populates="api_creds", uselist=False)

    # def create(self, api_key):
    #     id = str(uuid.uuid4())
    #     self.session.add(ApiCreds(id, api_key))
    #     self.session.flush()
    #     self.session.commit()
    #     return id
# Base.metadata.create_all(engine)

# with Session() as session:
#     with session.begin():
#         AbstractModel.metadata.create_all(engine)
#         user = User(username='assdaswd', password='awsds')
#         session.add(user)
#         api_keys = ApiCreds(api_key='hjhwkkj')
#         session.add(api_keys)
#         session.commit()
