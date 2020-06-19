import unittest
import pandas_datareader.data as web
import pandas as pd
from pandas_datareader.nasdaq_trader import get_nasdaq_symbols
from datetime import datetime
from tqdm import tqdm

#symbols.head()
class gather_stockinfo():
    startday=datetime(2000,1,1)
    #startday=datetime(2020,5,1)
    today = datetime.today()
    endday=today
    #tiker名取得
    @classmethod
    def fetch_symbols(cls,symbol):
        symbols = get_nasdaq_symbols()
        tmpsymbols=symbols.iloc[:,[1,4,7,9]]
        symbol_data =tmpsymbols.loc[symbol]
        return symbol_data

    #result表示用(history用)
    @classmethod
    def fetch_stock_data(cls,symbol,dateseries):
        data=[]
        if dateseries == "intraday":
            data = gather_stockinfo.fetch_intraday_tikders(symbol)
        elif dateseries == "daily":
            data = gather_stockinfo.fetch_dailytime_tikders(symbol)
        elif dateseries == "weekly":
            data = gather_stockinfo.fetch_weekly_tikders(symbol)
        elif dateseries == "monthly":
            data = gather_stockinfo.fetch_monthly_tikders(symbol)
        
        return data

    #インデックス削除とdataframe型→リスト化
    @classmethod
    def cleansing_stock_data(cls,data):
        tmpdata = data.reset_index()
        tmpdata = tmpdata.reset_index(drop=True)
        tmpdata = tmpdata.values.tolist()        
        return tmpdata

    #日毎
    #3ヶ月前までを対象にする
    @classmethod
    def fetch_dailytime_tikders(cls,symbol):    
        beforeday = datetime(cls.today.year, cls.today.month - 3, 1)
        data = web.DataReader(symbol, "av-daily-adjusted", beforeday,cls.endday,api_key='H6EQKKOI0UPG6OSV')
        return data

    #週毎
    #現在より10年前までを対象にする
    @classmethod
    def fetch_weekly_tikders(cls,symbol):
        beforeday = datetime(cls.today.year -10, cls.today.month , 1)
        data=[]
        data = web.DataReader(symbol, "av-weekly-adjusted", beforeday,cls.endday,api_key='H6EQKKOI0UPG6OSV')
        return data
    #月毎`
    @classmethod
    def fetch_monthly_tikders(cls,symbol):
        data = web.DataReader(symbol, "av-monthly-adjusted", cls.startday,cls.endday,api_key='H6EQKKOI0UPG6OSV')
        return data
    #当日
    @classmethod
    def fetch_intraday_tikders(cls,symbol):
        data = web.DataReader(symbol, "av-intraday",api_key='H6EQKKOI0UPG6OSV')
        return data


#test=web.DataReader("AAPL", "av-intraday", api_key='H6EQKKOI0UPG6OSV')
#av-weekly-adjusted
#av-monthly-adjusted
#tmp=gather_stockinfo.fetch_symbols('QQQ')
#tmp=gather_stockinfo.fetch_weekly_tikders('QQQ')




#tmp=gather_stockinfo.fetch_dailytime_tikders('QQQ')
#tmp.to_csv('test.csv')
#print(tmp.sort_index(axis=0, ascending=False))
#tmp2=tmp.reset_index()
#print(type(tmp))
#print(tmp)
#print(tmp.head().to_string(header=False))



