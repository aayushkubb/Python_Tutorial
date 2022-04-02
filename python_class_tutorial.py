# Create a class representing a person and then deffine attributes


class Person:

    #Initialize few variable
    def __init__(self, name, age):
        self.name=name
        self.age=age

    #custom function speaks
    def   speak(self):
        print("Hello my name is ",self.name)
        print("Hello my age is ",self.age)

name=input("Please enter your name")
age=input("Please enter your age")
# aay - object
# Person is the class
aay=Person(name,age)
aay.speak()