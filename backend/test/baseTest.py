import unittest
from fastapi.testclient import TestClient
class BaseTest(unittest.TestCase):
    def setUp(self):
        from api import createApp
        from api.database import engine, init_database
        from api.configs import TESTING
        from sqlalchemy.orm import sessionmaker
        app = createApp(TESTING)
        self.db = sessionmaker(engine)()
        init_database(engine)
        self.client = TestClient(app=app)

    def tearDown(self):
        from api.database import engine, Base
        Base.metadata.drop_all(engine)
        