# Generated by Django 3.2.6 on 2021-08-29 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseUserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_profile', serialize=False, to='users.user')),
                ('bio', models.CharField(blank=True, max_length=30, verbose_name='Bio')),
                ('website', models.URLField(blank=True, max_length=255, verbose_name='Website')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Birth date')),
            ],
        ),
        migrations.CreateModel(
            name='ManagerProfile',
            fields=[
                ('baseuserprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='profiles.baseuserprofile')),
            ],
            bases=('profiles.baseuserprofile',),
        ),
        migrations.CreateModel(
            name='MemberProfile',
            fields=[
                ('baseuserprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='profiles.baseuserprofile')),
            ],
            options={
                'permissions': [('change_profile_status', 'Can change the status of user profiles')],
            },
            bases=('profiles.baseuserprofile',),
        ),
    ]
