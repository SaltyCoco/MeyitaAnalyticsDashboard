import os
import psycopg2
from configparser import ConfigParser

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'queries/pjcconfig.ini')
cfg = ConfigParser()
cfg.read(filename)

class pg_aws_con:
    def __init__(self):
        HOST = os.environ.get('HOST')
        US = os.environ.get('US')
        PS = os.environ.get('PS')
        PORT = os.environ.get('PORT')
        DBNAME = os.environ.get('DBNAME')
        self.aws_pg_conn = psycopg2.connect(
            user=US,
            password=PS,
            host=HOST,
            database = DBNAME,
            port=PORT,
            #sslrootcert=<path to cert>,
            #sslmode='require'
        )
def pg_aws_conn():
    return pg_aws_con()