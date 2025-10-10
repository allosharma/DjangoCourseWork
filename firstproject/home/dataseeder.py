from home.models import student2
from faker import Faker
import random

fake = Faker('en_IN')

def seed_fake_data(n):
    for _ in range(n):
        name = fake.name()
        age = random.randint(18, 30)
        email = fake.unique.email()
        mobile_number = fake.phone_number()
        DOB = fake.date_of_birth(tzinfo=None, minimum_age=16, maximum_age=30)

        student_instance = student2(
            name=name,
            age=age,
            email=email,
            mobile_number=mobile_number,
            DOB=DOB
        )
        student_instance.save()
    print(f"Successfully seeded {n} fake student records.")

# Example usage: seed_fake_data(10)from home.models import student2
seed_fake_data(5000) 