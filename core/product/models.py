from django.db import models


class Image(models.Model):
    file = models.ImageField(upload_to='media/files')


class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Cap(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    photo = models.ImageField(upload_to='media/photos')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    images = models.ManyToManyField(Image)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
