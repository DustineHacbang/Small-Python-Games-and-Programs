medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'P1002',
        'age': 45,
        'gender': 'Male',
        'diagnosis': 'Diabetes',
        'medications': ['Metformin'],
        'last_visit_id': 'V2302',
    },
    {
        'patient_id': 'P1003',
        'age': 56,
        'gender': 'Female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'V2303',
    },
    {
        'patient_id': 'P1004',
        'age': 67,
        'gender': 'Male',
        'diagnosis': 'Heart Disease',
        'medications': ['Aspirin'],
        'last_visit_id': 'V2304',
    },
    ]

def validate(data):
    is_sequence = isinstance(data, (list, tuple))
    if not is_sequence :
        print('Invalid format: expected a list or tuple.')
        return False