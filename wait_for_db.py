import psycopg2
import time

params = {
  'database': 'ccm_db',
  'user': 'ccm_user',
  'password': 'ccm_pwd',
  'host': 'db',
  'port': 5432
}

conn = None

while conn is None:
    try:
        conn = psycopg2.connect(**params)
    except psycopg2.OperationalError:
        conn = None
        print("Database not ready, sleeping 1 sec...")
        time.sleep(1)

print("Database is ready, lets migrate all the things!!!")
