from sqlalchemy_utils import database_exists as db_exists
from sqlalchemy import create_engine


def database_exist(connect_url):
    return db_exists(url=connect_url)


def create_database(user, password, server):
    engine = create_engine("mysql://%s:%s@%s" % (user, password, server))
    engine.execute("CREATE DATABASE ammezzon")
    engine.execute("USE ammezzon")
