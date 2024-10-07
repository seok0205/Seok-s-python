class Person:
    def __init__(self, age, name, gender):
        while 1:
            if gender != 'male' and gender != 'female':
                print("incorrect. write 'male' or 'female'.")
                gender = input("gender: ")
            elif gender == 'male' or gender == 'female':
                break
        self.name = name
        self.gender = gender
        self.age = age

    def display(self):
        print(f"name: {self.name}, gender: {self.gender}")
        print(f"age: {self.age}")
        
    def greet(self):
        if int(self.age) > 19:
            print(f"Hi, {self.name}! You're adult!")
        else:
            print(f"Hi, {self.name}! Where are your parents?")

a = input("age: ")
b = input("name: ")
c = input("gender: ")

someone = Person(a, b, c)

someone.display()
someone.greet()