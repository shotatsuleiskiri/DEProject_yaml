import myFramework.source.posgresql.connect as conn
import myFramework.utils.utils as utils

import pandas as pd


class ToStaging:
    
    def __init__(self, dbname, schema):
        self.dbname = dbname
        self.schema = schema
    
    def getDF(self, source_dbname, tablename):
        return pd.read_sql(f"select * from {self.schema}.{tablename}"
                        ,conn.getConnection(source_dbname))
