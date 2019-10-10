from django.shortcuts import render, redirect
from .models import Stock
from .forms Stockform
from django.contrib import messages


def home(request):
	import requests 
	import json 

	if request.method == 'POST':
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_062031d20883444f9ea74e2610fe2011")

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
	if request.method == 'POST':
		form = Stockform(request.POST or None)

		if form.isvalid():
			form.save()
			message.success(request, ("Stock has been added"))
			return redirect('add_stock')
	else:
		ticker = Stock.objects.all()
		output = []
		return render(request, 'add_stock.html', {'ticker': ticker})
