class Car:
    def __init__(self, model: str, year: int, price: float):
        self.model = model
        self.year = year
        self.price = price

    def __str__(self):
        return f"Model: {self.model}; Year: {self.year}; Price: {self.price} UAH"

    @property
    def car_type(self):
        if self.price > 10_000_000:
            return "елітне"
        elif 2_000_000 <= self.price <= 10_000_000:
            return "середнячок"
        else:
            return "економ"

    def drive(self, distance: float):
        cost_of_trip = distance * 10
        if cost_of_trip <= self.price:
            self.price -= cost_of_trip
            print(f"The trip cost {cost_of_trip} UAH. Now the car's price is {self.price} UAH.")
        else:
            print("Not enough money for the trip!")


def create_car(model, year, price):
    return Car(model, year, price)


car1 = create_car("Toyota", 2022, 15000000)
car2 = create_car("Honda", 2015, 3000000)
car3 = create_car("Lada", 2005, 100000)

print(car1)
print(car2)
print(car3)
print(car1.car_type)
car1.drive(1000000)
car2.drive(200)
car3.drive(50)
car1.drive(400000)
print(car1.car_type)
print(car2.car_type)
print(car3.car_type)
