# Generated by Django 2.2.6 on 2019-12-05 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('tipo_prodcuto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Tipo_producto')),
            ],
        ),
    ]
