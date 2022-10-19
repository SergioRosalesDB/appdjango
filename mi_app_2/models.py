from django.db import models
import uuid
from djongo import models


class BbCategoriesImport(models.Model):
    productid = models.IntegerField(blank=True, null=True)
    detailid = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'bb_categories_import'

        def __str__(self):
            fila = "Producid: " + self.productid + "Detailid: " + self.detailid + "Name: " + self.name
            return fila




class BbDetailsImport(models.Model):
    productid = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bb_details_import'


class BbProductImages(models.Model):
    productid = models.IntegerField(blank=True, null=True)
    label = models.TextField(blank=True, null=True)
    unit = models.TextField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    href = models.TextField(blank=True, null=True)
    s3ref = models.TextField(blank=True, null=True)
    primaryimage = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bb_product_images'


class Bestbuymodel(models.Model):
    _id = models.ObjectIdField()
    accessories = models.TextField(blank=True, null=True)
    addToCartUrl = models.TextField(blank=True, null=True)
    bestSellingRank = models.TextField(blank=True, null=True)
    categoryPath = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)
    condition = models.TextField(blank=True, null=True)
    customerReviewAverage = models.FloatField(blank=True, null=True)
    customerReviewCount = models.IntegerField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    dollarSavings = models.TextField(blank=True, null=True) 
    features = models.TextField(blank=True, null=True)  
    freeShipping = models.BooleanField(blank=True, null=True)
    includedItem = models.TextField(blank=True, null=True)  
    inStoreAvailability = models.BooleanField(blank=True, null=True)
    inStoreAvailabilityText = models.TextField(blank=True, null=True)
    longDescription = models.TextField(blank=True, null=True)
    manufacturer = models.TextField(blank=True, null=True)
    mobileUrl = models.TextField(blank=True, null=True)
    modelNumber = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    onlineAvailability = models.BooleanField(blank=True, null=True)
    onlineAvailabilityText = models.TextField(blank=True, null=True)
    onSale = models.BooleanField(blank=True, null=True)
    preowned = models.BooleanField(blank=True, null=True)
    regularPrice = models.TextField(blank=True, null=True)  
    salePrice = models.TextField(blank=True, null=True)  
    shippingCost = models.TextField(blank=True, null=True)  
    shortDescription = models.TextField(blank=True, null=True)
    sku = models.TextField(blank=True, null=True)
    thumbnailImage = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    upc = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bestbuy'

    
    def get_data(self):
        return {
            
            'accessories': self.accessories,
            'addToCartUrl': self.addToCartUrl,
            'bestSellingRank': self.bestSellingRank,
            'categoryPath': self.categoryPath,
            'color': self.color,
            'condition': self.condition,
            'customerReviewAverage': self.customerReviewAverage,
            'customerReviewCount': self.customerReviewCount,
            'details': self.details,
            'description': self.description,
            'dollarSavings': self.dollarSavings,
            'features': self.features,
            'freeShipping': self.freeShipping,
            'includedItem': self.includedItem,
            'inStoreAvailability': self.inStoreAvailability,
            'inStoreAvailabilityText': self.inStoreAvailabilityText,
            'longDescription': self.longDescription,
            'manufacturer': self.manufacturer,
            'mobileUrl': self.mobileUrl,
            'modelNumber': self.modelNumber,
            'name': self.name,
            'onlineAvailability': self.onlineAvailability,
            'onlineAvailabilityText': self.onlineAvailabilityText,
            'onSale': self.onSale,
            'preowned': self.preowned,
            'regularPrice': self.regularPrice,
            'salePrice': self.salePrice,
            'shippingCost': self.shippingCost,
            'shortDescription': self.shortDescription,
            'sku': self.sku,
            'thumbnailImage': self.thumbnailImage,
            'type': self.type,
            'upc': self.upc,
            'url': self.url,

        }

class Lowesmodel(models.Model):
    _id = models.ObjectIdField()
    product = models.TextField(blank=True, null=True)
    LACPreApprovalPromotion = models.TextField(blank=True, null=True)
    additionalServices = models.TextField(blank=True, null=True)
    financeTermId = models.TextField(blank=True, null=True)
    itemInventory = models.TextField(blank=True, null=True)
    itemNumber = models.TextField(blank=True, null=True)
    lacPromotions = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    locator = models.TextField(blank=True, null=True)
    mfePrice = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)
    productAssoc = models.TextField(blank=True, null=True)
    productLevelPromotions = models.TextField(blank=True, null=True)
    productPromotion = models.TextField(blank=True, null=True)
    restriction = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'lowes'


class Homemodel(models.Model):
    _id = models.ObjectIdField()
    fulfillment = models.TextField(blank=True, null=True)
    itemId = models.TextField(blank=True, null=True)
    dataSources = models.TextField(blank=True, null=True)
    identifiers = models.TextField(blank=True, null=True)
    availabilityType = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    media = models.TextField(blank=True, null=True)
    pricing = models.TextField(blank=True, null=True)
    reviews = models.TextField(blank=True, null=True)
    seo = models.TextField(blank=True, null=True)
    specificationGroup = models.TextField(blank=True, null=True)
    taxonomy = models.TextField(blank=True, null=True)
    favoriteDetail = models.TextField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    sizeAndFitDetail = models.TextField(blank=True, null=True)
    badges = models.TextField(blank=True, null=True)
    seoDescription = models.TextField(blank=True, null=True)
    dataSource = models.TextField(blank=True, null=True)
    keyProductFeatures = models.TextField(blank=True, null=True)
    subscription = models.TextField(blank=True, null=True)
    bestSellerRank = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'home_depot'

class Walmartmodel(models.Model):
    _id = models.ObjectIdField()
    type = models.TextField(blank=True, null=True)
    model = models.TextField(blank=True, null=True)
    upc = models.TextField(blank=True, null=True)
    usItemId = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    priceInfo = models.TextField(blank=True, null=True)
    secondaryOfferPrice = models.TextField(blank=True, null=True)
    shortDescription = models.TextField(blank=True, null=True)
    shippingOption = models.TextField(blank=True, null=True)
    averageRating = models.TextField(blank=True, null=True)
    numberOfReviews = models.TextField(blank=True, null=True)
    imageInfo = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'Walmart'


class Databasechangelog(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    author = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    dateexecuted = models.DateTimeField()
    orderexecuted = models.IntegerField()
    exectype = models.CharField(max_length=10)
    md5sum = models.CharField(max_length=35, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    tag = models.CharField(max_length=255, blank=True, null=True)
    liquibase = models.CharField(max_length=20, blank=True, null=True)
    contexts = models.CharField(max_length=255, blank=True, null=True)
    labels = models.CharField(max_length=255, blank=True, null=True)
    deployment_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'databasechangelog'


class Databasechangeloglock(models.Model):
    id = models.IntegerField(primary_key=True)
    locked = models.BooleanField()
    lockgranted = models.DateTimeField(blank=True, null=True)
    lockedby = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'databasechangeloglock'


class Databasechangeloglock(models.Model):
    id = models.IntegerField(primary_key=True)
    locked = models.BooleanField()
    lockgranted = models.DateTimeField(blank=True, null=True)
    lockedby = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'databasechangeloglock'

class DevopsBestBuy(models.Model):
    VendorID = models.TextField(max_length=250)
    VendorName = models.CharField(max_length=250)
    Timestamp = models.CharField(max_length=250)
    TotalTime = models.TextField(max_length=250)
    TotalItems = models.CharField(max_length=250)
    NewItems = models.CharField(max_length=250)
    UpdatedItems =  models.CharField(max_length=250)
    Errors = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'devops'

    def get_data(self):
        return {
            'VendorID': self.VendorID,
            'VendorName': self.VendorName,
            'Timestamp': self.Timestamp,
            'TotalTime': self.TotalTime,
            'TotalItems': self.TotalItems,
            'NewItems': self.NewItems,
            'UpdatedItems': self.UpdatedItems,
            'Errors': self.Errors,
        }


class Productlist(models.Model):
    category = models.TextField(max_length=250,  null=True)
    matchid = models.TextField(max_length=250,  null=True)
    modelnumber = models.TextField(max_length=250,  null=True)
    brand = models.TextField(max_length=250,  null=True)
    loweomniid = models.TextField(max_length=250,  null=True)
    lowesdescription = models.TextField(max_length=250,  null=True)
    homedepotitemid = models.TextField(max_length=250,  null=True)
    homedepotproductlabel = models.TextField(max_length=250,  null=True)
    bestbuysku = models.TextField(max_length=250,  null=True)
    bestbuyproductname = models.TextField(max_length=250,  null=True)
    matched = models.TextField(max_length=250,  null=True)
    delete = models.TextField(max_length=250,  null=True)

    class Meta:
        managed = False
        db_table = 'productlist'