from xmlrpc.client import boolean


print('Functions')
def divisible(numerator:int, denominator:int)->boolean:
    return numerator % denominator ==0
print(divisible(44,4))

