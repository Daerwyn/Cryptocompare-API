import uuid

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from DBManagment.DB_tables import User, Base, ApiCreds


class DBManager:

    def __init__(self, url):
        self.engine = create_engine(url, echo=True)
        self.Session = sessionmaker(bind=self.engine)

    def create_table(self):
        Base.metadata.create_all(self.engine)

    def add_user(self, username, password, api_key):
        session = self.Session()
        user_id = str(uuid.uuid4())
        user = User(id=user_id, username=username, password=password)
        api_creds = ApiCreds(id=user_id, api_key=api_key)
        session.add(user)
        session.add(api_creds)
        session.commit()

    def get_user(self, username):
        session = self.Session()
        user = session.query(User).filter_by(username=username).first()
        if user:
            return user
        else:
            print(f"User '{username}' not found.")
            return None

    # def delete_user(self, user_id):
    #     session = self.Session()
    #     self.user_id = user_id
    #     session.query(User).filter_by(id=self.user_id).delete()
