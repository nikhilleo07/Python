from file_utilities import path_name, log_file_name
from os_utilities import detect_os
this_os = detect_os()
log_path = path_name()
filename = log_file_name(".log")
print (this_os)
print(log_path + filename )