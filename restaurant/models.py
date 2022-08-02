from sre_parse import CATEGORIES
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    TRADE_CHOISES = (
    ("WAITER", "Waiter"),
    ("BARTENDER", "Bartender"),
    ("ADMINISTRATOR", "Administrator"),
    # ...
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    trade = models.CharField(max_length=20, choices=TRADE_CHOISES)
    employed = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.user.username} - {self.trade}"

class Component(models.Model):
    CATEGORIES = (
        ("HOT DRINKS", "Hot drinks"),
        ("COLD DRINKS", "Cold drinks"),
        ("SALADS", "Salads"),
        # ...
    )
    category = models.CharField(max_length=25, choices=CATEGORIES, blank=True)
    component = models.CharField(max_length=25, blank=True)
    price = models.FloatField(blank=True)

    def __str__(self) -> str:
        return f"{self.category} {self.component} | {self.price}$"

class Menu(models.Model):
    DAYS = (
        ("MONDAY", "Monday"),
        ("TUESDAY", "Tuesday"),
        ("WEDNESDAY", "Wednesday"),
        ("THURSDAY", "Thursday"),
        ("FRIDAY", "Friday"),
        ("SATURDAY", "Saturday"),
        ("SUNDAY", "Sunday"),
        # ...
    )
    name = models.CharField(max_length=30, blank=True)
    day = models.CharField(max_length=10, choices=DAYS, blank=True)
    components = models.ManyToManyField(Component)

    def __str__(self) -> str:
        return f"{self.day} menu - {self.components.count()} components"

class Restaurant(models.Model):
    name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=13)
    employees = models.ManyToManyField(Employee)
    menus = models.ManyToManyField(Menu)

    def __str__(self) -> str:
        return f"Restaurant: {self.name} - {self.employees.count()} employees - {self.menus.count()} menus"

