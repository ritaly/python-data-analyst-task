import psycopg2


db_connection = psycopg2.connect(
    host="********************",
    user="********************",
    password="********************",
    dbname="********************",
)


cur = db_connection.cursor()
cur.execute("SELECT * FROM public.pdsdat LIMIT 884;")


print(cur.fetchall())
cur.close()
