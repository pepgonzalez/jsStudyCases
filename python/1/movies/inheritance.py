class Parent():
    def __init__(self, last_name, eye_color):
        print("parent constructor")
        self.last_name = last_name
        self.eye_color = eye_color

class Child(Parent):
    def __init__(self, last_name, eye_color, toys):
        print("child constructor")
        Parent.__init__(self, last_name, eye_color)
        self.toys = toys
        
parent = Parent("Gzz", "brown")
child = Child("Gzz", "green", 1)
print(child.last_name)

