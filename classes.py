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
    pi = 3.14

    def __init__(self, r):
        self.r = r

    def setRadius(self, r):
        self.r = r

    def getRadius(self):
        return self.r

    def get_area_circle(self):
        return self.pi * self.r ** 2
