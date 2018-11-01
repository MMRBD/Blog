from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    details = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    # add more...

    def __str__(self):
        return self.title
# python manage.py migrate
# python manage.py makemigrations
# python manage.py migrate
