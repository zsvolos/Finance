import numpy as np 

#for comma delimitted series
def net_present_worth(i , s ):
    pw = 0 
    s = s.strip() 
    
    series = s.split( ',' )
    series = [ float(t) for t in series ]

    for j in range(0, len(series)): 
        npw += series[j] * ( (1/( 1+i)) ** ( j ) )
    
    print(npw)
    print(series)


def present_worth(i , s): 
    pw = 0 
    s = s.strip() 
    
    series = s.split( ',' )
    series = [ float(t) for t in series ]

    for j in range(0, len(series)): 
        if series[j] <= 0 : 
            pass
        else:
            pw += series[j] * ( (1/( 1+i)) ** ( j ) )
    
    print(pw)
    print(series)

def future_worth(i , s):
    fw = 0 
    s = s.strip() 

    series = s.split( ',' )
    series = [ float(t) for t in series ]

    for j in range(0, len(series)):
        if series[j] <= 0 : 
            pass
        else: 
            fw += series[j] * ( (1+i) **(len(series)-j))

    print(fw) 

#effective interest given nominal, defaulting to compounding monthly
def effective_interest( r, m = 12 ):
    ieff = ( (1 + r/m)**m ) - 1
    return ieff 

def 




