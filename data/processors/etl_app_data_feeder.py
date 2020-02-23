# data/processors/etl_app_data_feeder.py


import pandas as pd

from data.queries.qryReader import qryRd
from data.queries.pg_conns import pg_aws_conn

con = pg_aws_conn()

df = pd.read_sql(sql=qryRd("rev_in"), con=con.aws_pg_conn)
name = "mainDataSet"
file = "main/" + ".csv"
df.to_csv(file, index=False)

