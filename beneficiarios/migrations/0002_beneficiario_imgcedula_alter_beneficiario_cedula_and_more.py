# Generated by Django 5.0.1 on 2024-01-18 17:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asociados', '0001_initial'),
        ('beneficiarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiario',
            name='ImgCedula',
            field=models.FileField(blank=True, null=True, upload_to='cedula'),
        ),
        migrations.AlterField(
            model_name='beneficiario',
            name='cedula',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='beneficiario',
            name='parentesco',
            field=models.CharField(choices=[('MADRE', 'Madre'), ('PADRE', 'Padre'), ('HERMANO', 'Hermano'), ('HERMANA', 'Hermana'), ('ESPOSO', 'Esposo'), ('HIJO', 'Hijo'), ('HIJA', 'Hija'), ('SOBRINO', 'Sobrino'), ('SOBRINA', 'Sobrina')], max_length=40, verbose_name='Parentesco'),
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nomMascota', models.CharField(max_length=30, verbose_name='Nombre Mascota')),
                ('Raza', models.CharField(max_length=30, verbose_name='Raza')),
                ('añoNacimiento', models.DateField(verbose_name='Fecha Nacimiento')),
                ('fotoMascota', models.FileField(blank=True, null=True, upload_to='mascota')),
                ('ImgCarnet', models.FileField(blank=True, null=True, upload_to='carnet')),
                ('fkAsociado', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='asociados.asociado')),
            ],
            options={
                'verbose_name': 'Mascota',
                'verbose_name_plural': 'Mascotas',
                'ordering': ['pk'],
            },
        ),
    ]
