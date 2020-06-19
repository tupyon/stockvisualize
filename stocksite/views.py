from django.shortcuts import render, redirect, reverse  
from django.views import View  

class index(View):
    def get(self, request, *args, **kwargs):
        return redirect(reverse('stockapp:top_page'))


def quotedisplay(request):
    return render(request, 'stockapp:tickerdisplay')

def tickerserach(request):
    return render(request, 'stockapp:tickerserach')
#    return redirect(reverse('stockapp:tickerserach'))



index = index.as_view()