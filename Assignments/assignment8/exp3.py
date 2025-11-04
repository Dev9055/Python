class Car:
    def __init__(self,car_name,car_model,car_speed):
        self.car_name = car_name
        self.car_model = car_model
        self.car_speed = car_speed
    def accelerate(self):
        return self.car_speed + 70

    def brakes(self):
        return self.car_speed - 20
car_name=input("enter car name: ")
car_model=input("enter car model: ")
car_speed=int(input("enter car speed: "))

car=Car(car_name,car_model,car_speed)

result1=car.accelerate()
result2=car.brakes()

print("When the car accelerates,speed is {} ".format(result1))
print("Car brakes applied; speed is {} ".format(result2))





