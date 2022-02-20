import numpy as np
import pandas as pd 


def asset_over_time_apy(P:int, r:float, n:int, t:float) -> pd.DataFrame:
    """
    Compute the ending value of some investment after a certain amount of time with compound interest. 
    
    Parameters
    ---------
    P: int
        Initial investment
    r: float
        Annual Interest Rate
    n: int
        Number of compounding periods per year
    t: int
        Number of years

    Returns
    ---------
    amount: pd.DataFrame
        Final amount

    Examples
    ---------

    >>> # Suppose we invest $5,000 into an investment that compounds at 6% annually.
    >>> # Calculate the ending value of this investment after 10 years:
    >>> P, r, n, t = 5000, .06, 1, 10
    >>> df = asset_over_time_apy(P=5000, r=.06, n=1, t=10)
    >>> # Expected df[-1] = 8954.238483
           
    """

    df = pd.DataFrame(data={'time': np.linspace(start=1, stop=t, num=t)})
    df['value']= df.applymap(lambda t: P*(pow((1+r/n), n*t)))

    return df




if __name__ == "__main__":  
   """
   Run for testing only and store example
   """

   """
   https://www.statology.org/compound-interest-in-python/
   Example 1: Compound Interest Formula with ANNUAL Compounding
   Suppose we invest $5,000 into an investment that compounds at 6% annually.
   Calculate the ending value of this investment after 10 years:
   """

   df = asset_over_time_apy(P=5000, r=.06, n=1, t=10)
   print(df)
   # Expected df[-1] = 8954.238483

   """
   Example 2: Compound Interest Formula with MONTHLY Compounding
   Suppose we invest $1,000 into an investment that compounds at 6% annually 
   and is compounded on a monthly basis (12 times per year).
   Calculate the ending value of this investment after 5 years:
   """

   df = asset_over_time_apy(P=1000, r=.06, n=12, t=2)
   print(df)
