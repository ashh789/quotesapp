from django.db import models
from django.core.urlresolvers import reverse

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=50)

    class Meta:
        ordering=["name"]
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("quotepage",kwargs={"slug":self.slug})


class Person(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    tag = models.ForeignKey(Tag)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("personquotes",kwargs={"slug":self.slug})


class Quote(models.Model):
    text=models.TextField(max_length=500)
    person=models.ForeignKey(Person)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.text









