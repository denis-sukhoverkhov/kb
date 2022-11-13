from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.checkins = {}
        self.times_for_stations = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = {"stationName": stationName, 't': t}

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkin_stricture = self.checkins[id]

        self.times_for_stations[
            (checkin_stricture['stationName'], stationName)].append(t-checkin_stricture['t'])

        del self.checkins[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        summ = sum(self.times_for_stations[(startStation, endStation)])
        ct_elements = len(self.times_for_stations[(startStation, endStation)])
        return round(summ / ct_elements, 5)


if __name__ == "__main__":
    undergroundSystem = UndergroundSystem()
    undergroundSystem.checkIn(45, "Leyton", 3)
    undergroundSystem.checkIn(32, "Paradise", 8)
    undergroundSystem.checkIn(27, "Leyton", 10)
    undergroundSystem.checkOut(45, "Waterloo", 15)
    undergroundSystem.checkOut(27, "Waterloo", 20)
    undergroundSystem.checkOut(32, "Cambridge", 22)
    assert undergroundSystem.getAverageTime("Paradise", "Cambridge") == 14.00000
    assert undergroundSystem.getAverageTime("Leyton", "Waterloo") == 11.00000
    undergroundSystem.checkIn(10, "Leyton", 24)
    assert undergroundSystem.getAverageTime("Leyton", "Waterloo") == 11.00000
    undergroundSystem.checkOut(10, "Waterloo", 38)
    assert undergroundSystem.getAverageTime("Leyton", "Waterloo") == 12.00000

    undergroundSystem = UndergroundSystem()
    undergroundSystem.checkIn(10, "Leyton", 3)
    undergroundSystem.checkOut(10, "Paradise", 8)
    assert undergroundSystem.getAverageTime("Leyton", "Paradise") == 5.00000
    undergroundSystem.checkIn(5, "Leyton", 10)
    undergroundSystem.checkOut(5, "Paradise", 16)
    assert undergroundSystem.getAverageTime("Leyton", "Paradise") == 5.5
    undergroundSystem.checkIn(2, "Leyton", 21)
    undergroundSystem.checkOut(2, "Paradise", 30)
    assert undergroundSystem.getAverageTime("Leyton", "Paradise") == 6.66667
