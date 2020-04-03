from rest_framework import serializers

from barbershop_server.models import Master, Service, Session, Review


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('id', 'time', 'master',)

    def create(self, validated_data):
        return Session.objects.create(**validated_data)


class MasterSerializer(serializers.ModelSerializer):
    sessions = SessionSerializer(source='session_set', many=True)

    class Meta:
        model = Master
        fields = ('name', 'description', 'id', 'rating', 'photo', 'sessions')

    def create(self, validated_data):
        return Master.objects.create(**validated_data)


class ServiceSerializer(serializers.ModelSerializer):
    masters = serializers.ListSerializer(child=MasterSerializer())

    class Meta:
        model = Service
        fields = ('name', 'description', 'id', 'price', 'photo', 'masters',)

    def create(self, validated_data):
        return Service.objects.create(**validated_data)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'text', 'rating', 'date', 'user',)

    def create(self, validated_data):
        return Master.objects.create(**validated_data)
