# Generated by Django 2.2.6 on 2019-11-17 16:54

from django.db import migrations
from django.core.files import File


def create_default_image(apps, schema_editor):
    file_name = 'default.jpg'
    Image = apps.get_model('images', 'image')

    img = Image.objects.create(
        title='default',
        value=file_name
    )
    img.value.save(
        file_name,
        File(
            open('images/fixtures/images/default.jpg', 'rb')
        )
    )


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [migrations.RunPython(
    	create_default_image,
    	lambda x,y: (x,y)
    	)
    ]