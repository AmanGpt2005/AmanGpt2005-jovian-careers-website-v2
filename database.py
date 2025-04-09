import sqlalchemy
import os
from sqlalchemy import create_engine,text

db_connection_string= os.environ['DB_CONNECTION_STRING']

engine=create_engine(
  db_connection_string,
  connect_args={
    "ssl":{
      "ssl_ca":"etc/ssl/cert.pem"
    }
  })

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  print("type(result)",type(result))
  result_all=result.all()
  print("type(result_all)",type(result_all))
  first_result=result_all[0]
  print("type(first_result):",type(first_result))
  first_result_dict=dict(result_all[0])
  print("type(first_result_dict):",type(first_result_dict))
  print(first_result_dict)
  