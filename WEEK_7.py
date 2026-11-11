import pandas as pd
import numpy as np
print("=" * 60)
product_data = [['ebook',2000],['plants',6000], ['pencil',3000]]
indexes=[1,2,3]
columns_name=['product','unit_sold']
product_df= pd.DataFrame(product_data,index=indexes,columns=columns_name)
print(product_df)
print("=" * 60)
# using dictionaries
product_data={'product': ['e-book', 'plants', 'Pencil'], 'unit_sold':
[2000, 5000, 3000]}
product_df = pd.DataFrame(data=product_data)
print(product_df)
print("=" * 60)
# using numpy array
products =np.array([['','product','unit_sold'], [1, 'E-book',2000],[2, 'Plants', 6000], [3, 'Pencil', 3000]])
product_pf = pd.DataFrame(data=products[1:,1:],index=products[1:,0 ],columns=products[0,1:])
print(product_pf) # output is same as of first case