import numpy as np 
import numpy_financial as npf 
#find the acceptability of a project givien initial cost, annual profits, depreciation method, 
def tax_with_depreciation(annual_profit, years, initial_cost, depreciation_method = 'SL',  salvage = 0,alpha = 2 ): 
    #create cash flow series
    series = []
    series.append(initial_cost)
    #append annual profits
    for j in range(1,years+1):
        series.append(annual_profit)
    
    #calculate depreciation for DB method and apply it to cash flow 
    if depreciation_method == 'DB':
        coeff = alpha/years 
        bv = initial_cost
        seriesdb = series
        for j in range(1, years+1): 
            seriesdb[j] = seriesdb[j]-bv*coeff
            bv = (bv - bv*coeff)
        series_depr = seriesdb
        #return the edited cash flow 

    elif depreciation_method == 'SL': 
        depreciable_total = initial_cost-salvage
        annual_dep_charge = (1/years)*depreciable_total
        seriessl = series 
        for j in range(1,years+1): 
            seriessl[j] = seriessl[j] - annual_dep_charge
        series_depr = seriessl

    elif depreciation_method == 'SOYD': 
        depreciable_total = initial_cost-salvage
        seriessoyd = series 
        denom = years*(years+1)/2
        for j in range(1, years+1):
            seriessoyd[j] = seriessoyd[j] * ( ((len(seriessoyd) - 1) - (j-1))/denom )
        series_depr = seriessoyd
        
    
    #apply tax 

    npconversion = np.array( series_depr ) 
    irr = npf.irr(npconversion)
    return irr 



            

        

        



    