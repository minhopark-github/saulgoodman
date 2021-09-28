import pandas as pd
data={
    "a":1,
    "b":2,
    "c":3
}

sr=pd.Series(data)
print(type(sr))
print("\n")
print(sr)

print(data['a'], ":", sr['a'],":", sr[0])

print()

print(sr[['a','c']])

print("-----")
print(sr[1:2]) #인덱스 첨자로 접근하면 마지막 데이터 미포함
print("-----")
print(sr['b':'c']) #인덱스로 하면 마지막 데이터 포함
print("-----")
data={
    "a":[1,2,3],
    "b":[4,5,6],
    "c":[7,8,9]
}

df=pd.DataFrame(data)
print(df)



df1=pd.DataFrame(data,index=["idx1","idx2","idx3"],columns=['a','b','c'])
print(df1)

var=[[1,2,3],[4,5,6],[7,8,9]]
df2=pd.DataFrame(var,index=["idx1","idx2","idx3"],columns=['a1','b1','c1'])
print(df2)


exam_data={'수학':[90,80,70],'영어':[98,89,95],'음악':[85,95,100],'체육':[100,90,90]}

df=pd.DataFrame(exam_data,index=['서준','우현','민아'])
print(df)
print("\n")

#데이터프레임 df를 복제하여 변수 df2에 저장. df2의 1개 행(row) 삭제

df2=df[:]
df2.drop('우현',inplace=True)
print(df2)

print()
print()
print()
df3=df[:]
df3.drop(['서준','민아'],axis=0,inplace=True)
print(df3)
print()
print()
print()

df['수학']=[1,2,45]
print(df, "\n\n\n\n", df3)

print("--------------------")
print(df.loc['서준':'민아'])
print("------")
print(df.iloc[0:2])
print("------")
print(df.loc['민아'])
print(df.iloc[2])

df.loc["희연"]=[99,97,88,99]
print(df)


print("------문제시작------")

print("키보드에서 국영수 점수를 입력받아 이름을 인덱스로 저장하는 score dataframe을 생성하여 결과를 출력")

data={
    "국어":[],
    "영어":[],
    "수학":[]
}

df=pd.DataFrame(data)
print(df)

while True:
    try:
        msg=(input("이름 국 영 수 입력")).split()
        name=msg[0]
        if name=='quit':
            break
        kor=float(msg[1])
        eng=float(msg[2])
        math=float(msg[3])
        df.loc[name]=[kor,eng,math]
        print(df)
    except:
        print("제대로 입력")

print("검색하고자 하는 이름을 입력받아 성적과 성적의 합 출력")


search_name=input("검색하려는 이름")

if search_name in df.index:
    print("성적:\n{} 합계:{}".format(df.loc[search_name],sum(df.loc[search_name])))

else:
    print("해당하는 이름이 없다.")

# import pandas as pd

# # DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장 
# exam_data = {'이름' : [ '서준', '우현', '인아'],
#              '수학' : [ 90, 80, 70],
#              '영어' : [ 98, 89, 95],
#              '음악' : [ 85, 95, 100],
#              '체육' : [ 100, 90, 90]}
# df = pd.DataFrame(exam_data)
# print(df,"\n---------------------------")



# # '이름' 열을 새로운 인덱스로 지정하고, df 객체에 변경사항 반영
# df.set_index('이름', inplace=True)
# print(df)
# print('\n')

# # 데이터프레임 df의 특정 원소 1개 선택 ('서준'의 '음악' 점수)
# a = df.loc['서준', '음악']
# print(a)
# b = df.iloc[0, 2]
# print(b)
# print('\n')

# # 데이터프레임 df의 특정 원소 2개 이상 선택 ('서준'의 '음악', '체육' 점수) 
# c = df.loc['서준', ['음악', '체육']]
# print(c)
# d = df.iloc[0, [2, 3]]
# print(d)
# e = df.loc['서준', '음악':'체육']
# print(e)
# f = df.iloc[0, 2:]
# print(f)
# print('\n')

# # df의 2개 이상의 행과 열로부터 원소 선택 ('서준', '우현'의 '음악', '체육' 점수) 
# g = df.loc[['서준', '우현'], ['음악', '체육']]
# print(g)
# h = df.iloc[[0, 1], [2, 3]]
# print(h)
# i = df.loc['서준':'우현', '음악':'체육']
# print(i)
# j = df.iloc[0:2, 2:]
# print(j)


# # print(list(i for i in range(0,3)))
# print(list(df['음악'][i] for i in range(0,3)))


import pandas as pd

data={
    "키":[],
    "몸무게":[],
}

df=pd.DataFrame(data)
print(df)

while True:
    try:
        msg=(input("이름 키 몸무게 입력")).split()
        name=msg[0]
        if name=='q':
            break
        h=float(msg[1])
        w=float(msg[2])
        df.loc[name]=[h,w]
        print(df)
    except:
        print("제대로 입력")

print("검색하고자 하는 이름을 입력받아 키와 몸무게 출력")


search_name=input("검색하려는 이름")

if search_name in df.index:
    print("{}".format(df.loc[search_name]))

else:
    print("해당하는 이름이 없다.")

new_v=input("해당 인원의 키와 몸무게 변경값 입력").split()
try:
    h=float(new_v[0])
    w=float(new_v[1])
    df.loc[search_name,['키','몸무게']]=[h,w]
    print("바뀐 데이터프레임",df)

except:
    print("입력 잘해 좀")

t=0
small=[]
for i in df['키']:
    if i < sum(df['키'])/len(df['키']):
        print(df.iloc[t])
    t+=1
print(small)


