# Generated by Django 4.2.9 on 2024-01-03 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=200)),
                ('degree', models.CharField(max_length=200)),
                ('gpa', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('start_date', models.CharField(max_length=200)),
                ('end_date', models.CharField(max_length=200)),
                ('other_information', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='CV_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('bio', models.TextField(max_length=2000)),
                ('education', models.ManyToManyField(to='CV_gen.education')),
                ('interests', models.ManyToManyField(to='CV_gen.interests')),
                ('skills', models.ManyToManyField(to='CV_gen.skills')),
                ('work_experience', models.ManyToManyField(to='CV_gen.workexperience')),
            ],
        ),
    ]
