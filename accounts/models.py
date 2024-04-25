from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, name=None, phone=None):
        if not email or len(email) <= 0:
            raise ValueError("Email field is required !")
        if not password:
            raise ValueError("Password is must !")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone=phone
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, name=None, phone=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            name=name,
            phone=phone
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser):
    class Types(models.TextChoices):
        SELLER = "SELLER", "seller"
        CONSUMER = "CONSUMER", "seller"

    type = models.CharField(max_length=9, choices=Types.choices,
                            # Default is user is teacher
                            default=Types.CONSUMER)
    email = models.EmailField(max_length=200, unique=True)
    name = models.CharField(max_length=50, default="abcd")
    phone = models.CharField(max_length=10, default="1234567890")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # special permission which define that
    # the new user is teacher or student
    is_seller = models.BooleanField(default=False)
    is_consumer = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name","phone"]

    # defining the manager for the UserAccount model
    objects = UserAccountManager()

    def __str__(self):
        return str(self.email)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        if not self.type or self.type == None:
            self.type = UserAccount.Types.CONSUMER
        return super().save(*args, **kwargs)


class SellerManager(models.Manager):
    def create_user(self, email, password=None, name=None, phone=None):
        if not email or len(email) <= 0:
            raise ValueError("Email field is required !")
        if not password:
            raise ValueError("Password is must !")
        email = email.lower()
        user = self.model(
            email=email,
            name=name,
            phone=phone
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(type=UserAccount.Types.SELLER)
        return queryset


class Seller(UserAccount):
    class Meta:
        proxy = True

    objects = SellerManager()

    def save(self, *args, **kwargs):
        self.type = UserAccount.Types.SELLER
        self.is_seller = True
        return super().save(*args, **kwargs)


class ConsumerManager(models.Manager):
    def create_user(self, email, password=None, name=None, phone=None):
        if not email or len(email) <= 0:
            raise ValueError("Email field is required !")
        if not password:
            raise ValueError("Password is must !")
        email = email.lower()
        user = self.model(
            email=email,
            name=name,
            phone=phone
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(type=UserAccount.Types.CONSUMER)
        return queryset


class Consumer(UserAccount):
    class Meta:
        proxy = True

    objects = ConsumerManager()

    def save(self, *args, **kwargs):
        self.type = UserAccount.Types.CONSUMER
        self.is_consumer = True
        return super().save(*args, **kwargs)

