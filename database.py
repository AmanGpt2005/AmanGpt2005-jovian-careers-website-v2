import sqlalchemy
from sqlalchemy import create_engine,text
engine=create_engine("mysql+pymysql://sql12770857:ad4MXKybts@sql12.freesqldatabase.com/sql12770857?charset=utf8mb4")

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
  