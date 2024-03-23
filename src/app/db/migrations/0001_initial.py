# Generated by Django 5.0.3 on 2024-03-23 00:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.content')),
            ],
        ),
        migrations.CreateModel(
            name='PageItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_items', to='db.content')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='db.page')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tables', to='db.pageitem')),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='table',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='db.table'),
        ),
        migrations.CreateModel(
            name='TableRow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rows', to='db.table')),
            ],
        ),
        migrations.CreateModel(
            name='TableCell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('row', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cells', to='db.tablerow')),
            ],
        ),
    ]