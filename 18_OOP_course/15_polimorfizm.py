class Room:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = x * y

    def __add__(self, obj):
        if isinstance(obj, Room):
            return self.area + obj.area

    def __eq__(self, obj):
        if isinstance(obj, Room):
            return self.area == obj.area



r1 = Room(3, 7)
r2 = Room(4, 10)