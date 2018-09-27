from sqlalchemy_utils import database_exists as db_exists
from sqlalchemy import create_engine


class DatabaseSetupService(object):

    def __init__(self):
        pass

    def database_exist(self, connect_url):
        return db_exists(url=connect_url)

    def create_database(self, user, password, server):
        engine = create_engine("mysql://%s:%s@%s" % (user, password, server))
        engine.execute("CREATE DATABASE ammezzon")
        engine.execute("USE ammezzon")
