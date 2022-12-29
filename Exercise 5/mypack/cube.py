cube_text = "Yo, time to cube stuff!"
def cube(x):
 return x*x*x
if (__name__ == '__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")
    number = int(input("Enter the number : "))
    print(cube_text," ",cube(number))
else:
    print(f"This module is called {__name__} and is being called by another script")