from rest_framework import serializers

from users.models import Location, User


class UserListSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    total_ads = serializers.SerializerMethodField()  # переопределится в методе ниже

    @staticmethod
    def get_total_ads(user):  # имя аргумента может быть любым
        return user.ad_set.filter(is_published=True).count()

    class Meta:
        model = User
        exclude = ['password']


class UserRetrieveSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    locations = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.pop('locations')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        from django.contrib.auth.hashers import make_password
        user.password = make_password(user.password)

        for i in self._locations:
            location_obj, _ = Location.objects.get_or_create(
                name=i,
            )
            user.locations.add(location_obj)
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.pop('locations')
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()

        for i in self._locations:
            location_obj, _ = Location.objects.get_or_create(
                name=i,
            )
            user.locations.add(location_obj)
        user.save()
        return user


class UserDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
