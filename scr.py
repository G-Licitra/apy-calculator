import numpy as np
import pandas as pd 
from datetime import datetime

"""
APY a.k.a. annual percentage yield, is the rate earned on an investment in a year, 
taking into account the effects of compounding interest. APY is calculated by: 
APY= (1 + r/n)**n – 1, 
where “r” is the stated annual interest rate and “n” is the number of compounding 
periods each year.    
"""

initial_investment = 100 
r = 5/100  # 5 [%] annual interest rate
n = 4 # quartely number of compounding periods each year
APY = (1+r/n)**n -1

asset_APY = initial_investment + initial_investment*APY
asset_APR = initial_investment + initial_investment*r

print(f"APY = {round(APY*100,3)} %")
print(f"Asset with APY = {round(asset_APY, 3)} $")
print(f"Asset with APR = {round(asset_APR, 3)} $")



date_list = pd.date_range(start=datetime.today(), 
                         freq="M",
                         periods=12).tolist()


asset_list = [initial_investment]

for i in range(len(date_list)-1):
    print(f"i = {i} | date = {date_list[i]}")
    asset_list.append(asset_list[i] + asset_list[i]*APY)
    

df_asset = pd.DataFrame(data=asset_list, index=date_list, columns=['Asset (APY)']).round(2)