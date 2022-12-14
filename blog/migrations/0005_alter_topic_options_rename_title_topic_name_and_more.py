# Generated by Django 4.1.2 on 2022-10-26 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_topic_alter_post_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.ManyToManyField(to='blog.topic'),
        ),
    ]
