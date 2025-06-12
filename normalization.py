import pandas as pd

def normalize_data(employees):
    print("normalize_data loaded")

    df = pd.DataFrame(employees)

    # Combine first and last name
    df['Full Name'] = df['first_name'] + ' ' + df['last_name']

    # Handle phone numbers
    df['phone'] = df['phone'].apply(lambda x: "Invalid Number" if 'x' in str(x) else x)

    # Assign designation based on experience
    def get_designation(exp):
        if exp < 3:
            return 'System Engineer'
        elif 3 <= exp <= 5:
            return 'Data Engineer'
        elif 5 < exp <= 10:
            return 'Senior Data Engineer'
        else:
            return 'Lead'

    df['designation'] = df['years_of_experience'].apply(get_designation)

    # Safely handle 'hire_date'
    if 'hire_date' in df.columns:
        df['hire_date'] = pd.to_datetime(df['hire_date'], errors='coerce').dt.strftime('%Y-%m-%d')
    else:
        print("'hire_date' field not found in data. Adding 'hire_date' as NaT.")
        df['hire_date'] = pd.NaT

    # Convert valid phone numbers to int
    def convert_phone(phone):
        try:
            return int(phone)
        except:
            return phone

    df['phone'] = df['phone'].apply(convert_phone)

    # Type conversion
    df = df.astype({
        'Full Name': str,
        'email': str,
        'gender': str,
        'age': int,
        'job_title': str,
        'years_of_experience': int,
        'salary': int,
        'department': str
    })

    return df
