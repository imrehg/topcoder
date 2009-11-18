from __future__ import division
from mm57 import hash
from time import time

def isint(test):
    if (int(test) - test) == 0:
        return True
    else:
        return False

def backhash(test, i):
    if isint(test):
        return (int(test) ^ i) / 33
    else:
        return 0

def data2str(data, nchar):
    string = ""
    for i in range(nchar, -1, -1):
        string += chr(data[i])
    return string

string = "0123456789"
test = hash(string)
print "Test: %s -> %d" %(string,test)

data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def recursehash(nchar, data, hashtemp):
    if (nchar < 20):
        for i in range(33, 127):
            temp = backhash(hashtemp, i)
            if isint(temp):
                data[nchar] = i
                if (temp == 5381.0):
                    return (nchar, data)
                if (temp >= 5381 * 30) | (temp < 0):
#                    print data2str(data, nchar)
                    (out1, out2) =  recursehash(nchar + 1, data, temp)
                    if (out1 > 0):
                        return (out1, out2)
        return (0, [])
    else :
        return (0, [])

start = time()
out1, out2 = recursehash(0, data, test)
print out1, out2
res = data2str(out2, out1)
print "Result: %s (%d)" %(res, hash(res))
elapsed = time() - start
print "Time: %f s" %(elapsed)
