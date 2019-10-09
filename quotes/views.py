
from django.shortcuts import render
from .models import Stock

def home(request):
	import requests 
	import json 

	if request.method == 'POST':
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_52ea6173dbb24a05a1a9b25eb6e52c41")

		try:
				api = json.loads(api_request.content)
		except Exception as e:
				api = "Error..."
		return render(request, 'home.html', {'api': api})

	else:
			return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..."})       
            
def about(request):
        return render(request, 'about.html', {})

def add_stock(request):

		ticker = Stock.objects.all()
		output = []
		
		return render(request, 'add_stock.html',{"ticker": ticker})
