# Generated by Django 2.2.5 on 2019-10-17 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("franchises", "0002_historicaldomain")]

    operations = [
        migrations.AddField(
            model_name="plan",
            name="description",
            field=models.CharField(
                blank=True, max_length=1000, null=True, verbose_name="descripción"
            ),
        ),
        migrations.AlterField(
            model_name="plan",
            name="max_users",
            field=models.PositiveIntegerField(verbose_name="máximo de usuarios"),
        ),
        migrations.AlterField(
            model_name="plan",
            name="modules",
            field=models.ManyToManyField(
                to="franchises.Module", verbose_name="modulos"
            ),
        ),
        migrations.AlterField(
            model_name="plan",
            name="name",
            field=models.CharField(max_length=100, verbose_name="nombre"),
        ),
        migrations.AlterField(
            model_name="plan",
            name="price",
            field=models.PositiveIntegerField(verbose_name="precio"),
        ),
    ]