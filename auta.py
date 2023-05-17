print("Programowanie obiektowe")
class Car:
    pass
my_car= Car()
type(my_car)
print(my_car)
class Car:
    def __init__(self):
       pass
class Car:
    def __init__(self,make,model_name,top_speed,color):
        self.make = make
        self.model_name = model_name
        self.top_speed = top_speed
        self.color= color
mustang = Car(make="Ford",model_name="Mustang",top_speed=250,color="Yellow")
print(mustang.color)    