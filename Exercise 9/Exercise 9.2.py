from file_utilities import path_name, log_file_name
from os_utilities import detect_os,cpu_load
from time import sleep
this_os = detect_os()
log_path = path_name()
filename = log_file_name(".csv")
while True:
    sleep(1)
    timestamp = log_file_name("")
    information = cpu_load()
    logline = timestamp + ":" + str(information[0]) + "," + str(information[1]) + "\n" 
    try:
        with open(filename, "a") as file_handle:
            print(f"logging to {filename}")
            file_handle.write(logline)
    except IOError as err:
        print(f"IOError was {err}")
    except EOFError as err:
        print(f"End of file error was {err}")
    except OSError:
        print("OS Error")
    except:
        print("General Error")
