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

#--------------------------------키 몸무게 받아서 하는 프로그램 v1--------

# import pandas as pd

# data={
#     "키":[],
#     "몸무게":[],
# }

# df=pd.DataFrame(data)
# print(df)

# while True:
#     try:
#         msg=(input("이름 키 몸무게 입력")).split()
#         name=msg[0]
#         if name=='q':
#             break
#         h=float(msg[1])
#         w=float(msg[2])
#         df.loc[name]=[h,w]
#         print(df)
#     except:
#         print("제대로 입력")

# print("검색하고자 하는 이름을 입력받아 키와 몸무게 출력")


# search_name=input("검색하려는 이름")

# if search_name in df.index:
#     print("{}".format(df.loc[search_name]))

# else:
#     print("해당하는 이름이 없다.")

# new_v=input("해당 인원의 키와 몸무게 변경값 입력").split()
# try:
#     h=float(new_v[0])
#     w=float(new_v[1])
#     df.loc[search_name,['키','몸무게']]=[h,w]
#     print("바뀐 데이터프레임",df)

# except:
#     print("입력 잘해 좀")

# t=0
# small=[]
# for i in df['키']:
#     if i < sum(df['키'])/len(df['키']):
#         print(df.iloc[t])
#     t+=1
# print(small)

#------------------------------키 몸무게 받아서 하는 프로그램 v2

#클래스 써서 해보고 싶다.
import pandas as pd
from pandas.core.indexes.base import Index #나 이거 쓴적 없는데 왜 생겨있지 index 관련 함수 쓰면 계속
#이름을 길게 쓰면 안되는 버그가 있다. 뭐지. a b c d처럼 짧은 이름은 괜찮은데 John처럼 이름이 길어지니까 튕기네
#self.group["name"]+=name으로 되어있었다. self.group("name")+=[name]로 하니까 되네. 이게 이름 긴거랑 상관이 있을까 애초에 list와 str로 자료형이 달라서 typeerror가 떴어야 한다. 처음처럼 쓰면 글자 하나씩 name으로 들어가더라.

change=[]
class Stats:
    group={
        "name": [],
        "height": [],
        "weight": []
    }
    df=pd.DataFrame(group)
    @classmethod
    def print_df(cls):
        df=pd.DataFrame(cls.group)
        df.set_index("name",inplace=True)
        print("------List of input group------")
        print(df)
        print("-------------------------------")
    @classmethod
    def change_df(cls):
        global change
        cls.df.set_index("name",inplace=True)
        for n in cls.df.index:
            if n==change[0]:
                cls.df.loc[n]=float(change[1]),float(change[2])
                print(cls.df.loc[n])
        print("------List of changed group------")
        print(cls.df)
        print("-------------------------------")
    @classmethod
    def small_df(cls):
        ave=(cls.df["height"].sum())/(cls.df["height"].__len__())
        small_num=len([i for i in cls.df["height"] if i<ave])
        print("average height:{}, # of smaller than average: {}".format(ave, small_num))
        for i, h in enumerate(cls.df["height"]):
            # if h<ave:
            #     print(cls.df.iloc[i])
            ##Alternative sol using df.drop
            if h>=ave:
                cls.df.drop(cls.df.index[i],inplace=True)
        print(cls.df)
    def __init__(self, name, height, weight):
        self.name=name
        self.height=height
        self.weight=weight
        Stats.group["name"] += [name]
        Stats.group["height"] += [height]
        Stats.group["weight"] += [weight]
        Stats.df=pd.DataFrame(self.group)
    
#Prob.1
while True:
    msg=input("Put name height weight (press 'q' to quit)>").split()
    try:
        if msg[0]=='q':
            print("This is what you typed")
            Stats.print_df()
            break
        if len(msg)!=3:
            print("put 1 name and 2 numbers")
            continue
        Stats(msg[0],float(msg[1]),float(msg[2]))
    except:
        print("use correct type of height and weight")
#Prob.2
change=input("Change target. Put name height weight again(should be on the list)").split()
try:
    if len(change)!=3:
            print("Put 1 name and 2 numbers")
    else:
        Stats.change_df()
except:
    print("Unexpected error ocurred")
#Prob.3
Stats.small_df()
