# from django.db import models
#
#
# class Person(models.Model):
#     name = models.CharField(max_length=50)
#     age = models.IntegerField()


# New
# from django.db import models
#
#
# class Nugget(models.Model):
#     content = models.TextField()
#
#     def __str__(self):
#         return self.content

# New3
# from django.db import models
#
#
# class Nugget(models.Model):
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.content

# last
from django.db import models

# from django.db import models
#
#
# class Nugget(models.Model):
#     name = models.CharField(max_length=255)
#     type = models.CharField(max_length=255)
#     datatype = models.CharField(max_length=255)
#     description = models.TextField()
#     tags = models.ManyToManyField('Tag')
#
#     def __str__(self):
#         return self.name
#
#
# class Tag(models.Model):
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name

from django.db import models


class Nugget(models.Model):
    # id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    datatype = models.CharField(max_length=50)
    description = models.TextField()
    tags = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
