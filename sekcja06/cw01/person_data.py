from faker import Faker


def get_random_person():
    generator = Faker()
    return {
        'pid': None,
        'fname': generator.first_name(),
        'lname': generator.last_name(),
        'age': generator.random_int(1, 100)
    }
