# class User:
#     def __init__(self, user_id, user_name, followers=0, following=0):
#         self.user_id = user_id
#         self.user_name = user_name
#         self.followers = followers
#         self.following = following
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
#
# user_1 = User("001", "Anurag")
# user_2=User("002", "Golu")
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)
#
# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)


class Car:
    def __init__(self, make, model, manufacturing_year, mileage):
        self.make = make
        self.model = model
        self.manufacturing_year = manufacturing_year
        self.mileage = mileage

    def display_info(self):
        print(f"Make is {self.make}, Model is {self.model}, "
              f"Manufactured in year {self.manufacturing_year} and mileage: {self.mileage}")


my_car = Car("Toyota", "Corolla", "2020", 15000)
my_car.display_info()
