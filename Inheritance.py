

class Parent:
    def display(self):
        print("Hey Everyone")
        

class Child(Parent):
    def display(self):
        print("Hay Yash GM")
        
class GrandChild(Parent):
    def display(self):
        print("Hay Shreyash GM")

g1=GrandChild()
g1.display()
