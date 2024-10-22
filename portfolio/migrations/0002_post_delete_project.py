# Generated by Django 4.2.16 on 2024-10-22 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='posts/')),
                ('mood', models.CharField(blank=True, max_length=100, null=True)),
                ('pinned', models.BooleanField(default=False)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
