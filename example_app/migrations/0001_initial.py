# Generated by Django 3.0.2 on 2020-02-17 01:44

from django.db import migrations, models
import django.db.models.deletion
import example_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenderExample',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=50)),
                ('delete_flag', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            bases=(models.Model, example_app.models.GenericMethods),
        ),
        migrations.CreateModel(
            name='PersonExample',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.CharField(max_length=50, unique=True)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('delete_flag', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('gender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='example_app.GenderExample')),
            ],
            bases=(models.Model, example_app.models.GenericMethods),
        ),
    ]