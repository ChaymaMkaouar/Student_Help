# Generated by Django 5.0.3 on 2024-05-17 22:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student_Help', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friends', models.ManyToManyField(related_name='friends', to='Student_Help.user')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='friend_list', to='Student_Help.user')),
            ],
        ),
    ]
