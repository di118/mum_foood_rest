# Generated by Django 2.2.5 on 2019-09-02 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ingredient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('description', models.TextField()),
                ('vegan', models.BooleanField(default=False)),
                ('vegetarian', models.BooleanField(default=False)),
                ('likes', models.IntegerField()),
                ('ingredients', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ingredient.Ingredient')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
