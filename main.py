from classes import Cat, Circle

cats = [{"name": "Барон", "sex": "мальчик", "age": 2}, {"name": "Сэм", "sex": "мальчик", "age": 2}]

for cat in cats:
    obj_cat = Cat(name=cat.get("name"), sex=cat.get("sex"), age=cat.get("age"))
    print(obj_cat.getName(), obj_cat.getSex(), obj_cat.getAge())

c1 = Circle(5)
print("Площадь окружности с радиусом {} равна {}".format(c1.getRadius(), c1.get_area_circle()))
c1.setRadius(8)
print("Площадь окружности с радиусом {} равна {}".format(c1.getRadius(), c1.get_area_circle()))