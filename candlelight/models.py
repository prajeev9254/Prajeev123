from django.db import models



class post(models.Model):
    head=models.CharField(max_length=111)
    desc=models.CharField(max_length=111)
    date=models.DateField(auto_now_add=True,null=True,blank=True)
    img=models.ImageField(upload_to='IMG')
