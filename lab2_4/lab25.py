import pandas as pd
import numpy as np


orders = pd.read_csv('orders.csv')
orders['order_date'] = pd.to_datetime(orders['order_date'])
cust = pd.read_csv('customers.csv')
order_full = pd.merge(orders,cust, left_on ='customer_id', right_on = 'id')
order_full['year'] = order_full['order_date'].dt.year
pivot = order_full.pivot(index=['state'],columns ='year',aggfunc=np.sum)
print(order_full)
print(pivot)