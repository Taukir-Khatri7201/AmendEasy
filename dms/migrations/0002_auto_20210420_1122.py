# Generated by Django 3.1.6 on 2021-04-20 05:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='aadhar_queries_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Actual_AadharNo', models.BigIntegerField(validators=[django.core.validators.MaxValueValidator(999999999999)])),
                ('AadharNo', models.CharField(max_length=10)),
                ('fname', models.CharField(max_length=10)),
                ('mname', models.CharField(max_length=10)),
                ('lname', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=10)),
                ('address_proof', models.CharField(max_length=10)),
                ('contact_no', models.CharField(max_length=10)),
                ('dob', models.CharField(max_length=10)),
                ('birth_proof', models.CharField(max_length=10)),
                ('Gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='AdminInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmpId', models.CharField(max_length=100)),
                ('fName', models.CharField(default='abcd', max_length=50)),
                ('mName', models.CharField(default='xyz', max_length=50)),
                ('lName', models.CharField(default='pqrs', max_length=50)),
                ('DocName', models.CharField(max_length=100)),
                ('Image', models.ImageField(default='', upload_to='dms/images')),
            ],
        ),
        migrations.CreateModel(
            name='signup1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmpId', models.CharField(max_length=100)),
                ('fp_User', models.ImageField(default='', upload_to='dms/images')),
            ],
        ),
        migrations.RemoveField(
            model_name='aadhar',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='drivinglicence',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='pancard',
            name='name',
        ),
        migrations.RemoveField(
            model_name='pancardq',
            name='Street',
        ),
        migrations.RemoveField(
            model_name='pancardq',
            name='city',
        ),
        migrations.RemoveField(
            model_name='pancardq',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='ration',
            name='name',
        ),
        migrations.RemoveField(
            model_name='voterid',
            name='name',
        ),
        migrations.AddField(
            model_name='aadhar',
            name='fName',
            field=models.CharField(default='abcd', max_length=50),
        ),
        migrations.AddField(
            model_name='aadhar',
            name='lName',
            field=models.CharField(default='pqrs', max_length=50),
        ),
        migrations.AddField(
            model_name='aadhar',
            name='mName',
            field=models.CharField(default='xyz', max_length=50),
        ),
        migrations.AddField(
            model_name='aadharq',
            name='AadharNo',
            field=models.BigIntegerField(default=123, validators=[django.core.validators.MaxValueValidator(999999999999)]),
        ),
        migrations.AddField(
            model_name='aadharq',
            name='DOB',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='aadharq',
            name='Mobile_NUmber',
            field=models.BigIntegerField(default=9796959493, validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AddField(
            model_name='aadharq',
            name='Sex',
            field=models.CharField(default='male', max_length=6),
        ),
        migrations.AddField(
            model_name='aadharq',
            name='address_proof',
            field=models.ImageField(default='', upload_to='dms/images'),
        ),
        migrations.AddField(
            model_name='aadharq',
            name='birth_proof',
            field=models.ImageField(default='', upload_to='dms/images'),
        ),
        migrations.AddField(
            model_name='drivinglicence',
            name='fName',
            field=models.CharField(default='abcd', max_length=50),
        ),
        migrations.AddField(
            model_name='drivinglicence',
            name='lName',
            field=models.CharField(default='pqrs', max_length=50),
        ),
        migrations.AddField(
            model_name='drivinglicence',
            name='mName',
            field=models.CharField(default='xyz', max_length=50),
        ),
        migrations.AddField(
            model_name='licenceq',
            name='DOB',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='licenceq',
            name='Mobile_NUmber',
            field=models.BigIntegerField(default=9796959493, validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AddField(
            model_name='pancard',
            name='fName',
            field=models.CharField(default='abcd', max_length=50),
        ),
        migrations.AddField(
            model_name='pancard',
            name='lName',
            field=models.CharField(default='pqrs', max_length=50),
        ),
        migrations.AddField(
            model_name='pancard',
            name='mName',
            field=models.CharField(default='xyz', max_length=50),
        ),
        migrations.AddField(
            model_name='pancardq',
            name='DOB',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='ration',
            name='fName',
            field=models.CharField(default='abcd', max_length=50),
        ),
        migrations.AddField(
            model_name='ration',
            name='lName',
            field=models.CharField(default='pqrs', max_length=50),
        ),
        migrations.AddField(
            model_name='ration',
            name='mName',
            field=models.CharField(default='xyz', max_length=50),
        ),
        migrations.AddField(
            model_name='rationq',
            name='DOB',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='voterid',
            name='fName',
            field=models.CharField(default='abcd', max_length=50),
        ),
        migrations.AddField(
            model_name='voterid',
            name='lName',
            field=models.CharField(default='pqrs', max_length=50),
        ),
        migrations.AddField(
            model_name='voterid',
            name='mName',
            field=models.CharField(default='xyz', max_length=50),
        ),
        migrations.AddField(
            model_name='voteridq',
            name='DOB',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='voteridq',
            name='FathersName',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='voteridq',
            name='Sex',
            field=models.CharField(default='male', max_length=6),
        ),
        migrations.AlterField(
            model_name='ration',
            name='dealersName',
            field=models.CharField(max_length=100),
        ),
    ]
