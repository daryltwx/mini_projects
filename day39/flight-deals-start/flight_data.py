import requests

FLIGHT_API_KEY = "Your API here"


flight_endpoint = "https://api.tequila.kiwi.com/"

flight_params = {
    "apikey": FLIGHT_API_KEY,
    "fly_from": "SIN",
    "fly_to": "ICN/SIN/",
    "date_from": "none",
}

# date_from - in dd/mm/yyyy format
# date_to

# Minimal length of stay in int
# nights_in_dst_from

# one_for_city: 1
# selected_cabins: M

# price_from - minimum price

class FlightData:
    #This class is responsible for structuring the flight data.
    pass

    # Assume this is for API call to get flight data searches
    #flight_response = requests.get(url=f"{flight_endpoint}/v2",  )



    def search_iata_codes(self, term: str):
        iata_code_params = {
            "term": term,
        }

        headers = {
            "apikey": FLIGHT_API_KEY,
        }

        location_response = requests.get(url=f"{flight_endpoint}/locations/query", params=iata_code_params, headers=headers)
        print(location_response.json())
        print(location_response.status_code)


flight_data_instance = FlightData()
flight_data_instance.search_iata_codes(term="SIN")