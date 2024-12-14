import requests
import json

def fetch_gus_data(url):
    """Fetches data from the Statistics Poland (GUS) API.

    Args:
        url: The API URL.

    Returns:
        dict or None: Data in JSON format as a Python dictionary, or None on error.
        Also prints the HTTP status code.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception for HTTP 4xx or 5xx status codes
        print(f"HTTP Status Code: {response.status_code}") #Prints the status code
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        if response is not None:
          print(f"Server Response Content: {response.text}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON Decoding Error: {e}")
        if response is not None:
          print(f"Server Response Content: {response.text}")
        return None

# Example usage for the list of indicators:
indicators_url = "https://api-sdp.stat.gov.pl/api/1.0.0/indicators/indicator-indicator?lang=en"
indicators_data = fetch_gus_data(indicators_url)

if indicators_data:
    # Processing indicators data
    # For example, displaying indicator names:
    for indicator in indicators_data:
        print(f"Indicator ID:{indicator['id-wskaznik']} Name: {indicator['nazwa']}")

# Example usage for specific indicator data (requires its ID):
# First, you need to retrieve the list of indicators and find the ID of the one you need.
# This example uses ID '1' (Consumer price index)
indicator_data_url = "https://api-sdp.stat.gov.pl/api/1.0.0/indicators/indicator-data-indicator?id-wskaznik=639&id-rok=2023&lang=pl"
specific_indicator_data = fetch_gus_data(indicator_data_url)

if specific_indicator_data:
    # Processing detailed data
    print("\n--- Specific Indicator Data ---")
    # Displaying the first few records as an example:
    for i in specific_indicator_data:
        print(i)