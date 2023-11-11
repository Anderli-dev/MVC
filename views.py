from models import Vehicle


def AllView(vehicles: [Vehicle]):
    for vehicle in vehicles:
        print("Hull: " + vehicle.hull + ", Wheels: " + str(vehicle.wheels) + ", Engine: " + vehicle.engine)


def CarView(cars: [Vehicle]):
    for car in cars:
        print("Wheels: " + str(car.wheels) + ", Engine: " + car.engine)


def PlaneView(planes: [Vehicle]):
    for plane in planes:
        print("Wheels: " + str(plane.wheels) + ", Engine: " + plane.engine)


def BoatView(boats: [Vehicle]):
    for boat in boats:
        print("Wheels: " + str(boat.wheels) + ", Engine: " + boat.engine)
