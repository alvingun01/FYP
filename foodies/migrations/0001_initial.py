# Generated by Django 4.1 on 2022-10-17 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Menu",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("price", models.FloatField()),
                ("hot", models.BooleanField()),
                ("category", models.CharField(max_length=100)),
                ("peanut", models.BooleanField(default=False)),
                ("shrimp", models.BooleanField(default=False)),
                ("lactose", models.BooleanField(default=False)),
                ("halal", models.BooleanField(default=False)),
                ("vegetarian", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("table_no", models.IntegerField()),
                ("telp_no", models.CharField(max_length=14)),
                ("paid", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Stall",
            fields=[("id", models.AutoField(primary_key=True, serialize=False)),],
        ),
        migrations.CreateModel(
            name="OrderStall",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "order_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="foodies.order"
                    ),
                ),
                (
                    "stall_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="foodies.stall"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderMenu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField()),
                (
                    "menu_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="foodies.menu"
                    ),
                ),
                (
                    "order_stall_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="foodies.orderstall",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="menu",
            name="stall_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="foodies.stall"
            ),
        ),
    ]