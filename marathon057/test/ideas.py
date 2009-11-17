from __future__ import division
from mm57 import hash


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

def goodChars(test):
    out = ""
    end = 0
    for i in range(33,127):
        temp = backhash(test, i)

        if (int(temp) - temp) == 0:
            out += chr(i)

        if temp == 5381.0:
            print "%c = END!" %(chr(i))
            end = i
    return (out, end)

end = 0

string = "fY"
test = hash(string)
print "Test: %s -> %d" %(string,test)

out, end = goodChars(test)
print out
for i in range(0,len(out)):
#    print backhash(test,ord(out[i]))
    our, end = goodChars(backhash(test,ord(out[i])))
    if (end > 0):
        print "%c%c" %(chr(end),out[i])
