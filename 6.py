
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print("Restaurant name:", self.restaurant_name)
        print("Cuisine type:", self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name," is open")

class User:
    def __init__(self,first_name,last_name,user_name,email_address):
        self.first_name=first_name
        self.last_name=last_name
        self.user_name=user_name
        self.email_address=email_address

    def describe_user(self):
        print("First name",self.first_name)
        print("Last name:",self.last_name)
        print("Username:",self.user_name)
        print("Email address:",self.email_address)

    def greet_user(self):
        print("Hello ",self.user_name)

def main():
   
   restaurant1=Restaurant("Jo's diner","American")
   restaurant2=Restaurant("Back to The Earth","Vegan,Organic")
   restaurant3=Restaurant("Bottomless","Buffet,Continental")

   restaurant1.describe_restaurant()
   restaurant1.open_restaurant()
   print("----------------")
   restaurant2.describe_restaurant()
   restaurant2.open_restaurant()
   print("----------------")
   restaurant3.describe_restaurant()
   restaurant3.open_restaurant()
   print("----------------")

   user1 = User("John","Doe", "johndoe", "john@gmail.com")
   user2 = User("Sarah","Smith","sarahsmith","sarah@gmail.com")
   user3 = User("Michael","Brown","michaelbrown","michael@gmail.com")

   user1.describe_user()
   user1.greet_user()

   print("----------------")

   user2.describe_user()
   user2.greet_user()

   print("----------------")

   user3.describe_user()
   user3.greet_user()

if __name__=="__main__":
   main()

    

