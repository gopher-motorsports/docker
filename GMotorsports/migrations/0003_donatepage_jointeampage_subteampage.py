# Generated by Django 2.2.15 on 2020-08-09 21:15

import cms.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('GMotorsports', '0002_carspage_teampage'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubteamPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainp', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mainpplaceholder', slotname='mainp', to='cms.Placeholder')),
                ('subteam_image', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subteam_imageplaceholder', slotname='subteam_image', to='cms.Placeholder')),
                ('subteam_leader', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subteam_leaderplaceholder', slotname='subteam_leader', to='cms.Placeholder')),
            ],
        ),
        migrations.CreateModel(
            name='JoinTeamPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jointeam', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jointeamplaceholder', slotname='jointeam', to='cms.Placeholder')),
                ('meetingtime', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetingtimeplaceholder', slotname='meetingtime', to='cms.Placeholder')),
            ],
        ),
        migrations.CreateModel(
            name='DonatePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donatep', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='donatepplaceholder', slotname='donatep', to='cms.Placeholder')),
            ],
        ),
    ]
