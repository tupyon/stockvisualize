import pandas as df
import psycopg2
import csv 
import uuid
#stockData=df.read_csv("stock5.csv")

conn = psycopg2.connect("dbname=demodb user=stockapp")
cur = conn.cursor()

with open ("stock5.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[2] is not '' :

            sql =  "INSERT INTO closeprices VALUES('{}','{}','{}','{}')"
            sql = sql.format(row[0],row[1],row[2],uuid.uuid1())
            cur.execute(sql)
            conn.commit()


        #print(row[0],row[1],row[2])


cur.close()
conn.close()

#print(stockData)
#connection = psycopg2.connect("host=192.168.24.97 port=9403 dbname=sampledb user=sayamada password=pssword")