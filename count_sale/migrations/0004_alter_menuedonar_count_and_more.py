# Generated by Django 4.1.1 on 2023-01-12 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('count_sale', '0003_alter_menuedonar_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuedonar',
            name='count',
            field=models.CharField(max_length=2, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='menuedonar',
            name='menue_choices',
            field=models.CharField(choices=[('stud', 'Студенческая шаурма'), ('classic', 'Классическая шаурма'), ('chees', 'Сырная шаурма'), ('big', 'Большая шаурма'), ('vegan', 'Вегатарианская шаурма'), ('danar', 'Данар'), ('clousepizza', 'Закрытая пицца'), ('shaurmitto', 'Шаурмитто'), ('hot-dog', 'Хот-дог'), ('hot-dog_lavash', 'Хот-дог в лаваше'), ('double_hot-dog_lavash', 'Двойной хот-дог в лаваше'), ('hot-dog_meat', 'Хот-дог с мясом'), ('samsa', 'Самса'), ('bastella', 'Бастелла'), ('tandyr', 'Лепешки тандырные '), ('chees_add', 'Сыр'), ('halapenio', 'Халапеньо'), ('tea', 'Чай'), ('coffe', 'Кофе'), ('coffe_3_in_1', 'Кофе 3 в 1')], max_length=50, verbose_name='Товары'),
        ),
    ]
