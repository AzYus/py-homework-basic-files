file_name='recipes.txt'

def read_txt(file_Name):
    with open(file_Name, 'r', encoding='utf 8') as file_menu:
        menu = {}
        for line in file_menu:
            dish_name=line[:-1]
            count_line = file_menu.readline().strip()
            list_ing=[]
            for i in range(int(count_line)):
                dish_items = dict.fromkeys(['ingredient_name', 'quantity', 'measure'])  # временный словарь
                ingridient = file_menu.readline().strip().split(' | ')  # перемещение по файлу
                for item in ingridient:
                    dish_items['ingredient_name'] = ingridient[0]
                    dish_items['quantity'] = ingridient[1]
                    dish_items['measure'] = ingridient[2]
                list_ing.append(dish_items)
                cook_book={dish_name : list_ing}
                menu.update(cook_book)
            file_menu.readline()
    return (menu)


def get_shop_list_by_dishes(dishes, person_count=int):
    menu=read_txt(file_name)
    order_list={}
    try:
        for dish in dishes:
            for item in menu[dish]:
                items_list = dict([(item['ingredient_name'], {'measure': item['measure'], 'quantity': int(item['quantity']) * person_count})])
                order_list.update(items_list)
        print(order_list)
    except KeyError:
        print("Проверьте ввод")



get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)