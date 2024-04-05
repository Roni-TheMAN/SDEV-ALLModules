# Program: Car Info MAker
# Name: Ronit Patel
# Date: 2024-04-05
# Description: This program will take the car type and other infos and presents it.
class car_type:
    def __init__(self, car_type):
        self.car_type = car_type


class car_info(car_type):
    def __init__(self, car_make, car_model, car_doors, car_roof, car_type):
        super().__init__(car_type)
        self.car_make = car_make
        self.car_model = car_model
        self.car_doors = car_doors
        self.car_roof = car_roof

    def car_info_p(self):
        print("vehicleType: " + self.car_type)
        print("vehicleMake: " + self.car_make)
        print("vehicleModel: " + self.car_model)
        print("vehicle Doors: " + self.car_doors)
        print("vehicle Roof: " + self.car_roof)


car_type_info = input("Enter Vehicle Type(car, truck, plane, boat, broomstick): ")
car_make_info = input("Enter vehicle Make: ")
car_model_info = input("Enter vehicle Model: ")
car_doors_info = input("Enter vehicle Doors(2 or 4): ")
car_roof_info = input("Enter vehicle Roof(Solid or SunRoof): ")

car = car_info(car_make_info, car_model_info, car_doors_info, car_roof_info, car_type_info)

car.car_info_p()
