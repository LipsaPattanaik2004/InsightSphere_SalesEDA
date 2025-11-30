import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
sales = pd.read_csv('data/sales_data.csv', parse_dates=['order_date'])
sales.head()

print('Rows, Columns:', sales.shape)
print(sales.info())
print(sales.describe(include='all'))

sales['revenue'] = sales['quantity'] * sales['unit_price']
sales['month'] = sales['order_date'].dt.month
sales['year'] = sales['order_date'].dt.year
sales[['order_id','order_date','revenue','month','year']].head()

# Revenue by month
rev_month = sales.groupby(['year','month'])['revenue'].sum().reset_index()
print(rev_month)

# Revenue by region
rev_region = sales.groupby('region')['revenue'].sum().reset_index()
print(rev_region)

plt.figure()
plt.plot(rev_month['month'].astype(str) + '-' + rev_month['year'].astype(str), rev_month['revenue'])
plt.xlabel('Month-Year')
plt.ylabel('Revenue')
plt.title('Revenue by Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

top_prod = sales.groupby('product')['revenue'].sum().sort_values(ascending=False).reset_index()
print(top_prod)

plt.figure()
plt.bar(top_prod['product'], top_prod['revenue'])
plt.xlabel('Product')
plt.ylabel('Revenue')
plt.title('Revenue by Product')
plt.tight_layout()
plt.show()

# Export cleaned data
sales.to_csv('data/sales_data_cleaned.csv', index=False)
print('Exported cleaned data to data/sales_data_cleaned.csv')
