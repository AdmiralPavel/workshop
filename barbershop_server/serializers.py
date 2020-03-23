from rest_framework import serializers

from barbershop_server.models import Master, Service, Session


class SessionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    time = serializers.DateTimeField()

    def create(self, validated_data):
        return Session.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.time = validated_data.get('time', instance.time)


class MasterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    id = serializers.IntegerField()
    rating = serializers.IntegerField()
    photo = serializers.CharField(max_length=255)
    #sessions = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = Master
        fields = ('name', 'description', 'id', 'rating', 'photo', )

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
    masters = MasterSerializer(many=True)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('title', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.id = validated_data.get('id', instance.id)
        instance.price = validated_data.get('price', instance.price)
        instance.photo = validated_data.get('photo', instance.photo)

        instance.save()
        return instance

    def create(self, validated_data):
        return Service.objects.create(**validated_data)


class ReviewSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=255)
    text = serializers.CharField(max_length=255)
    id = serializers.IntegerField()
    rating = serializers.IntegerField()
    date = serializers.DateField()

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.text = validated_data.get('text', instance.text)
        instance.id = validated_data.get('id', instance.id)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.date = validated_data.get('date', instance.date)

        instance.save()
        return instance

    def create(self, validated_data):
        return Master.objects.create(**validated_data)
