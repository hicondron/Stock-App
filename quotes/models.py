from django.db import models

class Stock(models.Model):
    ticker = models.CharField(max_length=10)
    
    def _str_(self):
        return self.ticker
