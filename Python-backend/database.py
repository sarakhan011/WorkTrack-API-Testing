from sqlalchemy import create_engine

DATABASE_URL = "mysql+pymysql://root:abc1234@localhost:3306/worktrack"

engine = create_engine(DATABASE_URL)

try:
    connection = engine.connect()
    print("Connected to MySQL successfully!")
    connection.close()

except Exception as e:
    print("Connection failed:")
    print(e)
