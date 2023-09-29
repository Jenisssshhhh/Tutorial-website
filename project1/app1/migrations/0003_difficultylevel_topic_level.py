# Generated by Django 4.2.2 on 2023-07-19 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_remove_useraccount_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Difficultylevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='topic',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.difficultylevel'),
        ),
    ]
