def enforce_data_types(df):
    df = df.astype({
        'Full Name': str,
        'email': str,
        'gender': str,
        'age': 'Int64',
        'job_title': str,
        'years_of_experience': 'Int64',
        'salary': 'Int64',
        'department': str
    })
    return df

def show_data(df):
    print(df)
