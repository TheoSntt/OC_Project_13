"""
Defines the models of the lettings app.
"""
from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Address Model.
    Addresses are linked to the Letting Model through its address OneToOneField field
    ...
    Attributes
    ----------
    number : int
        street number for the address
    street : str
        name of the street for the address
    city : str
        name of the city of the address
    state : str
        name of the state of the address
    zip_code : int
        ZIP code for the address
    country_iso_code : str
        country ISO code for the address

    Methods
    -------
    __str__():
        Returns the street number followed by the name of the street
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
        It defines what string is returned when str(<an address object>) is called.
        ...
        Parameters
        ----------
        None
        ...
        Returns
        -------
        A string representing the address like so : '<street number> <street name>'
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Letting Model.
    Lettings are linked to the Address Model through their address OneToOneField field
    ...
    Attributes
    ----------
    title : str
        title of the letting
    address : FK
        address of the letting

    Methods
    -------
    __str__():
        Returns the title of the letting
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Letting model str method.
        It defines what string is returned when str(<a letting object>) is called.
        ...
        Parameters
        ----------
        None
        ...
        Returns
        -------
        A string representing the letting like so : '<letting title>'
        """
        return self.title
