import requests

url = "https://tripadvisor16.p.rapidapi.com/api/v1/flights/searchFlights"

querystring = {"sourceAirportCode":"BOM","destinationAirportCode":"DEL","date":"2024-06-22","itineraryType":"ONE_WAY","sortOrder":"ML_BEST_VALUE","numAdults":"1","numSeniors":"0","classOfService":"ECONOMY","pageNumber":"1","nearby":"yes","nonstop":"yes","currencyCode":"USD","region":"USA"}

headers = {
	"x-rapidapi-key": "e162fd8152msh0cf46da1ab186adp1c7ab1jsn86ae92313f36",
	"x-rapidapi-host": "tripadvisor16.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())