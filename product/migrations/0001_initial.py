# Generated by Django 4.2.1 on 2023-08-06 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('diagonal', models.CharField(max_length=255)),
                ('ram', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('category', models.ManyToManyField(to='product.category')),
            ],
        ),
    ]