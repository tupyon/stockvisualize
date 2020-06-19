import pandas as df
import psycopg2
import csv 
import uuid
from operator import itemgetter


class output_stock_detaildata():

    @classmethod
    def output_history(cls,findname):
        stockdata=[]
        #sql =  "select max(stockdate) from closeprices;"
        sql =  "select distinct stockdate  from closeprices where symbol = '{}' order by stockdate desc;"
        sql = sql.format(findname)
        conn = psycopg2.connect("dbname=demodb user=stockapp")
        with conn.cursor() as cur:
            cur.execute(sql)
            for row in cur:
                stockdata.append(row)

        #        sql="select symbol,stockdate,price from closeprices where stockdate = row[0]"

            #    sql = sql.format(row[0],row[1],row[2],uuid.uuid1())
        #    conn.commit()
        print (stockdata)
        return stockdata


#output_stock_detaildata.output_history('QQQ')
