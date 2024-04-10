import random


class BurgersTestData:
    AUTH_NAME = 'Vera'
    AUTH_EMAIL = 'verakuzmina7111@yandex.ru'
    AUTH_PASSWORD = '123456'
    AUTH_RANDOM_EMAIL = f'verakuzmina7{random.randint(100, 999)}@yandex.ru'
    AUTH_PASSWORD_NEGATIVE = '12345'
