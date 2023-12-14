import myFramework.source.posgresql.connect as conn
import myFramework.utils

import pandas as pd


class ToStaging:
    
    def __init__(self, dbname, schema):
        self.dbname = dbname
        self.schema = schema
    

