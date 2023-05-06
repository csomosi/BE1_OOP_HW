class SpaceShip:
    fuel: int = 400
    passengers: list = ["John", "Steve", "Sam", "Danielle"]
    shields: bool = True
    speedometer: int = 0

    def __init__(self):
        pass

    def list_passengers(self):
        for p_name in self.passengers:
            print(f"Passanger: {p_name}")

    def add_passenger(self, new_passenger: str):
        self.passengers.append(new_passenger)
        print(f"{new_passenger} was added to the ship")

    def turnoff_shield(self):
        self.shields = False
        print("Fuel is low, turning off shields...")

    def info(self, speedometer, fuel):
        print(
            f"the SpaceShip is at: {speedometer}\nthe spaceship has: {fuel} fuel"
        )

    def travel(self, distance: int):
        print(f"trying to travel: {distance}")
        # if fuel is 0:
        if self.fuel == 0:
            print("can not go further, tank is empty")

        # we have fuel, but less than we need:
        elif distance > self.fuel * 2:
            print(f"can not go {distance}, can only travel: {self.fuel*2}")
            self.speedometer = self.speedometer + self.fuel * 2
            if self.shields == True:
                self.turnoff_shield()
            else:
                pass

            self.fuel = 0
            self.info(self.speedometer, self.fuel)

        # everything is okay:

        else:
            print(f"travelled {distance}")
            self.fuel = self.fuel - int(distance / 2)
            if self.fuel < 30:
                self.turnoff_shield()
            else:
                pass
            self.speedometer = self.speedometer + distance
            self.info(self.speedometer, self.fuel)


mySpaceShip = SpaceShip()

mySpaceShip = SpaceShip()
mySpaceShip.list_passengers()
mySpaceShip.add_passenger('Lindsay')
mySpaceShip.list_passengers()
mySpaceShip.travel(750)
mySpaceShip.travel(200)
mySpaceShip.travel(100)
