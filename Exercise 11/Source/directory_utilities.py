import os, platform
current_working_directory = None
def detect_os()->str:
    return platform.system()
def detect_working_directory()->str:
 return os.getcwd()
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