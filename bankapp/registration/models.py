from django.db import models

# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-name"]


class Branch(models.Model):
    name = models.CharField(max_length=100, blank=True, default='Kovalam')
    district = models.ForeignKey(
        'District', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-name"]


gender_choice=(('male','MALE'),('female','FEMALE'),('others','OTHERS'))
account_choices=(('savings account','SAVINGS ACCOUNT'),('current account','CURRENT ACCOUNT'))

class register(models.Model):
    name=models.CharField(max_length=250)
    dob=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=200,choices=gender_choice, default='male')
    phone=models.IntegerField()
    email=models.CharField(max_length=250)
    address=models.TextField()

    district= models.ForeignKey(
        "District", on_delete=models.CASCADE, null=True, blank=True)
    branch = models.ForeignKey(
        'Branch', blank=True, on_delete=models.CASCADE, null=True)
    account=models.CharField(max_length=250,null=True,choices=account_choices,default='savings account')
    debit=models.BooleanField(default=True)
    credit = models.BooleanField(default=True)
    cheque = models.BooleanField(default=True)

    def __str__(self):
        return self.name