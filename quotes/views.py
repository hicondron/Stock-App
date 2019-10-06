from django.shortcuts import render

# Create your views here.

def home(request):

    import requests
    import json

    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_52ea6173dbb24a05a1a9b25eb6e52c41")

    try: 
        api = json.loads(api_request.content)

    except Exception as e:
        api = "Error ...."
        
    return render(request, 'home.html', {'api':api})
    # pk_52ea6173dbb24a05a1a9b25eb6e52c41

def about(request):
    return render(request, 'about.html', {})
