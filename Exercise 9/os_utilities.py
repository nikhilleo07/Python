import platform
 
def detect_os()->str:
    return platform.system()
def cpu_load():
    return(psutil.cpu_count(), psutil.cpu_percent())
if (__name__ == '__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")

    my_os = detect_os()
    my_os = my_os.lower()

    if my_os == "windows":
        print("Your system is Windows")
    elif my_os == "linux":
        print("Your system is Linux")
    elif my_os == "darwin":
        print("Your Apple system is MacOS")
    elif my_os == "cygwin":
        print("Your Apple system is MacOS")
    elif my_os == "aix":
        print("Your IBM system is AIX")
    else:
        print(f"Unidentified system = {my_os}")
else:
    pass
