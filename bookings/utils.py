from django.utils.crypto import get_random_string

# generates random unique alphanumeric strings


def generate_number(length):
    return get_random_string(length=length)


def generate_booking_number():
    return f'BRT-{generate_number(12)}'
