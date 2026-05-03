from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///weather.db")

df = pd.read_sql("SELECT * FROM weather", engine)
print(df)