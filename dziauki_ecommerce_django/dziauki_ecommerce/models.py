from django.db import models

# main table for property posting - few basic attributes
class PropertyPosting(models.Model):
    postingID = models.AutoField(primary_key=True)
    postingTitle = models.CharField(max_length=1000)
    postingDate = models.DateField(blank=True, null=True),
    floor = models.CharField(max_length=20, blank=True)
    buildingNumber = models.CharField(max_length=20, blank=True)
    streetName = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    # flag to differentiate institutional and private offers (private by default)
    institutionalSeller = models.BooleanField(blank=True, default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    roomNumber = models.IntegerField(blank=True, null=True)
    usableArea = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # flag determining if posting is for rent or for sale (sale by default)
    forSaleFlag = models.BooleanField(default=True)
    ownershipType = models.CharField(max_length=100, blank=True)
    # field for additional fees for tenanats
    otherFeesAndBills = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)

    