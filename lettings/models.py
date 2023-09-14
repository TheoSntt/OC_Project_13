"""
Defines the models of the lettings app.
"""
from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Defines the Address Model.
    Addresses are linked to the Letting Model through its address OneToOneField field
    """
    class Meta:
        verbose_name_plural = "adresses"
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """
        Address model str method.
        It defines what string is returned when str(<an address object>) is called
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Defines the Letting Model.
    Lettings are linked to the Address Model through their address OneToOneField field
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
