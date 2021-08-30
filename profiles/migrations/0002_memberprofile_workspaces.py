# Generated by Django 3.2.6 on 2021-08-29 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workspace', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberprofile',
            name='workspaces',
            field=models.ManyToManyField(through='workspace.WorkspaceMembers', to='workspace.Workspace'),
        ),
    ]