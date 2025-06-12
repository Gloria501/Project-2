def test_export_and_read(self):
        df = normalize_data(self.sample_data)
        enforce_data_types(df, 'test_output.csv')  
        read_back = pd.read_csv('test_output.csv')
        self.assertIn('Full Name', read_back.columns)

    def test_validate_data_no_errors(self):
        df = normalize_data(self.sample_data)
        errors =  show_data(df)
        self.assertEqual(errors, [])


if _name_ == '_main_':
    unittest.main()