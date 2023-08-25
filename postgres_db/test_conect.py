import psycopg2
from psycopg2.extras import RealDictCursor
import time
from dotenv import load_dotenv

load_dotenv()
import os




url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")




while True:   
    try:
        conn = psycopg2.connect(host=url, database='postgres', user='postgres',
                                password=key, cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful")
        break

    except Exception as error:
            print('Conection to database failed')
            print("Error:",  error)
            time.sleep(2)