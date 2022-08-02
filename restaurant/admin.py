from curses.ascii import EM
from tkinter import E
from django.contrib import admin
from .models import Restaurant, Employee, Menu, Component


admin.site.register(Restaurant)
admin.site.register(Employee)
admin.site.register(Menu)
admin.site.register(Component)
