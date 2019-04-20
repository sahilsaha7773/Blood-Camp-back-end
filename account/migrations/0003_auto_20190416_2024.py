# Generated by Django 2.0.5 on 2019-04-16 14:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_auto_20190415_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friends', models.ManyToManyField(related_name='_friendship_friends_+', to='account.Friendship')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='friendship', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'friendship',
                'verbose_name_plural': 'friendships',
            },
        ),
        migrations.CreateModel(
            name='FriendshipRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=200)),
                ('created', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('accepted', models.BooleanField(default=False)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations_from', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations_to', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'friendship request',
                'verbose_name_plural': 'friendship requests',
            },
        ),
        migrations.CreateModel(
            name='UserBlocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blocks', models.ManyToManyField(related_name='blocked_by_set', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_blocks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user blocks',
                'verbose_name_plural': 'user blocks',
            },
        ),
        migrations.AlterUniqueTogether(
            name='friendshiprequest',
            unique_together={('to_user', 'from_user')},
        ),
    ]
