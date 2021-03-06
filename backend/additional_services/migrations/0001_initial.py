# Generated by Django 2.1.2 on 2019-01-02 16:42

from django.db import migrations, models
import django.db.models.deletion
import localized_fields.fields.field


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', localized_fields.fields.field.LocalizedField(required=['en'], uniqueness=[], verbose_name='display name')),
                ('short_name', localized_fields.fields.field.LocalizedField(required=['en'], uniqueness=[], verbose_name='short name')),
                ('website', localized_fields.fields.field.LocalizedField(required=['en'], uniqueness=[], verbose_name='website')),
                ('logo', models.ImageField(upload_to='additional_services/providers/logos/%Y/%m/%d/', verbose_name='logo')),
            ],
            options={
                'ordering': ('display_name',),
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', localized_fields.fields.field.LocalizedField(required=['en'], uniqueness=[], verbose_name='display name')),
                ('short_description', localized_fields.fields.field.LocalizedField(required=['en'], uniqueness=[], verbose_name='short description')),
            ],
            options={
                'ordering': ('display_name',),
            },
        ),
        migrations.CreateModel(
            name='SubscriptionType',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('display_name', localized_fields.fields.field.LocalizedField(required=['en'], uniqueness=[], verbose_name='display name')),
            ],
        ),
        migrations.CreateModel(
            name='UserServiceSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribed_at', models.DateTimeField(auto_now_add=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_subscriptions', to='additional_services.Service')),
            ],
        ),
    ]
