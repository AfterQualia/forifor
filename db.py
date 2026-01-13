import psycopg2
conn = psycopg2.connect(database = "foriforDB", user = "postgres", password = "")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS saved_info ("
            "id SERIAL PRIMARY KEY,"
            "hash TEXT,"
            "site TEXT)")
conn.commit()
cur.close()