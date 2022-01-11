from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import ModelState
from django.utils.timezone import now
from django.urls import reverse
from datetime import datetime

# Create your models here.
# makemigrations - creates changes and stores in a file
# migrate - applies the pending changes created my makemigrations

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):                  
        return self.name                # Returns name in database

    # def get_absolute_url(self):
    #     return reverse('users')

class Application(models.Model):
    COURSES = (
    ('Artificial Intelligence & Data Science', 'Artificial Intelligence & Data Science'),
    ('Artificial Intelligence & Machine Learning', 'Artificial Intelligence & Machine Learning'),
    ('IoT, Block-Chain Technology & Cyber Security', 'IoT, Block-Chain Technology & Cyber Security'),
    ('Computer Science Engineering', 'Computer Science Engineering'),
    ('Information Technology', 'Information Technology'),
    ('Electronics & Communication Engineering', 'Electronics & Communication Engineering'),
    ('Electrical & Electronics Engineering', 'Electrical & Electronics Engineering'),
    ('Mechanical Engineering', 'Mechanical Engineering'),
    ('Civil Engineering', 'Civil Engineering'),
    ('Chemical Engineering', 'Chemical Engineering'),
    ('Biotechnology', 'Biotechnology'),
    )

    GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
    )

    STATUS = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    course = models.CharField(max_length=100, choices= COURSES)
    name = models.CharField(max_length=200) 
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128, default="None")
    DOB = models.DateField(default=datetime.today)
    email = models.EmailField() 
    phone = models.CharField(max_length=200) 
    address = models.TextField(max_length=200) 
    student_profile = models.ImageField(upload_to="images") 
    ssc_score = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    ssc_memo = models.ImageField(upload_to="images", null=True)
    ssc_tc = models.ImageField(upload_to="images", null=True)
    inter_score = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    inter_memo = models.ImageField(upload_to="images", null=True)
    inter_tc = models.ImageField(upload_to="images", null=True)
    eamcet_score = models.IntegerField(null=True)
    eamcet_memo = models.ImageField(upload_to="images", null=True)
    jee_score = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    jee_memo = models.ImageField(upload_to="images", null=True)
    Application_Status = models.TextField(max_length=100, choices=STATUS, default="Pending")
    message = models.TextField(max_length=100, default="", null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('users')