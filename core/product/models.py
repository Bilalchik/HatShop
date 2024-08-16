from django.db import models


class Banner(models.Model):
    title = models.CharField(
        max_length=123
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
    title = models.CharField(
         max_length=123
    )

    def __str__(self):
        return self.title


class Image(models.Model):
    file = models.ImageField(
        upload_to='media/products_detail_images'
    )


class Product(models.Model):
    brands = models.ManyToManyField(
        'Brand'
    )
    title = models.CharField(
        max_length=123
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    description = models.TextField()
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
    logo = models.ImageField(
        upload_to='media/product_logos'
    )
    images = models.ManyToManyField(
        Image
    )
    is_active = models.BooleanField(
        default=True
    )
    size = models.PositiveSmallIntegerField(
        choices=(
            (1, 'S'),
            (2, 'M'),
            (3, 'L'),
            (4, 'XL'),
        )
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(
        max_length=123
    )
    logo = models.ImageField(
        upload_to='media/brand_logos'
    )

    def __str__(self):
        return self.title



