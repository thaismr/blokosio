# Generated by Django 3.2.6 on 2021-08-30 00:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_remove_memberprofile_workspaces'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workspace', '0004_alter_workspace_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workspace',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='workspace',
            name='members',
            field=models.ManyToManyField(related_name='workspaces', through='workspace.WorkspaceMembers', to='profiles.MemberProfile'),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='owner',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workspaces_owned', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='workspacemembers',
            constraint=models.UniqueConstraint(fields=('workspace', 'member'), name='unique_membership'),
        ),
    ]
