class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!!"

class Cat(Animal):
    def speak(self):
        return "Meow!!"

dog=Dog("Buddy")
cat=Cat("Whiskers")
print(f"{dog.name} says: {dog.speak()}")
print(f"{cat.name} says: {cat.speak()}")


class Payment:
    def __init__(self,mode):
        self.mode=mode
    def app(self):
        pass
class GPay(Payment):
    def app(self):
        print("Speaking to Google Payment Gateway")
class PhonePay(Payment):
    def app(self):
        print("Speaking to PhonePay Payment Gateway")
class AmazonPay(Payment):
    def app(self):
        print("Speaking to Amazon Payment Gateway")

gp=GPay("GooglePay")
pp=PhonePay("PhonePay")
ap=AmazonPay("AmazonPay")
gp.app()
pp.app()
ap.app()