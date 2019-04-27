# Generated by Django 2.0.6 on 2019-04-27 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('meta_ano', models.TextField()),
                ('meta_acum', models.TextField()),
                ('real_acum', models.TextField()),
                ('percent_ating', models.TextField()),
                ('atingido_ano', models.TextField()),
                ('farol', models.TextField()),
                ('qt_salarios', models.TextField()),
                ('obs', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('publicador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
