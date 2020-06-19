from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
# Create your models here.
class Closeprices(models.Model):
    symbol = models.CharField(max_length=10, blank=False, null=False)
    stockdate = models.DateField(blank=True, null=True)
    price = models.DecimalField(
        max_digits=13, 
        decimal_places=4, 
        blank=False, 
        null=True,
        validators=[MinValueValidator(0.0000), MaxValueValidator(99999.9999)]
        )
    # price = models.TextField()
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)

    class Meta:
        managed = False
        db_table = 'closeprices'

    def __str__(self):
        return f"{self.symbol}, {self.stockdate}, {self.price},{self.id}"


class Symbollist(models.Model):
    tiker = models.CharField(primary_key=True,max_length=10, blank=True, null=False)
    companyname = models.CharField(max_length=1000, blank=True, null=True)
    etf = models.BooleanField(blank=True, null=True)
    financial_status = models.CharField(max_length=10, blank=True, null=True)
    nasdaq_symbol = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'symbollist'

    def __str__(self):
        return self.tiker



# class Symbollist(models.Model):
#     tiker= models.CharField(primary_key=True,max_length=10,blank=False,null=False)
#     companyname= models.TextField()
#     etf =models.BooleanField()
#     financial_status = models.CharField(max_length=20)
#     nasdaq_symbol = models.CharField(max_length=10,blank=True,null=True)

#     class Meta:
#         managed = False
#         db_table = 'symbollist'

#     def __str__(self):
#         return self.tiker

