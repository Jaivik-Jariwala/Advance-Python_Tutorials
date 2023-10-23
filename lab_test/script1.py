# %%
# importing dependencies
import pandas as pd
import numpy as np

# %%
df = pd.read_csv('sales_data.csv')


# %%
df.head(3)

# %%
df.describe()

# %%
total_sales = np.sum(df['Sales'])

# %%
total_profit = np.sum(df['Profit'])

# %%
print(total_sales)
print(total_profit)

import logging


#configure logging by changing level = logging --> to error
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

def disp():
    try:
        result=x/y
    except ZeroDivisionError:
        logging.error("division by zero error")
    else:
        logging.info("result is :{result}")



#perform division
divide(10,2)
divide(10,0)



