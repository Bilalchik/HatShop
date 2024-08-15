# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
#
# class MyUserManager(BaseUserManager):
#     def create_user(self,phone_number,username,password=None):
#         if not phone_number:
#             raise ValueError('Пользователи должны иметь номер телефона')
#
#         user = self.model(
#             phone_number=phone_number,
#             username=username,
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self,phone_number,username,password=None):
#
#         user = self.create_user(
#             phone_number=phone_number,
#             username=username,
#             password=password
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user
#
# class MyUser(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(
#         'Имя',
#         max_length=123
#     )
#     phone_number = models.CharField(
#         'Номер телефона',
#         max_length=17,
#         unique=True
#     )
#     email = models.EmailField(
#         'Электронная почта',
#         blank=True,
#         null=True
#     )
#     password = models.CharField(
#         'Пароль',
#         max_length=128
#     )
#     cover = models.ImageField(
#         upload_to='cover/',
#         blank=True,
#         null=True
#     )
#     created_date = models.DateTimeField(
#         'Дата создания',
#         auto_now_add=True
#     )
#     updated_date = models.DateTimeField(
#         'Дата обновления',
#         auto_now=True
#     )
#     status = models.PositiveSmallIntegerField(
#         choices=(
#             (1, 'Обычный пользователь'),
#             (2, 'Менеджер')
#         ),
#         default=1,
#         verbose_name='Статус пользователя'
#     )
#     is_admin = models.BooleanField(
#         'Администратор',
#         default=False
#     )
#
#     USERNAME_FIELD = 'phone_number'
#     REQUIRED_FIELDS = ['username']
#
#     objects = MyUserManager()
#
#     def __str__(self):
#         return self.username


