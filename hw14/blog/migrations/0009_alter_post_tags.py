# Generated by Django 5.1.2 on 2024-11-27 14:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0008_tag_post_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(blank=True, to="blog.tag"),
        ),
    ]