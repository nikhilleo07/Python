from datetime import datetime as dt
import sys, csv
def path_name():
    this_os = sys.platform
    if this_os == 'win32':
        return './logfiles/'
    elif this_os == 'linux':
        return '/home/pi/logfiles/'
    else:
        print(f'Unsupported OS: {this_os}')
        exit(0)
def log_file_name(extension):
    now = dt.now()
    file_name = '%0.4d%0.2d%0.2d-%0.2d%0.2d%0.2d' % (now.year, now.month, now.day, now.hour, now.minute,now.second)
    return file_name + extension
if (__name__ == '__main__'):
 print(f"This module is called {__name__} and executes as a standalone script")
 log_path = path_name()
 filename = log_file_name(".log")
 print(log_path + filename )
else:
 pass