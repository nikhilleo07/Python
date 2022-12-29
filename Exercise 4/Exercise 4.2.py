from xmlrpc.client import boolean


def even(numberlist:list)->boolean:
    f=0
    for evennumber in numberlist:
        if evennumber %2==0:
            f=f+1
    if f >=1:
        return True
    else:
        return False
final=even([1,2,3,4,5,6,7,8,9])
print (final)