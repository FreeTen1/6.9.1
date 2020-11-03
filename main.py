from classes import Cat

cats = [{"name": "Барон", "sex": "мальчик", "age": 2}, {"name": "Сэм", "sex": "мальчик", "age": 2}]

for cat in cats:
    obj_cat = Cat(name=cat.get("name"), sex=cat.get("sex"), age=cat.get("age"))
    print(obj_cat.getName(), obj_cat.getSex(), obj_cat.getAge())
