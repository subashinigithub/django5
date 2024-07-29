from django.db import models
from django.contrib.auth.models import User
class students(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    age=models.PositiveIntegerField()
    Qualifcation=models.CharField(max_length=255)
    Grade=models.PositiveIntegerField()
    Group=models.CharField(max_length=255)
    EmailId=models.EmailField(null=True)
    password=models.CharField(max_length=255,null=True)
    def __str__(self) -> str:
        return self.name
class Item(models.Model):
    category=models.CharField(max_length=255)
    subcategory=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    amount=models.PositiveIntegerField()
    def __str__(self) -> str:
        return self.name
    
    """
    {
    "category":"new",
    "subcategory":"lkg",
    "name":"padan",
    "amount":"159"
    }
    
    
    """


