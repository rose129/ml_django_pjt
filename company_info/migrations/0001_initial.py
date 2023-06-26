# Generated by Django 3.2 on 2023-06-26 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='startup_ranking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.CharField(db_column='logo', max_length=100)),
                ('ranking', models.CharField(db_column='ranking', max_length=15)),
                ('company_name', models.CharField(db_column='company_name', max_length=100)),
                ('recap', models.CharField(db_column='recap', max_length=100)),
            ],
        ),
    ]
