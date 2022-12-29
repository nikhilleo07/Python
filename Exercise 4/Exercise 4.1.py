from xmlrpc.client import boolean


def find_num(number_list: list, number: int)->boolean:
 for checkinglist in number_list:
    if checkinglist == number:
        return True
    else:
        return False
result = find_num([1,2,3,4,5,6,7,8], 9)
print(result)