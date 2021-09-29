#문 seaborn 에서 dataset "iris"를 불러와서
# 1. 'species'컬럼을 인덱스로 설정
# 2. 나머지 데이터의 합과 평균을 데이터 프레임에 추가
# 3. 변경된 데이터를 파일에 csv 형식으로 저장
# 4. 저장된 파일을 프로그램으로 불러 옴
# 5. 불러온 데이터를 출력해서 확인

import pandas as pd
from pandas.io.parsers import read_csv
import seaborn as sns


iris=sns.load_dataset('iris')
df=pd.DataFrame(iris)
df.set_index("species",inplace=True)

print("-------Given Data with species index------")
print(df)
print("number of columns, number of indexs")
print(len(df.columns), len(df.index))
print("--------for each columns,--------")
print("--------find sum, average and add to dataframe--------")
#column을 일일이 타이핑하기 귀찮은데, 할수 있는 방법은 언뜻 봐도 총 세개다.
# 첫번째는 야매인데, 칼럼을 안쓰는거다. 연산할때는 Transverse로 그냥 row로 만들어주면, 숫자 인덱스를 쉽게 활용할 수 있다.
#두번째는 df.iloc[:,[]]이런 식으로 원하는 칼럼을 선택해서 데이터 처리 하는 거다. 이게 가장 기본이지.
#세번쨰는 df.columns를 이용하는건데, 나는 이게 그냥 칼럼 이름 시리즈만 뽑는걸로 생각했는데, 여기서 칼럼이름을 대체해서 인덱스처럼 활용가능하다. df[칼럼이름] 또는 df.칼럼이름 하면 해당 칼럼이 뽑히니까. 그래서 이번엔 신박한 세번째 방법으로 해볼거다.df.df.columns[i]은 안 되더라.확실히 괄호로 묶인게 파워풀하네.
iris_sum=[]
iris_avg=[]
print(df[df.columns[0]])
for i in range(0,len(df.columns)):
    iris_sum+=[sum(df[df.columns[i]])]
    iris_avg+=[sum(df[df.columns[i]])/len(df[df.columns[i]])]
print("---------sum--------")
print(iris_sum)
print("---------avg--------")
print(iris_avg)
print("--------merged---------")
df.loc["iris_sum"]=iris_sum
df.loc["iris_avg"]=iris_avg
print(df)
df.to_csv("./iris_problem.csv")
df_output=pd.read_csv("./iris_problem.csv")
print(df_output[df_output.columns[0]])
# small=[]
# print("under this value:",float(df.age.sum()/df.age.count()))
# for i,a in enumerate(df.age):
#     if a<float(df.age.sum()/df.age.count()):
#         small.append(df.iloc[i])
# df_small=pd.DataFrame(small)
# save_file_path="./save_iris.csv"
# print(df_small.to_csv(save_file_path,index=None))

# data_types=iris.dtypes
# column_names=iris.columns

# columns=[]
# for idx,dtype in enumerate(data_types):
#     if dtype in ['float64','int64']:
#         columns.append(column_names[idx])

# iris_select=iris.loc[:,columns] #df.loc[행 또는 배열,컬럼 또는 배열]

# iris_select.to_csv("./iris_save_file.csv",index=None)

# print(iris.dtypes)