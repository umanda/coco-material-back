# Generated by Django 4.2.3 on 2023-07-18 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vectors', '0016_setup_simple_unaccent'),
    ]

    operations = [
        migrations.AddField(
            model_name='vector',
            name='colored_gif',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='vector',
            name='gif',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='vector',
            name='svg',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddConstraint(
            model_name='vector',
            constraint=models.CheckConstraint(check=models.Q(('svg__isnull', False), ('colored_svg__isnull', False), ('gif__isnull', False), ('colored_gif__isnull', False), _connector='OR'), name='vector_should_have_some_file'),
        ),
    ]
