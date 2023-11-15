# Generated by Django 4.2.3 on 2023-07-10 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0004_passwordresets'),
    ]

    operations = [
        migrations.CreateModel(
            name='Computers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('model', models.CharField(default='', max_length=100)),
                ('price', models.FloatField(default=0.0)),
                ('status', models.CharField(choices=[('Brand New', 'BRAND NEW'), ('Refurbished', 'REFURBISHED'), ('Used', 'USED')], default='Brand New', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='passwordresets',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='AmountPaid',
        ),
        migrations.DeleteModel(
            name='Levels',
        ),
        migrations.DeleteModel(
            name='PasswordResets',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]