from django.db import models

class MenueDonar(models.Model):

    menue_item = [
        ('stud', 'Студенческая шаурма'),
        ('classic', 'Классическая шаурма'),
        ('chees', 'Сырная шаурма'),
        ('big', 'Большая шаурма'),
        ('vegan', 'Вегетарианская шаурма'),
        ('danar', 'Данар'),
        ('clousepizza', 'Закрытая пицца'),
        ('shaurmitto', 'Шаурмитто'),
        ('hot-dog', 'Хот-дог'),
        ('hot-dog_lavash', 'Хот-дог в лаваше'),
        ('double_hot-dog_lavash', 'Двойной хот-дог в лаваше'),
        ('hot-dog_meat', 'Хот-дог с мясом'),
        ('samsa', 'Самса'),
        ('bastella', 'Бастелла'),
        ('tandyr', 'Лепешки тандырные '),
        ('chees_add', 'Сыр'),
        ('halapenio', 'Халапеньо'),
        ('tea', 'Чай'),
        ('coffe', 'Кофе'),
        ('coffe_3_in_1', 'Кофе 3 в 1'),
    ]



    date_sale = models.DateTimeField(verbose_name = "Дата", auto_now = True)
    count = models.CharField(verbose_name = "Количество", max_length = 2)
    menue_choices = models.CharField(verbose_name = "Товары", choices = menue_item, max_length = 50)
    

    def __str__(self):
        return self.count + " " + self.menue_choices 
