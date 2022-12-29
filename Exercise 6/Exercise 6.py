import os, platform

current_working_directory = None
def detect_os()->str:
    return platform.system()
def detect_working_directory()->str:
    return os.getcwd()
def create_directory(directory_name: str)->int:
    if os.path.isdir(directory_name):
        return 2
    else:
        try:
            os.mkdir(directory_name)
            return 0
        except:
            print("Error creating directory {directory_name}")
        return 1

if (__name__ == '__main__'):
    print(f"This module executes as a standalone script")
    my_os = detect_os()
    my_os = my_os.lower()
    
    if my_os == "windows":
        print("Your system is Windows")
    elif my_os == "linux":
        print("Your system is Linux")
    else:
        print(f"Cannot continue, unidentified system = {my_os}")
        sys.exit()

    current_working_directory = detect_working_directory()
    print(f"You are coding in: {current_working_directory}")
else:
    print(f"This module is called {__name__} and is being called by another script")
if create_directory("JOR") == 0:
    print("Creating a directory worked")
elif create_directory("JOR") == 1:
    print("You couldn't create a directory!")
elif create_directory("JOR") == 2:
    print("Directory already existed!")

