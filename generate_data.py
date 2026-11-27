
import json

# FICTIONAL SAMPLE DATA ONLY
# These borrower records are created for demonstration and educational purposes.
# They do not represent real people or actual loan applications.

borrowers = [
    {
        "id": 1,
        "data_type": "fictional_sample",
        "name": "Uzair Khan",
        "email": "ali@example.com",
        "city": "Islamabad",
        "loan_amount": 50000,
        "loan_status": "Pending"
    },
    {
        "id": 2,
        "data_type": "fictional_sample",
        "name": "Ahmed Raza",
        "email": "ahmed@example.com",
        "city": "Rawalpindi",
        "loan_amount": 75000,
        "loan_status": "Approved"
    },
    {
        "id": 3,
        "data_type": "fictional_sample",
        "name": "Usman Tariq",
        "email": "usman@example.com",
        "city": "Lahore",
        "loan_amount": 30000,
        "loan_status": "Pending"
    }
]

with open("borrowers.json", "w", encoding="utf-8") as file:
    json.dump(borrowers, file, indent=4)

print("Fictional sample borrower data generated successfully!")
