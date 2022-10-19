from django.db import models

class Productlist(models.Model):
    category = models.CharField(max_length=250, blank=True, null=True)
    matchid = models.CharField(max_length=250,  blank=True, null=True)
    modelnumber = models.CharField(max_length=250, blank=True, null=True)
    brand = models.CharField(max_length=250,  blank=True, null=True)
    loweomniid = models.CharField(max_length=250,  blank=True, null=True)
    lowesdescription = models.CharField(max_length=250,  blank=True, null=True)
    homedepotitemid = models.CharField(max_length=250,  blank=True, null=True)
    homedepotproductlabel = models.CharField(max_length=250,  blank=True, null=True)
    bestbuysku = models.CharField(max_length=250,  blank=True, null=True)
    bestbuyproductname = models.CharField(max_length=250,  blank=True, null=True)
    matched = models.CharField(max_length=250,  blank=True, null=True)
    delete = models.CharField(max_length=250,  blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productlist'


class Product(models.Model):
    ProductsKey = models.AutoField(primary_key=True, serialize=False)
    SourceKey = models.CharField(max_length=500, blank=True, null=True)
    CategoryKey = models.CharField(max_length=500, blank=True, null=True)
    ModelNumber = models.CharField(max_length=500, blank=True, null=True)
    Brand = models.CharField(max_length=500, blank=True, null=True)
    SourcesId = models.CharField(max_length=500, blank=True, null=True)
    ProductTitle = models.CharField(max_length=500, blank=True, null=True)
    CreatedDate = models.CharField(max_length=500, blank=True, null=True)
    Matchable = models.CharField(max_length=500, blank=True, null=True)
    DateMatched = models.CharField(max_length=500, blank=True, null=True)
    MatchedBy =  models.CharField(max_length=500, blank=True, null=True)
    StartDate = models.CharField(max_length=500, blank=True, null=True)
    EndDate = models.CharField(max_length=500, blank=True, null=True)
    Version = models.CharField(max_length=500, blank=True, null=True)
    CurrentFlag = models.CharField(max_length=500, blank=True, null=True)
    ProductDescription = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Products'

class Deleteproductmatch(models.Model):
    categorydescr = models.CharField(max_length=500, blank=True, null=True)
    matchid = models.CharField(max_length=500, blank=True, null=True)
    modelnumber = models.CharField(max_length=500, blank=True, null=True)
    brand = models.CharField(max_length=500, blank=True, null=True)
    source = models.CharField(max_length=500, blank=True, null=True)
    productid = models.CharField(max_length=500, blank=True, null=True)
    productdescription = models.CharField(max_length=500, blank=True, null=True)
    matchtypedescr = models.CharField(max_length=500, blank=True, null=True)
    deleted = models.CharField(max_length=500, blank=True, null=True)
    addtomatch = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    

    class Meta:
        managed = False
        db_table = 'deleteproductmatch'

