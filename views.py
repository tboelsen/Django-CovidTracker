from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "your key",
    'x-rapidapi-host': "your host"
    }

response = requests.request("GET", url, headers=headers).json()


def CovidView(request):
	#create a list with all countries and regions
	count = int(response['results'])
	countries = []
	for i in range(0, count):
		countries.append(response['response'][i]['country'])
	countries = sorted(countries)

	#this is for the default data that are being displayed when first opening the site
	country = 'All'
	for k in range(0, count):
		if response['response'][k]['country'] == country:
			new = response['response'][k]['cases']['new']
			active = response['response'][k]['cases']['active']
			recovered = response['response'][k]['cases']['recovered']
			critical = response['response'][k]['cases']['critical']
			total = response['response'][k]['cases']['total']
			death = int(total) - int(active) - int(recovered)

	#update data once the user selects a new country/region
	if request.method == 'POST':
		country = request.POST['country']
		for j in range(0, count):
			if country == response['response'][j]['country']:
				new = response['response'][j]['cases']['new']
				active = response['response'][j]['cases']['active']
				recovered = response['response'][j]['cases']['recovered']
				critical = response['response'][j]['cases']['critical']
				total = response['response'][j]['cases']['total']
				death = int(total) - int(active) - int(recovered)
		context = {'country': country, 'countries': countries, 'new': new, 'active': active, 'recovered': recovered, 'critical': critical, 'death': death, 'total': total}
		return render(request, 'index.html', context)

	#initial return when first opening the site
	context = {'country': country, 'countries': countries, 'new': new, 'active': active, 'recovered': recovered, 'critical': critical, 'death': death, 'total': total}
	return render(request, 'index.html', context)
