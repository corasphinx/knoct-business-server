# Generated by Django 3.2.10 on 2021-12-16 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211216_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='enterprise',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_enterprise', to='users.enterprise'),
        ),
        migrations.AlterField(
            model_name='user',
            name='privilege',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_privilege', to='users.privilege'),
        ),
    ]
