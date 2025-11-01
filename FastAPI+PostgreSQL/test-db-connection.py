import psycopg2
from psycopg2 import OperationalError

DATABASE_URL = "postgresql://postgres:Monday%40123@localhost/ROOKIES"

try:
    conn = psycopg2.connect(DATABASE_URL)
    print("Connection successful!")
    conn.close()
except OperationalError as e:
    print("Connection failed!")
    print(e)