# Generated by Django 4.2.5 on 2023-09-06 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_dt', models.DateTimeField(auto_now_add=True)),
                ('group', models.CharField(max_length=100)),
                ('symbol', models.ImageField(upload_to='images/symbols')),
                ('votes', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=100)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
