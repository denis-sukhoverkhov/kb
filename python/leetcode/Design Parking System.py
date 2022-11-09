from enum import Enum


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.max_places_by_car_type = {
            1: big,
            2: medium,
            3: small,
        }

        self.taken_places_by_car_type = {i: 0 for i, v in self.max_places_by_car_type.items()}

    def has_available_places(self, carType: int):
        return self.max_places_by_car_type[carType] - self.taken_places_by_car_type[carType] > 0

    def addCar(self, carType: int) -> bool:
        if self.has_available_places(carType):
            self.taken_places_by_car_type[carType] += 1
            return True

        return False


if __name__ == "__main__":
    parkingSystem = ParkingSystem(1, 1, 0)
    assert parkingSystem.addCar(1) is True
    assert parkingSystem.addCar(2) is True
    assert parkingSystem.addCar(3) is False
    assert parkingSystem.addCar(1) is False
