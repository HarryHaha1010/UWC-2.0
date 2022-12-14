# Generated by Django 4.1.3 on 2022-12-12 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='curr_status',
            field=models.CharField(choices=[('Chưa được giao nhiệm vụ', 'Chưa được giao nhiệm vụ'), ('Đã được giao nhiệm vụ', 'Đã được giao nhiệm vụ')], max_length=100),
        ),
        migrations.AlterField(
            model_name='mcp',
            name='curr_status',
            field=models.CharField(choices=[('Đang sử dụng', 'Đang sử dụng'), ('Đang trống', 'Đang trống')], max_length=20),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='curr_status',
            field=models.CharField(choices=[('Đang sử dụng', 'Đang sử dụng'), ('Đang trống', 'Đang trống')], max_length=20),
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('route', models.CharField(max_length=200)),
                ('MCP', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='src.mcp')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='src.vehicle')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='mission',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='src.mission'),
        ),
    ]
