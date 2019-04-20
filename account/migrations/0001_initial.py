# Generated by Django 2.0.5 on 2019-04-15 08:02

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('donor', 'Donor'), ('receiver', 'Receiver')], default='receiver', max_length=10)),
                ('blood_group', models.CharField(choices=[('a+', 'A+'), ('b+', 'B+'), ('o+', 'O+'), ('a-', 'A-'), ('b-', 'B-'), ('o-', 'O-'), ('ab-', 'AB-'), ('AB+', 'AB+')], default='a+', max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]