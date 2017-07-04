from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return "{}".format(self.name)


class Movie(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    director = models.ForeignKey(Person, related_name='directors')
    actors = models.ManyToManyField(Person, through='RoleInfo')
    year = models.IntegerField()

    def __str__(self):
        return "{} ({})".format(self.title, self.year)


class RoleInfo(models.Model):
    role = models.CharField(max_length=24)
    movie = models.ForeignKey(Movie)
    person = models.ForeignKey(Person)

    def __str__(self):
        return "{}".format(self.role)
