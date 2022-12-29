class MyTemplate():
    class_object_attribute1 = 6378137
    class_object_attribute2 = 6356752 
    def __init__(self, attribute1: str, attribute2: bool) -> None:
        print("Constructor ran")
        self.attr1 = attribute1
        self.attr2 = attribute2
    def my_method1(self):
        if self.attr2:
            print(f"Good morning {self.attr1}")
        else:
            print(f"No greeting {self.attr1}")
    def my_method2(self,my_name:str):
        if self.attr2:
            print(f"Good morning {my_name}")
        else:
            print(f"No greeting {my_name}")

my_object = MyTemplate("John", True)
my_object.my_method1()
my_object.my_method2('Luffy')
print(my_object.class_object_attribute1, my_object.class_object_attribute2)


