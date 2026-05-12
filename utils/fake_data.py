from faker import Faker

fake = Faker("en_CA")


def generate_customer():

    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone": fake.phone_number()
    }