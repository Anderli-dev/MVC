

class Vehicle:
    def __init__(self, hull: str, wheels: int, engine: str):
        self.hull = hull
        self.wheels = wheels
        self.engine = engine

    @classmethod
    def getAll(self):
        database = open('db.txt', 'r')
        result = []
        for item in database:
            vehicle = Vehicle(item.split("|")[0], int(item.split("|")[1]), item.split("|")[2])
            result.append(vehicle)
        return result

