from django.conf import settings
from django.shortcuts import render
from django.views import View

# Import json to load JSON Data to Python Dictionary 
import json

# To make a request to API
import urllib.request

# Create your views here.

class IndexView(View):
    template_name = 'converter/index.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        amount = float(request.POST['amount'])
        from_currency = request.POST['from_currency']
        to_currency = request.POST['to_currency']
        print("Convert " + str(amount) + " " + from_currency + " to " + to_currency)

        try:
            # Get your API Key from ExchangeRate-API
            # https://www.exchangerate-api.com/

            # Get JSON data from API
            api_url = str('https://v6.exchangerate-api.com/v6/'+settings.CURRENCY_API_KEY+'/pair/'+ from_currency +'/'+ to_currency +'')
            source_data = urllib.request.urlopen(api_url).read()
            
            # Convert JSON Data to a Python Dictionary
            list_of_data = json.loads(source_data)

            # Get Conversion Rate
            conversion_rate = float(list_of_data['conversion_rate'])

            # Calculate the amount with conversion rate
            conversion_amount = round(amount * conversion_rate, 4)
            
            # Get required currency conversion data
            converter_data = {
                'amount': amount,
                'conversion_amount':conversion_amount,
                'from_currency':from_currency,
                'to_currency':to_currency,
                'from_country_flag_code':from_currency[:-1],
                'to_country_flag_code':to_currency[:-1],
            }
            context = {
                'converter_data': converter_data,
            }
        except:
            # Error in conversion calculation
            print("Error found")

            converter_data = {
                'error': 'Conversion Error..!!!',
            }

            context = {
                'converter_data': converter_data,
            }

        return render(request, self.template_name, context)