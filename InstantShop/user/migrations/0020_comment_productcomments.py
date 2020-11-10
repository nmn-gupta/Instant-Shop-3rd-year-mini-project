# Generated by Django 3.0.7 on 2020-11-02 05:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0019_delete_productcomments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_comment', models.DateField(default=datetime.datetime.today)),
                ('comment', models.TextField()),
                ('comment_done_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ManyToManyField(to='user.Comment')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Products')),
            ],
        ),
    ]