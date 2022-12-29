
class JORzClass():
 def __init__(self, my_greeting):
    print("Running constructor for JORzClass")
    self.message = my_greeting
 def my_method(self):
    print(self.message)

my_class1 = JORzClass("Morning JOR!")
my_class1.my_method()
print(type(my_class1))

my_class2= JORzClass("Evening LUFFY!")
my_class2.my_method()
print(type(my_class2))