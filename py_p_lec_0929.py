from numpy.lib.index_tricks import fill_diagonal
import pandas as pd
import numpy as np
from pandas.core.indexes.base import Index
import seaborn as sns
# dict={
#     "name": ["A","B","C"],
#     "h": [4,5,6],
#     "w": [7,8,9]
# }
# df=pd.DataFrame(dict)
# df.set_index("name",inplace=True)
# print(df)

# print(df.iloc[[0,2],[0,1]])
# print(df.iloc[0:3])

# print("----------")
# print(df.h[0:3])

# multi_ind={
#     "x": [1,2,3],
#     "y": [4,5,6],
#     "f(x,y)": [7,8,9],
#     "g(x,y)": [10,11,12]
# }
# df=pd.DataFrame(multi_ind)
# df=df.set_index(["x","y"])
# print(df)

# dict_data={'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}
# df=pd.DataFrame(dict_data,index=['r0','r1','r2'])

# print(df)

# print("\n")


# new_index=['r0','r1','r2','r3','r4']
# ndf=df.reindex(new_index)
# print(ndf)
# print("\n")

# new_index=['r0','r1','r2','r3','r4']
# ndf2=df.reindex(new_index, fill_value=0)
# print(ndf2)


# dict_data={'c0':[1,22,3], 'c1':[4,55,6], 'c2':[7,88,9], 'c3':[10,111,12], 'c4':[13,144,15]}
# df=pd.DataFrame(dict_data,index=['r0','r11','r2'])

# ndf=df.sort_index(ascending=False) #index number asceding
# print(ndf)


# dict_data={'c0':[1,22,3], 'c1':[4,55,6], 'c2':[7,88,9], 'c3':[10,111,12], 'c4':[13,144,15]}
# df=pd.DataFrame(dict_data,index=['r0','r11','r2'])

# # dict_data={'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}
# # df=pd.DataFrame(dict_data,index=['r0','r1','r2'])

# print(df)
# print("\n")

# ndf=df.sort_values(by='c1',ascending=False)
# print(ndf)


# print("-------------------")

# stu1=pd.Series({'kor':100,'eng':80,'math':90})
# stu2=pd.Series({'math':80,'kor':90,'eng':80})
# print(stu1,"\n",stu2,"\n")
# add=stu1+stu2
# subs=stu1-stu2
# mul=stu1*stu2
# div=stu1/stu2
# print(type(div))
# print("\n")
# result=pd.DataFrame([add,subs,mul,div],index=["add","subs","mul","div"])
# print(result) #행의 오름차순으로 정렬됨. 그래서 영어로 쓰면 eng kor math 순이고 한글로 쓰면 국어 수학 영어 순임.


# print("--------------------")
# stu1=pd.Series({'kor':np.nan, 'eng':80, 'math':90})
# stu2=pd.Series({'math':80, 'kor':90})
# print(stu1)
# print("\n")
# print(stu2)
# print("\n")

# sr_add=stu1.add(stu2, fill_value=0)
# sr_subs=stu1.sub(stu2, fill_value=0)
# sr_mul=stu1.mul(stu2, fill_value=0)
# sr_div=stu1.div(stu2, fill_value=0)
# print(type(div))
# print("\n")
# result=pd.DataFrame([sr_add,sr_subs,sr_mul,sr_div],index=["add","subs","mul","div"])
# print(result)




titanic=sns.load_dataset('titanic')
df=titanic.loc[100:201,['age','fare']]
# print(df.head(5))
# print("\n")
# print(type(df))
# print("\n")
# print("-------------df+10---------")
# print(df+10)
# print("-------------df.add(10,fill_value=0)---------")
# print(df.add(10,fill_value=0))
# print("-------------df.head---------")
# df1=df.head(10)
# print(df1)
# print("-------------df.tail---------")
# df2=df.tail(10)
# print(df2)
# print("-------------df1.add(df2,fill_value=0)---------")
# print(df1.add(df2,fill_value=0))

print("-------------Prob---------")
#print(int(df.age.sum()/df.age.count()))

#print(df.add(0,fill_value=0))
print(df)
print("under this value:",int(df.age.sum()/df.age.count()))
rdf=df.copy()
count=0
for i, a in enumerate(df.age):
    if a>int(df.age.sum()/df.age.count()):
        rdf.drop(df.index[i],inplace=True)
print("------removed over the average-------")
print(rdf, "tot number:", len(rdf.index)) 

#####################################################
# file_path='./read_csv_sample.csv'
# df=pd.read_csv(file_path)
# print("\n\n", df)

# df0=pd.read_csv(file_path,header=1)
# print("df0==\n",df0)

# df1=pd.read_csv(file_path,header=None)
# print("df1==\n",df1)

# df2=pd.read_csv(file_path,index_col='c0')
# print("df1==\n",df2)

# read_csv()
# -path = 파일의 위치 포함한 파일명
# -sep = 필드를 구분하는 구분자 comma
# -header = 첫 행이 있는지, 없으면 None, 0
# -index_col = 인덱스로 사용될 컬럼명, None 인덱스 없음
# -names:컬럼 이름으로 사용될 문자열 리스트
# -skiprows: 스킵하고자하는 행 수
# -skipfooter:마지막 몇 줄을 스킵할지 설정
# -encoding: 텍스트 인코딩 종류 지정 ex) 'utf-8'
# save_file_path="./sample_to_csv.csv"
# print(df.to_csv(file_path))

# save_file_path="./sample_to_csv1.csv"
# print(df.to_csv(save_file_path,index=None)) #df의 인덱스 제거

#titanic 데이터를 load해서 age가 평균 age보다 적은 데이터를 가져와서 save_titanic.csv 파일에 저장(인덱스는 빼고)
#titanic.dtypes, titanic.columns



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