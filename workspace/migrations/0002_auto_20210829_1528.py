# Generated by Django 3.2.6 on 2021-08-29 18:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workspace', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workspace',
            name='manager',
        ),
        migrations.AddField(
            model_name='workspace',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='workspaces', to='users.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workspace',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
