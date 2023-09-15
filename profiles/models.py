"""
Defines the models of the profiles app.
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile Model.
    Profiles are linked to the User Model through their user OneToOneField field
    ...
    Attributes
    ----------
    user : FK
        user to which the profile is linked
    favorite_city : str
        favorite city of the profile

    Methods
    -------
    __str__():
        Returns the username of the user linked to the profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Profile model str method.
        It defines what string is returned when str(<a profile object>) is called.
        ...
        Parameters
        ----------
        None
        ...
        Returns
        -------
        A string representing the profile like so : '<profile_user_username>'
        """
        return self.user.username
