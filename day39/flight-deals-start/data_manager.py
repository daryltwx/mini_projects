import requests


USERNAME = "Your Username here"
PASSWORD = "Your Password here"

AUTH_HEADER = "Your AUth here"

username = "Your Username here"
projectName = "flightPrices"
sheetName = "sheet1"

sheets_endpoint = f"https://api.sheety.co/{username}/{projectName}/{sheetName}"

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        # Get data from google sheet using API GET
        pass


# Return city IATA, code and lowest prices
# data_manager_instance = DataManager()
# print(data_manager_instance.data)

    def read_sheet(self):
        response = requests.get(url=sheets_endpoint, auth=(USERNAME, PASSWORD))
        data = response.json()["sheet1"]
        return data


    def write_sheet(self, city: str, lowest_price: int):
        sheet_input = {
            "sheet1": {
                "city": city,
                "iataCode": "none",
                "lowestPrice": lowest_price,
            }
        }
        sheet_response = requests.post(url=sheets_endpoint, json=sheet_input, auth=(USERNAME, PASSWORD))

        print(sheet_response.text)

# Test successful
print(DataManager().write_sheet(city="Tokyo", lowest_price=5))