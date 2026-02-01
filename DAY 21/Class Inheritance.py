''' Inheritance lets you create a new class (called a child or derived class) based on an existing class (called a parent or base class).
This helps you reuse code and extend functionality without rewriting everything. '''
class Animal:
    def __init__(self):
        self.num_eyes = 2
    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__() # Call parent constructor
    def breathe(self):
        super().breathe()
        print("doing this underwater. ")
    def swim(self):
        print("Moving in water.")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
