from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserDetails(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    FullName = models.CharField(max_length=255,null=True, blank=True)
    phone = models.CharField(max_length=255,null=True, blank=True)

    @property
    def email(self):
        return self.user.email
    
    @property
    def username(self):
        return self.user.username

class ExperienceCategory(models.Model):
    Category = models.CharField(max_length=255,null=True, blank=True)
    Description = models.CharField(max_length=255,null=True, blank=True)
    Image = models.FileField(upload_to='ExperienceCategory',null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.Image.delete()
        super().delete(*args, **kwargs)

class ExperienceImages(models.Model):
    E_id = models.IntegerField(default=0,null=True, blank=True)
    Image = models.FileField(upload_to='ExperienceImages',null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.Image.delete()
        super().delete(*args, **kwargs)

class ExperienceIncluded(models.Model):
    E_id = models.IntegerField(default=0,null=True, blank=True)
    Types = models.CharField(max_length=255,null=True, blank=True)
    Lines = models.CharField(max_length=255,null=True, blank=True)

class Experience(models.Model):
    EC_id=models.IntegerField(default=0,null=True, blank=True)
    Category = models.CharField(max_length=255,null=True, blank=True)
    Name=models.CharField(max_length=255,null=True, blank=True)
    Image = models.FileField(upload_to='Experience',null=True, blank=True)
    SmallDescription = models.CharField(max_length=255,null=True, blank=True)
    Description = models.CharField(max_length=255,null=True, blank=True)
    Address = models.CharField(max_length=255,null=True, blank=True)
    Price = models.CharField(max_length=255,null=True, blank=True)
    Days = models.CharField(max_length=255,null=True, blank=True)
    Date = models.DateField(null=True, blank=True)
    EndDate = models.DateField(null=True, blank=True)
    EIm_id = models.IntegerField(default=0,null=True, blank=True)
    EIn_id = models.IntegerField(default=0,null=True, blank=True)
    EF_id = models.IntegerField(default=0,null=True, blank=True)
    View = models.CharField(max_length=255,null=True, blank=True)

    # def save(self, *args, **kwargs):
    #         Id = str(self.id)
    #         self.EIm_id=Id
    #         self.EIn_id=Id
    #         self.EF_id=Id
    #         super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        self.Image.delete()
        super().delete(*args, **kwargs)


class ExperienceFormsQ(models.Model):
    E_id = models.IntegerField(default=0,null=True, blank=True)
    Name=models.CharField(max_length=255,null=True, blank=True)
    Q1 = models.TextField(default='',blank=True)
    Q2 = models.TextField(default='',blank=True)
    Q3 = models.TextField(default='',blank=True)
    Q4 = models.TextField(default='',blank=True)
    Q5 = models.TextField(default='',blank=True)
    Q6 = models.TextField(default='',blank=True)
    Q7 = models.TextField(default='',blank=True)
    Q8 = models.TextField(default='',blank=True)
    Q9 = models.TextField(default='',blank=True)
    Q10 = models.TextField(default='',blank=True)
    Q11 = models.TextField(default='',blank=True)
    Q12 = models.TextField(default='',blank=True)
    Q13 = models.TextField(default='',blank=True)
    Q14 = models.TextField(default='',blank=True)
    Q15 = models.TextField(default='',blank=True)
    Q16 = models.TextField(default='',blank=True)
    Q17 = models.TextField(default='',blank=True)


class ExperienceFormsA(models.Model):
    E_id = models.IntegerField(default=0,null=True, blank=True)
    Name=models.CharField(max_length=255,null=True, blank=True)
    FullName = models.TextField(null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    Email = models.CharField(max_length=255,null=True, blank=True)
    Countrycode = models.CharField(max_length=255,null=True, blank=True)
    ContactNo = models.CharField(max_length=255,null=True, blank=True)
    WPNo = models.CharField(max_length=255,null=True, blank=True)
    Country = models.CharField(max_length=255,null=True, blank=True)
    Pincode = models.CharField(max_length=255,null=True, blank=True)
    SOP = models.TextField(null=True, blank=True)
    A1 = models.TextField(default='',blank=True)
    A2 = models.TextField(default='',blank=True)
    A3 = models.TextField(default='',blank=True)
    A4 = models.TextField(default='',blank=True)
    A5 = models.TextField(default='',blank=True)
    A6 = models.TextField(default='',blank=True)
    A7 = models.TextField(default='',blank=True)
    A8 = models.TextField(default='',blank=True)
    A9 = models.TextField(default='',blank=True)
    A10 = models.TextField(default='',blank=True)
    A11 = models.TextField(default='',blank=True)
    A12 = models.TextField(default='',blank=True)
    A13 = models.TextField(default='',blank=True)
    A14 = models.TextField(default='',blank=True)
    A15 = models.TextField(default='',blank=True)
    A16 = models.TextField(default='',blank=True)
    A17 = models.TextField(default='',blank=True)

class MemoriesModel(models.Model):
    Image = models.FileField(upload_to='Memories',null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.Image.delete()
        super().delete(*args, **kwargs)

# class Staysmodel(models.Model):
#     Name=models.CharField(max_length=255,null=True, blank=True)
#     Image = models.FileField(upload_to='Stays',null=True, blank=True)
#     SmallDescription = models.CharField(max_length=255,null=True, blank=True)
#     Overview = models.CharField(max_length=255,null=True, blank=True)
#     Location = models.TextField(default='',blank=True)
#     Rooms = models.CharField(max_length=255,null=True, blank=True)
#     Guests = models.CharField(max_length=255,null=True, blank=True)

class ContactModel(models.Model):
    FullName=models.CharField(max_length=255,null=True, blank=True)
    ContactNo=models.CharField(max_length=255,null=True, blank=True)
    WPNo=models.CharField(max_length=255,null=True, blank=True)
    Email=models.CharField(max_length=255,null=True, blank=True)
    Msg = models.TextField(default='',blank=True)

class ReviewsModel(models.Model):
    Non = models.CharField(default='0',max_length=255,null=True, blank=True)
    View = models.CharField(default='0',max_length=255,null=True, blank=True)
    Image = models.FileField(upload_to='Reviews',null=True, blank=True)
    Name=models.CharField(max_length=255,null=True, blank=True)
    Description = models.TextField(default='',blank=True)
    SmallDescription = models.TextField(default='',blank=True)