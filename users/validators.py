from datetime import date
from typing import List, Union

from dateutil.relativedelta import relativedelta
from rest_framework.exceptions import ValidationError


class DateBirthdayValidator:
    def __init__(self, min_age: int):
        self.min_age = min_age

    def __call__(self, value: date):
        # value = (date.today() - value).days // 365
        value = relativedelta(date.today(), value).years  # проверка на возраст
        if value < self.min_age:  # если возраст меньше требуемого
            raise ValidationError(f'must be over {self.min_age} years old')


class EmailValidator:
    def __init__(self, unaccept_domain: Union[List, str]):
        if not isinstance(unaccept_domain, list):
            unaccept_domain = [unaccept_domain]
        self.unaccept_domain = unaccept_domain

    def __call__(self, value: str):
        value = value.split('@')
        for i in value:
            if i in self.unaccept_domain:
                raise ValidationError(f"{value[1]} unacceptable domain")
