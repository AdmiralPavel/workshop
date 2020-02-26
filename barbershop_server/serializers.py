from rest_framework import serializers

from barbershop_server.models import Master


class MasterSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    id = serializers.IntegerField()
    rating = serializers.IntegerField()
    photo = serializers.CharField(max_length=255)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.id = validated_data.get('id', instance.id)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.photo = validated_data.get('photo', instance.photo)

        instance.save()
        return instance

    def create(self, validated_data):
        return Master.objects.create(**validated_data)


class ServiceSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    id = serializers.IntegerField()
    price = serializers.IntegerField()
    photo = serializers.CharField(max_length=255)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('title', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.id = validated_data.get('id', instance.id)
        instance.price = validated_data.get('price', instance.rating)
        instance.photo = validated_data.get('photo', instance.photo)

        instance.save()
        return instance

    def create(self, validated_data):
        return Master.objects.create(**validated_data)