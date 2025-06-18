import requests

def fetch_employee_data(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        # Return directly if the data is a list
        if isinstance(data, list):
            return data
        print(" Unexpected data format. Expected a list of employees.")
        return []
    except requests.exceptions.RequestException as e:
        print(f" Error fetching data: {e}")
        return []
