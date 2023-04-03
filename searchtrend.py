#Google search analysis using pytrends

import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()
 #Reference: analyse search trends on queries based on "ML" 
 #Creating a dataframe of top 10 countries which searched for ML on Google
 
trends.build_payload(kw_list=["The Batman"])
data=trends.interest_by_region()
data = data.sort_values(by="The Batman", ascending = False)
data = data.head(10)        #parameter==takes 10 countries for analysis
print(data)


