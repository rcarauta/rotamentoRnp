# Generated by Django 2.2.6 on 2019-10-20 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='No',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origem', models.CharField(max_length=100)),
                ('peso', models.IntegerField()),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rotas.No')),
            ],
        ),
    ]
