from django.db import models


class Image(models.Model):
    file = models.ImageField(upload_to='media/product_detail_images')


class Banner(models.Model):
    title = models.CharField(
        max_length=100
    )
    image = models.ImageField(
        upload_to='media/banner_images'
    )
    description = models.CharField(
        max_length=99
    )
    is_first = models.BooleanField()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(
        max_length=150
    )
    logo = models.ImageField(
        upload_to='media/brand_logos'
    )

    def __str__(self):
        return self.title


class Product(models.Model):
    brand = models.ManyToManyField(
        'Brand'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=150
    )
    description = models.TextField()
    photo = models.ImageField(
        upload_to='media/product_photos'
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00
    )
    discount_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        blank=True,
        null=True
    )
    size = models.PositiveSmallIntegerField(
        choices=(
            (1, 'S'),
            (2, 'M'),
            (3, 'L'),
            (4, 'XL'),
        )
    )
    is_active = models.BooleanField(
        default=True
    )
    images = models.ManyToManyField(Image)
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    updated_date = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title
