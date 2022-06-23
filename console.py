import pymysql

con = pymysql.connect(host="localhost",
                         user="root",
                         password="Montreal@9856",
                         database="sports")
try:
    with con.cursor() as cur:
        cur.execute('SELECT Player, Team, sum(Points) from seasons group by Team having sum(Points) > 4000')
        rows = cur.fetchall()
        for row in rows:
            print(row)
finally:
    con.close()