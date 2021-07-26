import numpy as np 
import numpy_financial
#for comma delimitted series, first entry being initial investment
def net_present_worth(i , s ):
    npw = 0 
    s = s.strip() 
    
    series = s.split( ',' )
    series = [ float(t) for t in series ]

    for j in range(0, len(series)): 
        if j == 0:
            npw += series[j]
        else:
            npw += series[j] * ( (1/( 1+i)) ** ( j ) )
    return npw


def present_worth(i , s): 
    pw = 0 
    s = s.strip() 
    
    series = s.split( ',' )
    series = [ float(t) for t in series ]

    for j in range(0, len(series)): 
        if series[j] == 0 : 
            pass
        else:
            pw += series[j] * ( (1/( 1+i)) ** ( j ) )
    
    return pw

def future_worth(i , s):
    fw = 0 
    s = s.strip() 

    series = s.split( ',' )
    series = [ float(t) for t in series ]

    for j in range(0, len(series)):
       fw += series[j] * ( (1+i) **(len(series)-j))
    return fw

#effective interest given nominal, defaulting to compounding monthly
def effective_interest( r, m = 12 ):
    ieff = ( (1 + r/m)**m ) - 1
    return ieff 

def internal_ROR(s): 
    #returns decimal answer.
    s = s.strip() 
    series = s.split( ',' )
    series = [ float(t) for t in series ]
    series = np.array(series)
    irr = numpy_financial.irr(series)
    return irr 

def market_interest(interest, inflation):
    mrate = (1+interest)*(1+inflation)
    mrate = mrate - 1 
    return mrate






