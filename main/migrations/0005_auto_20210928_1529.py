# Generated by Django 3.2.7 on 2021-09-28 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_company_allowed_domain'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='info',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.customuser'),
            preserve_default=False,
        ),
    ]