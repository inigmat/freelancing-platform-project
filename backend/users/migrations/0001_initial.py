# Generated by Django 4.2.5 on 2023-10-02 06:59

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('is_customer', models.BooleanField(default=False)),
                ('is_worker', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Направление деятельности')),
                ('slug', models.SlugField(max_length=200, unique=True, validators=[django.core.validators.RegexValidator(message='Используйте допустимые символы!', regex='^[-a-zA-Z0-9_]+$')])),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Stack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Необходимый навык')),
                ('slug', models.SlugField(unique=True, validators=[django.core.validators.RegexValidator(message='Используйте допустимые символы!', regex='^[-a-zA-Z0-9_]+$')])),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='WorkerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='bio/images/', verbose_name='Фото')),
                ('payrate', models.IntegerField(default=0, verbose_name='Ставка оплаты')),
                ('about', models.TextField(blank=True, max_length=500, verbose_name='О себе')),
                ('diploma', models.FileField(blank=True, upload_to='', verbose_name='Дипломы, сертификаты, грамоты')),
                ('web', models.URLField(blank=True, verbose_name='Личный сайт')),
                ('activity', models.ManyToManyField(blank=True, to='users.activity', verbose_name='Специализация')),
                ('stacks', models.ManyToManyField(blank=True, to='users.stack', verbose_name='Навык')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='about/images/', verbose_name='Фото или логотип')),
                ('name', models.CharField(max_length=150, verbose_name='Название компании или ваше имя')),
                ('industry', models.CharField(max_length=255, verbose_name='Сфера деятельности')),
                ('web', models.URLField(blank=True, verbose_name='Личный сайт')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='stacks',
            field=models.ManyToManyField(blank=True, to='users.stack', verbose_name='Необходимый навык'),
        ),
    ]
