from rest_framework import serializers


def check_is(value):
    if value:
        raise serializers.ValidationError(f'{value} not allowed')
