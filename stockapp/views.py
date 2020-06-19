# from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the stockapp index.")
from django.shortcuts import render  
from django.views import View  
from .models import Closeprices
from stockapp.modules import  calstockprice,outputresult,gatherstockinfo,chart
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

class SampleView(View):  
    # def get(self, request, *args, **kwargs):  
    #     return render(request, 'stockapp/top_page.html')
    def get(self, request, *args, **kwargs):  
        #input_data = request.POST['input_data']
        #dateresult=[]
        #stocklist=[]
        upsidelist=[]
        donwsidelist=[]
        upsidelist = calstockprice.stock_calculate.calculate_upside_ratio()
        donwsidelist = calstockprice.stock_calculate.calculate_downside_ratio()
#        dateresult=Closeprices.objects.values('stockdate').distinct().order_by('stockdate').reverse()[:1]
#        dateresult=Closeprices.objects.filter('stockdate').distinct('stockdate').order_by('stockdate').reverse()[0]
#        Closeprices.objects
#        for row in dateresult:
#            stocklist=Closeprices.objects.defer('id').fileter(stockdate=row['stockdate']).order_by('symbol')
#        stocklist=Closeprices.objects.filter(stockdate=dateresult).order_by('symbol')
        params = {
            'upsidelist':upsidelist,
            'downsidelist':donwsidelist,
        }
#        print(stocklist)
#        context={'result_sample1':result_sample1, 'result_sample2':result_sample2,'result_sample3':result_sample3}
        return render(request, 'stockapp/top_page.html', params)



#class quoteDetail(View,LoginRequiredMixin):
#    #model = Item
def quotedisplay(request):
    symbol=request.GET.get('query')
    detaildata=[]
    tickerbaseinfo = gatherstockinfo.gather_stockinfo.fetch_symbols(symbol)
    # detaildata = gatherstockinfo.gather_stockinfo.fetch_dailytime_tikders(symbol)
    # weeklydata = gatherstockinfo.gather_stockinfo.fetch_weekly_tikders(symbol)
    # monthlydata = gatherstockinfo.gather_stockinfo.fetch_monthly_tikders(symbol)
    # intradata = gatherstockinfo.gather_stockinfo.fetch_intraday_tikders(symbol)
    detaildata = gatherstockinfo.gather_stockinfo.fetch_stock_data(symbol,"daily")
    detaildata = gatherstockinfo.gather_stockinfo.cleansing_stock_data(detaildata)

    weeklydata = gatherstockinfo.gather_stockinfo.fetch_stock_data(symbol,"weekly")
    weeklydata = gatherstockinfo.gather_stockinfo.cleansing_stock_data(weeklydata)

    monthlydata = gatherstockinfo.gather_stockinfo.fetch_stock_data(symbol,"monthly")
    monthlydata = gatherstockinfo.gather_stockinfo.cleansing_stock_data(monthlydata)

    intradata = gatherstockinfo.gather_stockinfo.fetch_stock_data(symbol,"intraday")
    intradata = gatherstockinfo.gather_stockinfo.cleansing_stock_data(intradata)

    plot_candle = chart.display_chart.stock_chandlestick(symbol)

    params = {
        "basicinfo":tickerbaseinfo,
        'detaildata':detaildata,
        'weeklydata':weeklydata,
        'monthlydata':monthlydata,
        'intradata':intradata,
        'plot_candle':plot_candle,
    }
    return render(request, 'stockapp/tickerdisplay.html',params)
#def quoteDetail():

def tickerserach(request):

    #ディクショナリ形式の引数を渡す
#    return render(request, 'ohanky.html',{'mytext1':mytext1,'mytext2':mytext2})
    return render(request, 'stockapp/tickerserach.html')




top_page = SampleView.as_view()



