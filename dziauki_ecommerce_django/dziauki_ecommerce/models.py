from django.db import models

# main table for property posting - few basic attributes
class PropertyPosting(models.Model):
    postingID = models.AutoField(primary_key=True)
    postingTitle = models.CharField(max_length=1000)
    postingDate = models.DateField(null=True)
    floor = models.CharField(max_length=20, null=True)
    buildingNumber = models.CharField(max_length=20, null=True)
    streetName = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    ownershipType = models.CharField(max_length=100, null=True)
    institutionalSeller = models.BooleanField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    roomNumber = models.IntegerField(null=True)


    