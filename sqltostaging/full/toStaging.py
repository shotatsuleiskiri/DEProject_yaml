# import myFramework.source.posgresql.connect as conn
# import myFramework.utils.utils

class ToStaging:

    def __init__(self, dbname, schema,tablename, tabletype):
        self.dbname = dbname
        self.schema = schema
        self.tablename = tablename
        self.tabletype = tabletype

tostagingfull = ToStaging()
