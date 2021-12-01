# Generated by Django 2.2.15 on 2020-08-09 20:26

import cms.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('GMotorsports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aerodynamics', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aerodynamicsplaceholder', slotname='aerodynamics', to='cms.Placeholder')),
                ('aerodynamics_image', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aerodynamics_imageplaceholder', slotname='aerodynamics_image', to='cms.Placeholder')),
                ('alumni1', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alumni1placeholder', slotname='alumni1', to='cms.Placeholder')),
                ('alumni2', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alumni2placeholder', slotname='alumni2', to='cms.Placeholder')),
                ('alumni3', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alumni3placeholder', slotname='alumni3', to='cms.Placeholder')),
                ('business', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='businessplaceholder', slotname='business', to='cms.Placeholder')),
                ('business_image', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='business_imageplaceholder', slotname='business_image', to='cms.Placeholder')),
                ('chief_engineer', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chief_engineerplaceholder', slotname='chief_engineer', to='cms.Placeholder')),
                ('chief_engineer_image', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chief_engineer_imageplaceholder', slotname='chief_engineer_image', to='cms.Placeholder')),
                ('electrical', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='electricalplaceholder', slotname='electrical', to='cms.Placeholder')),
                ('electrical_image', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='electrical_imageplaceholder', slotname='electrical_image', to='cms.Placeholder')),
                ('engine_drivetrain', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='engine_drivetrainplaceholder', slotname='engine_drivetrain', to='cms.Placeholder')),
                ('engine_drivetrain_image', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='engine_drivetrain_imageplaceholder', slotname='engine_drivetrain_image', to='cms.Placeholder')),
                ('ergonomics', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ergonomicsplaceholder', slotname='ergonomics', to='cms.Placeholder')),
                ('ergonomics_image', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ergonomics_imageplaceholder', slotname='ergonomics_image', to='cms.Placeholder')),
                ('frame_suspension', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='frame_suspensionplaceholder', slotname='frame_suspension', to='cms.Placeholder')),
                ('frame_suspension_image', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='frame_suspension_imageplaceholder', slotname='frame_suspension_image', to='cms.Placeholder')),
                ('president', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='presidentplaceholder', slotname='president', to='cms.Placeholder')),
                ('president_image', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='president_imageplaceholder', slotname='president_image', to='cms.Placeholder')),
                ('project_manager', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_managerplaceholder', slotname='project_manager', to='cms.Placeholder')),
                ('project_manager_image', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_manager_imageplaceholder', slotname='project_manager_image', to='cms.Placeholder')),
            ],
        ),
        migrations.CreateModel(
            name='CarsPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carshead', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carsheadplaceholder', slotname='carshead', to='cms.Placeholder')),
                ('carsp1', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carsp1placeholder', slotname='carsp1', to='cms.Placeholder')),
                ('carsp2', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carsp2placeholder', slotname='carsp2', to='cms.Placeholder')),
            ],
        ),
    ]
