# Generated by Django 3.2 on 2023-06-26 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recruiting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('company_intro', models.TextField()),
                ('main_duties', models.TextField()),
                ('requirments', models.TextField()),
                ('stack', models.TextField()),
                ('desirable_skills', models.TextField()),
                ('employee_benefits', models.TextField()),
                ('address', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
