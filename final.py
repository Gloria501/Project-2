from person1_api_fetch import fetch_employee_data
from normalization import normalize_data
from postprocessing import enforce_data_types, show_data

url = "https://api.slingacademy.com/v1/sample-data/files/employees.json"
raw_df = fetch_employee_data(url)

if raw_df:
    normalized_df = normalize_data(raw_df)
    final_df = enforce_data_types(normalized_df)
    show_data(final_df)
else:
    print("No employee data to process.")