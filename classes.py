class Cat:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def getName(self):
        return self.name

    def getSex(self):
        return self.sex

    def getAge(self):
        return self.age


class Circle:
    pi = 3.1415

    def __init__(self, r):
        self.r = r

    def setRadius(self, r):
        self.r = r

    def getRadius(self):
        return self.r

    def get_area_circle(self):
        return self.pi * self.r ** 2


class Rectangle:
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth

    def getWidth(self):
        return self.width

    def getHeigth(self):
        return self.heigth

    def getArea(self):
        return self.width * self.heigth


class Square:
    def __init__(self, w_h):
        self.w_h = w_h

    def getA(self):
        return self.w_h

    def getAreaSquare(self):
        return self.w_h ** 2
