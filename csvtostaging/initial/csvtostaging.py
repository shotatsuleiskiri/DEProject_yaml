
import pandas as pd
# import psycopg2
from sqlalchemy import create_engine 

# import time


# read data into Df
data = pd.read_csv("/Users//ramazkapanadze/Downloads/sales_data_sample.csv",  encoding='Latin-1')
df = pd.DataFrame(data)
# print(df)
# hostname = 'localhost'
# database = 'DBStaging'
# username = 'ramazkapanadze'
# pwd = 1604
# port_id = 5432
# conn = None
# cur = None
# # time.sleep(10)

engine = create_engine('postgresql://ramazkapanadze:1604@localhost:5432/DBStaging')

df.to_sql('sales_data', engine,schema='sales', if_exists='append', index=False)

# df1 = pd.DataFrame([{'name':'aaa','age':1}])
# print(df1)
# df1.columns = df1.columns.str.lower()
# df1.to_sql('data', engine,schema='sales', if_exists='append', index=False)






# try:

#   conn = psycopg2.connect(
#     host = hostname,
#     dbname = database,
#     user = username,
#     password = pwd,
#     port = port_id    
#   )

#   cur = conn.cursor()


# except Exception as error:
#   print(error)

# finally:
#   if cur is not None:
#     cur.close()
#   if conn is not None:
#     conn.close()

