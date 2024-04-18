import random
import string


class UserDataGenerator:

    @staticmethod
    def email_generator():
        letters = (''.join(random.choices(string.ascii_lowercase, k=10)))
        num = random.randint(000, 999)
        return f'{letters}7{num}@yandex.ru'

    @staticmethod
    def password_generator():
        auth_password = str(random.randint(000000, 999999))
        return auth_password
