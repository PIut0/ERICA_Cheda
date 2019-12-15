# Generated by Django 2.2.7 on 2019-12-14 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chedaapp', '0009_gumin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('for_whom', models.CharField(max_length=50)),
                ('l_field', models.CharField(choices=[('문화예술/가정', '문화예술/가정'), ('생활체육/건강', '생활체육/건강'), ('인문/사회', '인문/사회'), ('IT관련', 'IT관련'), ('자격증과정', '자격증과정'), ('일반', '일반')], max_length=10)),
                ('fee', models.IntegerField()),
                ('st_period', models.DateField()),
                ('fin_period', models.DateField()),
                ('date', models.TextField(max_length=200)),
                ('where', models.CharField(max_length=100)),
                ('to_st_date', models.DateTimeField()),
                ('to_fin_date', models.DateTimeField()),
                ('people', models.IntegerField()),
                ('how_apply', models.CharField(max_length=50)),
                ('ask', models.CharField(max_length=50)),
                ('etc', models.TextField(blank=True, null=True)),
            ],
        ),
    ]