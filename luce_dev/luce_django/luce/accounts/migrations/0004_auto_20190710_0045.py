# Generated by Django 2.2.3 on 2019-07-10 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_ethereum_public_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='institution',
            field=models.CharField(default='None', max_length=255),
            preserve_default=False,
        ),
    ]
