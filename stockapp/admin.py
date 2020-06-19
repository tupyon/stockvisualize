# Register your models here.
from django.contrib import admin
from .models import Closeprices ,Symbollist # models.pyで指定したクラス名

admin.site.register(Closeprices) # models.pyで指定したクラス名
admin.site.register(Symbollist) # models.pyで指定したクラス名
