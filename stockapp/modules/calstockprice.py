import pandas as df
import psycopg2
import csv 
import uuid
from operator import itemgetter
#stockData=df.read_csv("stock5.csv")

class stock_calculate():

    @classmethod
    def calculate_closeprice(cls):
        datediff=[]
        stockdata=[]
        #sql =  "select max(stockdate) from closeprices;"
        sql =  "select distinct stockdate  from closeprices  order by stockdate desc limit 2;"
        conn = psycopg2.connect("dbname=demodb user=stockapp")
        with conn.cursor() as cur:
            cur.execute(sql)
            for row in cur:
                datediff.append(row)
        #        sql="select symbol,stockdate,price from closeprices where stockdate = row[0]"
            #    sql = sql.format(row[0],row[1],row[2],uuid.uuid1())
        #    conn.commit()

        with conn.cursor() as cur:
            for datestr in datediff:
                sql="select symbol,stockdate,price from closeprices where stockdate = '{}'"
                sql = sql.format(datestr[0])
                cur.execute(sql)
                for row in cur:
                    stockdata.append(row)


        tickersymbols=[]
        with conn.cursor() as cur:
            sql="select distinct symbol from closeprices order by symbol;"
            cur.execute(sql)
            tickersymbols = cur.fetchall()
            # for row in cur:
            #     tickersymbols.append(row)
        cur.close()
        conn.close()

        newStockData=[]
        for symbol in tickersymbols:
            tmpstockdata=[]
            for row in stockdata:
                if row[0] == symbol[0]:
                    tmpstockdata.append(row)
            if tmpstockdata[1][1] > tmpstockdata[0][1]:
                tmpdiffvalue = tmpstockdata[1][2] - tmpstockdata[0][2]
                tmpvalue = tmpstockdata[1][2]
                tmpdate = tmpstockdata[1][1]
                tmpratio = tmpdiffvalue / tmpstockdata[0][2] * 100
            else:
                tmpdiffvalue = tmpstockdata[0][2] - tmpstockdata[1][2]
                tmpvalue = tmpstockdata[0][2]
                tmpdate = tmpstockdata[0][1]
                tmpratio = tmpdiffvalue / tmpstockdata[1][2] * 100
            valuedata=[symbol[0],tmpdate,"{:>}".format(tmpvalue) ,round(tmpdiffvalue,2),round(tmpratio,2)]
            newStockData.append(valuedata)

        return newStockData

    @classmethod
    def calculate_upside_ratio(cls):
        stockdata=[]

        stockdata = cls.calculate_closeprice()
        
        stockdata.sort(key=itemgetter(4),reverse=True) 

        return stockdata

    @classmethod
    def calculate_downside_ratio(cls):
        stockdata=[]
        stockdata = cls.calculate_closeprice()
        stockdata.sort(key=itemgetter(4))         
        return stockdata


#calculate = stock_calculate()
#calculate.calculate_closeprice()        
#stock_calculate.calculate_upside_ratio()           
#stock_calculate.calculate_downside_ratio()

