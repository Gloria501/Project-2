import unittest
from unittest.mock import patch
import pandas as pd

# Import your functions
from person1_api_fetch import fetch_employee_data
from normalization import normalize_data
from postprocessing import enforce_data_types, show_data


class TestEmployeeProject(unittest.TestCase):

    # ------------------ fetch_data.py Tests ------------------

   @patch('requests.get')
   def test_fetch_valid_json_list(self, mock_get):
    mock_get.return_value.json.return_value = [{'first_name': 'John', 'last_name': 'Doe'}]
    mock_get.return_value.status_code = 200
    result = fetch_employee_data('http://fakeapi.com')
    self.assertIsInstance(result, list)

    @patch('requests.get')
    def test_fetch_with_employees_key(self, mock_get):
        mock_get.return_value.json.return_value = {'employees': [{'first_name': 'Jane'}]}
        mock_get.return_value.status_code = 200
        result = fetch_employee_data('http://fakeapi.com')
        self.assertEqual(result[0]['first_name'], 'Jane')

    @patch('requests.get')
    def test_fetch_error_handling(self, mock_get):
        mock_get.side_effect = Exception("Connection failed")
        with self.assertRaises(Exception):  # or your custom exception
            fetch_employee_data("http://fakeapi.com")


    # ------------------ normalize_data.py Tests ------------------

    def setUp(self):
        self.sample_data = [{
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'gender': 'Male',
            'age': 30,
            'job_title': 'Developer',
            'years_of_experience': 4,
            'salary': 50000,
            'department': 'IT',
            'phone': '1234567890'
        }]

    def test_full_name_combined(self):
        df = normalize_data(self.sample_data)
        self.assertEqual(df.loc[0, 'Full Name'], 'John Doe')

    def test_designation_assigned(self):
        df = normalize_data(self.sample_data)
        self.assertEqual(df.loc[0, 'designation'], 'Data Engineer')

    def test_hire_date_handled(self):
        df = normalize_data(self.sample_data)
        self.assertIn('hire_date', df.columns)

    def test_invalid_phone_detection(self):
        self.sample_data[0]['phone'] = '123x456'
        df = normalize_data(self.sample_data)
        self.assertEqual(df.loc[0, 'phone'], 'Invalid Number')

    # ------------------ export_and_test.py Tests ------------------

    def test_export_and_read(self):
        df = normalize_data(self.sample_data)
        enforce_data_types(df, 'test_output.csv')  
        read_back = pd.read_csv('test_output.csv')
        self.assertIn('Full Name', read_back.columns)

    def test_validate_data_no_errors(self):
        df = normalize_data(self.sample_data)
        errors =  show_data(df)
        self.assertEqual(errors, [])


if __name__ == '__main__':
    unittest.main()
