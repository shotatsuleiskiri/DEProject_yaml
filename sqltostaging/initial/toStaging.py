
import psycopg2
import pandas as pd
from sqlalchemy import create_engine


class ToStaging:

    def __init__(self, dbname, schema):
        self.dbname = dbname
        self.schema = schema
    
    def getConnection(self, dbname):
        return create_engine(f'postgresql://ramazkapanadze:1604@localhost:5432/{dbname}')        

    def getTbaleList(self, schema):
        return pd.read_sql(f"select tablename  from pg_catalog.pg_tables where schemaname = '{schema}'",self.getConnection(self.dbname).connect())

    def getDF(self, tablename):
        # Read data from PostgreSQL database table and load into a DataFrame instance
        return pd.read_sql(f"select * from {self.schema}.{tablename}", self.getConnection(self.dbname).connect())

    def fillstaging(self,df, dbname,schema, tablename):
        df.to_sql(tablename, self.getConnection(dbname), schema=f"{schema}", if_exists='replace', index=False)
       

test = ToStaging("dvdrental", "public")

tbname_Df = test.getTbaleList(test.schema)['tablename']

for tbname in tbname_Df:    
    test.fillstaging(test.getDF(tbname),"DBStaging","dvdrental",tbname)
