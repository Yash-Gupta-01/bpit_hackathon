from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User

district_choices= {
    ("Delhi","Delhi"),
    ("Mumbai","Mumbai")
}

class Volunteer(models.Model):
    """
    phone_no
    district
    is_active
    author/volunteered_by"""
    phone_no=PhoneField(unique=True,blank=False,null=False)
    district=models.CharField(max_length=100,choices=district_choices,blank=False,null=False)
    is_active=models.BooleanField(default=True)
    volunteered_by=models.OneToOneField(User,on_delete=models.CASCADE)
    joined_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.phone_no)

    class Meta:
        verbose_name_plural='Volunteer'
        ordering=['-joined_at']
