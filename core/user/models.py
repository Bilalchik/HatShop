from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, phone_number, username, password=None):

        user = self.model(
            phone_number=phone_number,
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, username, password=None):
        user = self.create_user(
            phone_number=phone_number,
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(
        max_length=100
    )
    phone_number = models.CharField(
        max_length=20,
        unique=True
    )
    email = models.EmailField(
        blank=True,
        null=True
    )
    cover = models.ImageField(
        upload_to='media/user_covers',
        blank=True,
        null=True
    )
    address = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )
    status = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Обычныйй пользователь'),
            (2, 'Менеджер'),
            (3, 'Бугхалтер')
        ),
        default=1,
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    updated_date = models.DateTimeField(
        auto_now=True
    )
    is_admin = models.BooleanField(
        default=False
    )

    objects = MyUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

