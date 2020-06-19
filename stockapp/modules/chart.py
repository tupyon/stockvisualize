import plotly.graph_objects as go
from . import gatherstockinfo
import pandas as pd
from datetime import datetime
from plotly.offline import plot

class display_chart():

    @classmethod
    def stock_chandlestick(cls,symbol):
        plotdata = gatherstockinfo.gather_stockinfo.fetch_stock_data(symbol,"daily")
        #plotdata = gather_stockinfo.fetch_stock_data(symbol,"daily")
        plotdata = plotdata.reset_index()
        plotdata = plotdata.reset_index(drop=True)
        fig = go.Figure(data=[go.Candlestick(x=plotdata['index'],open=plotdata['open'],high=plotdata['high'],low=plotdata['low'],close=plotdata['close'])])
        plot_fig = plot(fig, output_type='div', include_plotlyjs=False,auto_open=True)
        return plot_fig




# tmp=display_chart.stock_chandlestick('TECL')
# tmp.show()