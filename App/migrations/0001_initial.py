# Generated by Django 3.0.5 on 2022-07-29 07:48

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BbCategoriesImport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.IntegerField(blank=True, null=True)),
                ('detailid', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bb_categories_import',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BbDetailsImport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.IntegerField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bb_details_import',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BbProductImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.IntegerField(blank=True, null=True)),
                ('label', models.TextField(blank=True, null=True)),
                ('unit', models.TextField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('width', models.IntegerField(blank=True, null=True)),
                ('href', models.TextField(blank=True, null=True)),
                ('s3ref', models.TextField(blank=True, null=True)),
                ('primaryimage', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bb_product_images',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BbProductImport',
            fields=[
                ('id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('addToCartUrl', models.TextField(blank=True, null=True)),
                ('bestSellingRank', models.TextField(blank=True, null=True)),
                ('color', models.TextField(blank=True, null=True)),
                ('condition', models.TextField(blank=True, null=True)),
                ('customerReviewAverage', models.FloatField(blank=True, null=True)),
                ('customerReviewCount', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('dollarSavings', models.TextField(blank=True, null=True)),
                ('features', models.TextField(blank=True, null=True)),
                ('freeShipping', models.BooleanField(blank=True, null=True)),
                ('includedItem', models.TextField(blank=True, null=True)),
                ('inStoreAvailability', models.BooleanField(blank=True, null=True)),
                ('inStoreAvailabilityText', models.TextField(blank=True, null=True)),
                ('longDescription', models.TextField(blank=True, null=True)),
                ('manufacturer', models.TextField(blank=True, null=True)),
                ('mobileUrl', models.TextField(blank=True, null=True)),
                ('modelNumber', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('onlineAvailability', models.BooleanField(blank=True, null=True)),
                ('onlineAvailabilityText', models.TextField(blank=True, null=True)),
                ('onSale', models.BooleanField(blank=True, null=True)),
                ('preowned', models.BooleanField(blank=True, null=True)),
                ('regularPrice', models.TextField(blank=True, null=True)),
                ('salePrice', models.TextField(blank=True, null=True)),
                ('shippingCost', models.TextField(blank=True, null=True)),
                ('shortDescription', models.TextField(blank=True, null=True)),
                ('sku', models.TextField(blank=True, null=True)),
                ('thumbnailImage', models.TextField(blank=True, null=True)),
                ('type', models.TextField(blank=True, null=True)),
                ('upc', models.TextField(blank=True, null=True)),
                ('url', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bestbuy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Databasechangelog',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=255)),
                ('filename', models.CharField(max_length=255)),
                ('dateexecuted', models.DateTimeField()),
                ('orderexecuted', models.IntegerField()),
                ('exectype', models.CharField(max_length=10)),
                ('md5sum', models.CharField(blank=True, max_length=35, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('comments', models.CharField(blank=True, max_length=255, null=True)),
                ('tag', models.CharField(blank=True, max_length=255, null=True)),
                ('liquibase', models.CharField(blank=True, max_length=20, null=True)),
                ('contexts', models.CharField(blank=True, max_length=255, null=True)),
                ('labels', models.CharField(blank=True, max_length=255, null=True)),
                ('deployment_id', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'databasechangelog',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Databasechangeloglock',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('locked', models.BooleanField()),
                ('lockgranted', models.DateTimeField(blank=True, null=True)),
                ('lockedby', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'databasechangeloglock',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DevopsBestBuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VendorID', models.TextField(max_length=250)),
                ('VendorName', models.CharField(max_length=250)),
                ('Timestamp', models.CharField(max_length=250)),
                ('TotalTime', models.TextField(max_length=250)),
                ('TotalItems', models.CharField(max_length=250)),
                ('NewItems', models.CharField(max_length=250)),
                ('UpdatedItems', models.CharField(max_length=250)),
                ('Errors', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'devops',
                'managed': False,
            },
        ),
    ]