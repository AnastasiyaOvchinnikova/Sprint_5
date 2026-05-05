import random
import string

def generate_email():
    """Генерирует уникальный email"""
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{random_string}@test.ru"
