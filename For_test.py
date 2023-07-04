class Point:
    MIN = 0
    MAX = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_attr(self, x, y):
        if self.MIN <= x <= self.MAX:
            self.x = x
            self.y = y

    def __getattribute__(self, item):
        if item == 'x':
            raise ValueError("Доступ запрещен")
        else:
            print("__getattribute__")
            return object.__getattribute__(self, item)
    def __setattr__(self, key, value):
        if key =='z':
            raise AttributeError("недопустимое имя атрибута")
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        print("__delattr__:"+ item)
        object.__delattr__(self, item)




pt1 = Point(10, 20)
pt2 = Point(1, 2)
print(pt1.yy)
