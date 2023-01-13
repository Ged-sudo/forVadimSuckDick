import requests
import json

#data_now = str(input("Введите дату, по которой нужен отчет (формат  - 2023-01-12 если это день, а если нужен отчет за месяц то - 2023-01): "))

url = "http://127.0.0.1:8000/api/get_info_sales/"

def needed_info():
    info = requests.get(url)

    serialised_info = json.loads(info.text)

    all_items = serialised_info['Info - ']

    all_marga = 0

    marg_items = {
        'stud': [0, 0],
        'classic': [0, 0],
        'chees': [0, 0],
        'big': [0, 0],
        'vegan': [0, 0],
        'danar': [0, 0],
        'clousepizza': [0, 0],
        'shaurmitto': [0, 0],
        'hot-dog': [0, 0],
        'hot-dog_lavash': [0, 0],
        'double_hot-dog_lavash': [0, 0],
        'hot-dog_meat': [0, 0],
        'samsa': [0, 0],
        'bastella': [0, 0],
        'tandyr': [0, 0],
        'chees_add': [0, 0],
        'halapenio': [0, 0],
        'tea': [0, 0],
        'coffe': [0, 0],
        'coffe_3_in_1': [0, 0]
    }

    menue_item_cost = {
        'stud': 140,
        'classic': 180,
        'chees': 180,
        'big': 230,
        'vegan': 100,
        'danar': 160,
        'clousepizza': 160,
        'shaurmitto': 160,
        'hot-dog': 110,
        'hot-dog_lavash': 120,
        'double_hot-dog_lavash': 140,
        'hot-dog_meat': 120,
        'samsa': 90,
        'bastella': 90,
        'tandyr': 40,
        'chees_add': 20,
        'halapenio': 10,
        'tea': 25,
        'coffe': 30,
        'coffe_3_in_1': 35
    }

    menue_item = {
        'stud': 'Студенческая шаурма',
        'classic': 'Классическая шаурма',
        'chees': 'Сырная шаурма',
        'big': 'Большая шаурма',
        'vegan': 'Вегетарианская шаурма',
        'danar': 'Данар',
        'clousepizza': 'Закрытая пицца',
        'shaurmitto': 'Шаурмитто',
        'hot-dog': 'Хот-дог',
        'hot-dog_lavash': 'Хот-дог в лаваше',
        'double_hot-dog_lavash': 'Двойной хот-дог в лаваше',
        'hot-dog_meat': 'Хот-дог с мясом',
        'samsa': "Самса",
        'bastella': "Бастелла",
        'tandyr': "Лепешки тандырные",
        'chees_add': 'Сыр',
        'halapenio': 'Халапеньо',
        'tea': 'Чай',
        'coffe': 'Кофе',
        'coffe_3_in_1': 'Кофе 3 в 1',
    }

    for item in all_items:
        #print(item['pk'], '\n', item['menue_choices'], '\n', item['count'])
        #if item["date_sale"].startswith(data_now):
        all_marga = all_marga + menue_item_cost.get(item['menue_choices']) * int(item['count'])
        marg_items[item['menue_choices']][0] = marg_items[item['menue_choices']][0] + menue_item_cost.get(item['menue_choices']) * int(item['count'])
        marg_items[item['menue_choices']][1] = marg_items[item['menue_choices']][1] + int(item['count'])
    
    line = ""

    # with open("otchet.txt", 'w') as file:
    #     for item in menue_item:
    #         line = menue_item[item] + " || было продано на  - " + str(marg_items[item][0]) + ",|| количество - " + str(marg_items[item][1]) + "\n"
    #         file.writelines(line)
        
        
    #     all_marg_line = f"Всего было продано {all_marga}"

    #     file.writelines("\n")
    #     file.writelines(all_marg_line)
    
    return all_marga




