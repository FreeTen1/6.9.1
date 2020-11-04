from classes import Cat, Circle, Rectangle, Square

cats = [{"name": "Барон", "sex": "мальчик", "age": 2}, {"name": "Сэм", "sex": "мальчик", "age": 2}]

for cat in cats:
    obj_cat = Cat(name=cat.get("name"), sex=cat.get("sex"), age=cat.get("age"))
    print(obj_cat.getName(), obj_cat.getSex(), obj_cat.getAge())
print()
r1, r2 = Rectangle(10, 5), Rectangle(12, 5)
sq1, sq2 = Square(5), Square(7)
c1, c2 = Circle(5), Circle(8)
figures = [r1, r2, sq1, sq2, c1, c2]

for figure in figures:
    if isinstance(figure, Circle):
        print(
            "Площадь окружности с радиусом {} равна {}".format(figure.getRadius(), round(figure.get_area_circle(), 4)))
    elif isinstance(figure, Square):
        print("Площадь квадрата со стороной {} равна {}".format(figure.getA(), figure.getAreaSquare()))
    else:
        print("Площадь прямоугольника с шириной {}, высотой {} равна {}".format(figure.getWidth(), figure.getHeigth(),
                                                                                figure.getArea()))
