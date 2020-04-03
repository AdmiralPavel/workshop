from django.db import models


class Master(models.Model):
    class Meta:
        db_table = 'masters'

    id = models.AutoField(db_column='id', primary_key=True, auto_created=True)
    name = models.CharField(max_length=255, db_column='name')
    description = models.CharField(max_length=255, db_column='description')
    rating = models.IntegerField(db_column='rating')
    photo = models.CharField(max_length=255, db_column='photo')

    def __str__(self):
        return self.name


class Service(models.Model):
    class Meta:
        db_table = 'services'

    id = models.AutoField(db_column='id', primary_key=True)
    name = models.CharField(max_length=255, db_column='name')
    description = models.CharField(max_length=255, db_column='description')
    photo = models.CharField(max_length=255, db_column='photo')
    price = models.IntegerField(db_column='price')
    masters = models.ManyToManyField(Master)

    def __str__(self):
        return self.name


class Review(models.Model):
    class Meta:
        db_table = 'reviews'

    id = models.AutoField(db_column='id', primary_key=True)
    text = models.CharField(max_length=255, db_column='text')
    rating = models.IntegerField(db_column='rating')
    date = models.TimeField(db_column='date')
    user = models.ForeignKey('User', related_name='reviews', on_delete=models.CASCADE)


class User(models.Model):
    class Meta:
        db_table = 'users'

    id = models.AutoField(db_column='id', primary_key=True)


class Session(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField()
    master = models.ForeignKey(Master, on_delete=models.CASCADE)

