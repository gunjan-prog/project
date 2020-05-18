from django.db import models


from django.contrib.auth.models import User

class Customers(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    mobile=models.BigIntegerField(null=True)
    created_date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name