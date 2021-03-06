# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-21 18:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields

GROUPS = ['General Staff', 'Internal Users', 'Legal Team Members', 'Marketing Reviewers', 'Partner Managers',
          'Partner Support Members', 'Project Coordinators', 'Publisher Admins', 'Publishers']
PERMISSION_GROUPS = ['Internal Users', 'Marketing Reviewers', 'Partner Coordinators', 'Publishers']
SWITCHES = ['publish_person_to_marketing_site']


def create_groups(apps, _schema_editor):
    Group = apps.get_model('auth', 'Group')
    for group in GROUPS:
        Group.objects.get_or_create(name=group)


def remove_groups(apps, _schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(name__in=GROUPS).delete()


def add_people_permission(apps, _schema_editor):
    Permission = apps.get_model('auth', 'Permission')
    Group = apps.get_model('auth', 'Group')

    target_permissions = Permission.objects.filter(
        codename__in=['add_person', 'change_person', 'delete_person']
    )

    permission_groups = Group.objects.filter(name__in=PERMISSION_GROUPS)
    for group in permission_groups:
        group.permissions.add(*target_permissions)


def remove_people_permission(apps, _schema_editor):
    Permission = apps.get_model('auth', 'Permission')
    Group = apps.get_model('auth', 'Group')

    target_permissions = Permission.objects.filter(
        codename__in=['add_person', 'change_person', 'delete_person']
    )

    permission_groups = Group.objects.filter(name__in=PERMISSION_GROUPS)
    for group in permission_groups:
        group.permissions.remove(*target_permissions)


def create_switches(apps, _schema_editor):
    Switch = apps.get_model('waffle', 'Switch')
    for switch in SWITCHES:
        Switch.objects.get_or_create(name=switch, defaults={'active': False})


def remove_switches(apps, _schema_editor):
    Switch = apps.get_model('waffle', 'Switch')
    Switch.objects.filter(name__in=SWITCHES).delete()


class Migration(migrations.Migration):

    replaces = [('publisher', '0001_initial'), ('publisher', '0002_auto_20160729_1027'), ('publisher', '0003_auto_20160801_1757'), ('publisher', '0004_auto_20160810_0854'), ('publisher', '0005_auto_20160901_0003'), ('publisher', '0006_auto_20160902_0726'), ('publisher', '0007_auto_20160905_1020'), ('publisher', '0008_auto_20160928_1015'), ('publisher', '0009_auto_20160929_1927'), ('publisher', '0010_auto_20161006_1151'), ('publisher', '0011_userattributes'), ('publisher', '0012_auto_20161020_0718'), ('publisher', '0013_create_enable_email_notifications_switch'), ('publisher', '0014_create_admin_group'), ('publisher', '0015_auto_20161117_1210'), ('publisher', '0016_auto_20161129_0910'), ('publisher', '0017_auto_20161201_1501'), ('publisher', '0018_create_internal_user_group'), ('publisher', '0019_create_user_groups'), ('publisher', '0020_auto_20161214_1304'), ('publisher', '0021_auto_20161214_1356'), ('publisher', '0022_auto_20161222_2135'), ('publisher', '0023_auto_20161228_1350'), ('publisher', '0024_auto_20170105_1626'), ('publisher', '0025_auto_20170106_1830'), ('publisher', '0026_create_switch_hide_features_for_pilot'), ('publisher', '0027_remove_old_permissions'), ('publisher', '0028_create_partner_manager_group'), ('publisher', '0029_auto_20170119_0934'), ('publisher', '0030_create_switch_add_instructor_feature'), ('publisher', '0031_courserunstate_coursestate_historicalcourserunstate_historicalcoursestate'), ('publisher', '0032_create_switch_for_comments'), ('publisher', '0033_auto_20170213_0914'), ('publisher', '0034_auto_20170213_0918'), ('publisher', '0035_publisheruser'), ('publisher', '0036_auto_20170216_0946'), ('publisher', '0037_auto_20170221_1150'), ('publisher', '0038_auto_20170223_0723'), ('publisher', '0039_rename_partner_coordinator_group'), ('publisher', '0040_auto_20170223_1241'), ('publisher', '0041_auto_20170306_1002'), ('publisher', '0042_auto_20170306_1014'), ('publisher', '0043_auto_20170321_1239'), ('publisher', '0044_auto_20170323_0749'), ('publisher', '0045_auto_20170330_0729'), ('publisher', '0046_auto_20170413_0935'), ('publisher', '0047_auto_20170413_1010'), ('publisher', '0048_auto_20170511_1059'), ('publisher', '0049_auto_20170518_1017'), ('publisher', '0050_auto_20170524_1909'), ('publisher', '0051_auto_20170525_1049'), ('publisher', '0052_auto_20170529_1002'), ('publisher', '0053_auto_20170604_1502'), ('publisher', '0054_auto_20170605_0953'), ('publisher', '0055_auto_20170620_1500'), ('publisher', '0056_auto_20170621_1712'), ('publisher', '0057_auto_20170920_1821'), ('publisher', '0058_auto_20170927_1758'), ('publisher', '0059_auto_20170928_0425'), ('publisher', '0060_auto_20171004_0521'), ('publisher', '0061_add_people_permission'), ('publisher', '0062_auto_20171212_2016'), ('publisher', '0063_auto_20171219_1841'), ('publisher', '0064_auto_20180125_1836'), ('publisher', '0065_auto_20180507_0951'), ('publisher', '0066_add_default_pacing_type'), ('publisher', '0067_auto_20181030_1426'), ('publisher', '0068_auto_20181105_1630'), ('publisher', '0069_move_has_ofac_restriction'), ('publisher', '0070_drupalloaderconfig'), ('publisher', '0071_auto_20181205_1528'), ('publisher', '0072_auto_20181219_2100'), ('publisher', '0073_drupalloaderconfig_load_unpublished_course_runs'), ('publisher', '0074_remove_preview_url'), ('publisher', '0075_auto_20190213_2015'), ('publisher', '0076_publisher_masters_track_rerun'), ('publisher', '0077_external-key'), ('publisher', '0078_delete_drupalloaderconfig'), ('publisher', '0079_course_url_slug'), ('publisher', '0080_remove_publisher_waffle_switches'), ('publisher', '0081_initialize_course_url_slug'), ('publisher', '0082_auto_20190909_1600'), ('publisher', '0083_publisher_course_unique_url_slug'), ('publisher', '0084_make_course_has_ofac_restrictions_nullable'), ('publisher', '0085_remove_course_has_ofac_restrictions'), ('publisher', '0086_make_auto_create_in_studio_null_boolean'), ('publisher', '0087_remove_auto_create_in_studio'), ('publisher', '0088_delete_enable_email_notifications_switch'), ('publisher', '0089_drop_tables')]

    initial = True

    dependencies = [
        ('course_metadata', '0001_squashed_0033_courserun_mobile_available'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('waffle', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            code=create_groups,
            reverse_code=remove_groups,
        ),
        migrations.RunPython(
            code=add_people_permission,
            reverse_code=remove_people_permission,
        ),
        migrations.RunPython(
            code=create_switches,
            reverse_code=remove_switches,
        ),
        migrations.CreateModel(
            name='UserAttributes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('enable_email_notification', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'UserAttributes',
            },
        ),
        migrations.CreateModel(
            name='HistoricalOrganizationUserRole',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('role', models.CharField(choices=[('partner_manager', 'Partner Manager'), ('project_coordinator', 'Project Coordinator'), ('marketing_reviewer', 'Marketing Reviewer'), ('publisher', 'Publisher')], max_length=63, verbose_name='Organization Role')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='course_metadata.Organization')),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'historical organization user role',
                'get_latest_by': 'history_date',
                'ordering': ('-history_date', '-history_id'),
            },
        ),
        migrations.CreateModel(
            name='OrganizationUserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('role', models.CharField(choices=[('partner_manager', 'Partner Manager'), ('project_coordinator', 'Project Coordinator'), ('marketing_reviewer', 'Marketing Reviewer'), ('publisher', 'Publisher')], max_length=63, verbose_name='Organization Role')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_user_roles', to='course_metadata.Organization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_user_roles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='organizationuserrole',
            unique_together=set([('organization', 'user', 'role')]),
        ),
        migrations.CreateModel(
            name='HistoricalOrganizationExtension',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('group', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='auth.Group')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='course_metadata.Organization')),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'historical organization extension',
                'get_latest_by': 'history_date',
                'ordering': ('-history_date', '-history_id'),
            },
        ),
        migrations.CreateModel(
            name='OrganizationExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='organization_extension', to='auth.Group')),
                ('organization', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='organization_extension', to='course_metadata.Organization')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'permissions': (('publisher_edit_course', 'Can edit course'), ('publisher_edit_course_run', 'Can edit course run'), ('publisher_view_course', 'Can view course'), ('publisher_view_course_run', 'Can view the course run')),
                'abstract': False,
            },
        ),
    ]
