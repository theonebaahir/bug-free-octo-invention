class BMW:
    def start_engine(self):
        print("BMW engine started with a roar!")

    def top_speed(self):
        print("BMW top speed: 250 km/h")

class Ferrari:
    def start_engine(self):
        print("Ferrari engine started with a vroom!")

    def top_speed(self):
        print("Ferrari top speed: 340 km/h")

# Function demonstrating polymorphism
def test_car(car):
    car.start_engine()
    car.top_speed()
    print("------------------")

# Create objects
bmw_car = BMW()
ferrari_car = Ferrari()

# Use the same function for different classes
test_car(bmw_car)
test_car(ferrari_car)
