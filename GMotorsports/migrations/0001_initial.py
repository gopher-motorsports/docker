# Generated by Django 2.2.15 on 2020-08-09 19:21

import cms.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstp1', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='firstp1placeholder', slotname='firstp1', to='cms.Placeholder')),
                ('firstp2', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='firstp2placeholder', slotname='firstp2', to='cms.Placeholder')),
                ('firstp3', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='firstp3placeholder', slotname='firstp3', to='cms.Placeholder')),
                ('firstphead', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='firstpheadplaceholder', slotname='firstphead', to='cms.Placeholder')),
                ('rank', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rankplaceholder', slotname='rank', to='cms.Placeholder')),
                ('secondp1', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secondp1placeholder', slotname='secondp1', to='cms.Placeholder')),
                ('secondp2', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secondp2placeholder', slotname='secondp2', to='cms.Placeholder')),
                ('secondphead', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secondpheadplaceholder', slotname='secondphead', to='cms.Placeholder')),
                ('thirdp1', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thirdp1placeholder', slotname='thirdp1', to='cms.Placeholder')),
                ('thirdp2', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thirdp2placeholder', slotname='thirdp2', to='cms.Placeholder')),
                ('thirdphead', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thirdpheadplaceholder', slotname='thirdphead', to='cms.Placeholder')),
            ],
        ),
        migrations.CreateModel(
            name='CompetitionPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comprankplaceholder', slotname='rank', to='cms.Placeholder')),
                ('year', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='yearplaceholder', slotname='year', to='cms.Placeholder')),
            ],
        ),
    ]