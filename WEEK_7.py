import pandas as pd
print("=" * 60)
product_data = [['ebook',2000],['plants',5000], ['pencil',3000]]

indexes=[1,2,3]
columns_name=['product','unit_sold']
product_df= pd.DataFrame(product_data,index=indexes,columns=columns_name)
print(product_df)