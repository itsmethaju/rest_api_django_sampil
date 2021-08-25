from django.db import models

# Create your models here.
class Task(models.Model):
    Task_name=models.CharField(max_length=250)
    Task_desc=models.CharField(max_length=250)
    date_created=models.DateTimeField(auto_now=True)
    completed=models.BooleanField(default=False)
    image=models.ImageField(upload_to='Image/',default="Image/None/noimg.jpg")

