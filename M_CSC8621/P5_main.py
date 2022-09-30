import P5_car

def main():
    # Task 2
    Car_1 = P5_car.Car(1995, "volvo")
    for _ in range (5):
        Car_1.accelerate()
        Car_1.get_speed()
    for _ in range (5):
        Car_1.brake()
        Car_1.get_speed()

if __name__ == "__main__":
    main()