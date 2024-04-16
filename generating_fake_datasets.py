from faker import Faker 
import pandas as pd

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    for _ in range(num_records):
        record = {
            'name': fake.name(),
            'address': fake.address(),
            'email': fake.email(),
            'phone_number': fake.phone_number(),
            'birthdate': fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d'),
            'blood_type': fake.random_element(elements=('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')),
            'gender': fake.random_element(elements=('Male', 'Female')),
        }
        data.append(record)
    return data

def save_data_to_csv(data, filename):
    import csv
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for record in data:
            writer.writerow(record)

if __name__ == "__main__":
    num_records = 10000
    fake_data = generate_fake_data(num_records)

    csv_filename = "fake_data.csv"
    save_data_to_csv(fake_data, csv_filename)


