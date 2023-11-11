from views import *
from models import Vehicle


def showAll():
    vehicles = Vehicle.getAll()
    AllView(vehicles)


def showCars():
    vehicles = Vehicle.getAll()
    cars = [vehicle for vehicle in vehicles if vehicle.hull == "car"]
    CarView(cars)


def showBoats():
    vehicles = Vehicle.getAll()
    boats = [vehicle for vehicle in vehicles if vehicle.hull == "boat"]
    BoatView(boats)


def showPlanes():
    vehicles = Vehicle.getAll()
    planes = [vehicle for vehicle in vehicles if vehicle.hull == "plane"]
    PlaneView(planes)


if __name__ == "__main__":
    print("All vehicles")
    showAll()

    print("All cars")
    showCars()
