# Generated by Django 3.2.3 on 2021-07-22 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.google.com/search?q=anjel&sxsrf=ALeKk03Tifazj0RdBo1EZAr0JXlm_J9tGQ:1626957942745&tbm=isch&source=iu&ictx=1&fir=Adiur5h6oZKXnM%252C7LZnuQScDtaARM%252C_&vet=1&usg=AI4_-kRdogdpoTbNV-WfoDyR1FQjiYsliQ&sa=X&ved=2ahUKEwim8_bR2vbxAhX1zDgGHdQtB6MQ9QF6BAgDEAE#imgrc=Adiur5h6oZKXnM', max_length=500),
        ),
    ]
