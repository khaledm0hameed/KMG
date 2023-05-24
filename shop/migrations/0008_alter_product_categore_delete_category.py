# Generated by Django 4.2.1 on 2023-05-24 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_category_alter_product_categore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categore',
            field=models.CharField(blank=True, choices=[('Laptop', 'Laptop'), ('Computer', 'Computer'), ('Phone', 'Phone'), ('Screen', 'Screen')], max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='category',
        ),
    ]