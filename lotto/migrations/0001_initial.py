# Generated by Django 2.2.6 on 2020-02-11 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuessNumbers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('text', models.CharField(max_length=255)),
                ('lottos', models.CharField(default='[1, 2, 3, 4, 5, 6]', max_length=255)),
                ('num_lotto', models.IntegerField(default=5)),
                ('update_date', models.DateTimeField()),
            ],
        ),
    ]