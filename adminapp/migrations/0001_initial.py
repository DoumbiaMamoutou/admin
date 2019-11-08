# Generated by Django 2.2.7 on 2019-11-08 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='categorie/%Y/%m/%d/')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tague',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('status', models.BooleanField(default=False)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SousCategrorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='souscategorie/%Y/%m/%d/')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('categorie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorie', to='adminapp.Categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='produit/%Y/%m/%d/')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('souscategorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produit_souscategorie', to='adminapp.SousCategrorie')),
                ('tague', models.ManyToManyField(related_name='produit_tag', to='adminapp.Tague')),
            ],
        ),
    ]
