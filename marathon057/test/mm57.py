## Thinking in Python for Marathon Match 57
## will convert it into Java later
## See notes in ProblemStatement.html

def s64(i):
    ''' Convert int type into signed long (64 bit)
    http://stackoverflow.com/questions/385572/need-help-typecasting-in-python
    '''
    return (i + 2**63) % 2**64 - 2**63

def hash(str):
    ''' A classic hashing algorithm
    
    Input:
    str: an ASCII string (each character between 33-126, inclusive)
    
    Output:
    hash : signed 64-bit integer type
    '''
    hashn = 5381  
    for i in range(0, len(str)):
        hashn = (hashn * 33) ^ ord(str[i])        
    return s64(hashn)


## Testing examples
examples = {"-6O&Qk9~czXENxRw!" : -4459230493565586372,
            "LRi~~&ZA!GrUU{V" : 5501830964056691222,
            "dtzY<EUr-\\(43~^" : -8337223747280775818,
            "RU~nLF6Qnu" : 8245112492441997732,
            "*Wm-" : 6380591320,
            "L929U}MRV#}-A0tY" : 1460305034284426165,
            ">`YjL}HrF<Zm%0,I" : 2572936786439756830,
            "s)`PqJ3Z4pG\\xm^UG" : -5525835650212379589,
            "<Rk%H}D>PJ5!~={0" : 3928777983488211852,
            "`r*0*(DYq3!_wW>KJ6" : 6271036284597753639,
            "<l-Jk)-}lr-D" : -9215950419413139433,
            "/Ood6" : 210553093784,
            "J``Hc)=h" : 7571000880659480,
            "Sgoo5" : 210684487780,
            "GEURYiJzlMo" : -4637535168201879794,
            ".V;$uM5'" : 7566717596914600,
            "x3zHC'6{Z+f5" : -5887852083349028841,
            "n2PC6O2kny5DMO" : 3477693585084717134,
            "?>]s%E-s" : 7567427147094292,
            ",l{V<87Jb?!J" : 8420151027292092103}

examplesrev = dict((v,k) for k, v in examples.iteritems())
