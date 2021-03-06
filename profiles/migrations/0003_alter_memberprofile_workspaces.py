# Generated by Django 3.2.6 on 2021-08-29 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0002_auto_20210829_1528'),
        ('profiles', '0002_memberprofile_workspaces'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberprofile',
            name='workspaces',
            field=models.ManyToManyField(blank=True, through='workspace.WorkspaceMembers', to='workspace.Workspace'),
        ),
    ]
