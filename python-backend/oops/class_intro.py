# class Car:

#     def __init__(self,wheel,engine,gear,head_light):
#         print(self)
#         self.wheel = wheel
#         self.engine = engine
#         self.gear= gear
#         self.head_light = head_light


# my_tata = Car("MRF","3 stroke","2","2")

# print(my_tata.wheel)
# print(my_tata.engine)


#  if you change self to this it will work but to understand in python we use self (mentain in python)

class Car:

    def __init__(this,wheel,engine,gear,head_light):
        print(this)
        this.wheel = wheel
        this.engine = engine
        this.gear= gear
        this.head_light = head_light


my_tata = Car("MRF","3 stroke","2","2")

print(my_tata.wheel)
print(my_tata.engine)