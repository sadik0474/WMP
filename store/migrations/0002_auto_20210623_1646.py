# Generated by Django 3.0.6 on 2021-06-23 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='author',
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]