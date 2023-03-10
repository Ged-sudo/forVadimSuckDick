# Generated by Django 4.1.1 on 2023-01-12 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenueDonar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.TextField(max_length=2, verbose_name='count_item')),
                ('menue_choices', models.CharField(choices=[('stud', 'Студенческая шаурма'), ('classic', 'Классическая шаурма'), ('chees', 'Сырная шаурма'), ('big', 'Большая шаурма'), ('vegan', 'Вегатарианская шаурма'), ('danar', 'Данар'), ('clousepizza', 'Закрытая пицца'), ('shaurmitto', 'Шаурмитто'), ('hot-dog', 'Хот-дог'), ('hot-dog_lavash', 'Хот-дог в лаваше'), ('double_hot-dog_lavash', 'Двойной хот-дог в лаваше'), ('hot-dog_meat', 'Хот-дог с мясом'), ('samsa', 'Самса'), ('bastella', 'Бастелла'), ('tandyr', 'Лепешки тандырные '), ('chees_add', 'Сыр'), ('halapenio', 'Халапеньо'), ('tea', 'Чай'), ('coffe', 'Кофе'), ('coffe_3_in_1', 'Кофе 3 в 1')], max_length=50, verbose_name='menue_choices')),
            ],
        ),
    ]
