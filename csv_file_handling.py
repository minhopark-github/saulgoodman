import pandas as pd
import seaborn as sns

# from numpy.lib.index_tricks import fill_diagonal
# import pandas as pd
# import numpy as np
# from pandas.core.indexes.base import Index
# import seaborn as sns

titanic=sns.load_dataset('titanic')
df=titanic.loc[:]
small=[]
print("under this value:",float(df.age.sum()/df.age.count()))
for i,a in enumerate(df.age):
    if a<float(df.age.sum()/df.age.count()):
        small.append(df.iloc[i])
df_small=pd.DataFrame(small)
save_file_path="./save_titanic.csv"
print(df_small.to_csv(save_file_path,index=None))

data_types=titanic.dtypes
column_names=titanic.columns

columns=[]
for idx,dtype in enumerate(data_types):
    if dtype in ['float64','int64']:
        columns.append(column_names[idx])

titanic_select=titanic.loc[:,columns] #df.loc[행 또는 배열,컬럼 또는 배열]

titanic_select.to_csv("./titanic_save_file.csv",index=None)

print(titanic.dtypes)