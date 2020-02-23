# data/queries/qryReader.py

import os

def qryRd(qryName):
    qry = os.path.join.dirname(__file__)
    rdQry = open(qry, 'r')
    sqlQry = rdQry.read()
    rdQry.close()
    return sqlQry