# #Class 개념

# # students=[
# #     {"name": 'John', "science": 61, "math": 96},
# #     {"name": 'David', "science": 82, "math": 36},
# #     {"name": 'Watson', "science": 59, "math": 16},
# #     {"name": 'Ben', "science": 93, "math": 76},
# #     {"name": 'Ailey', "science": 36, "math": 86}
# # ]

# def cre_stu(name, sci, math):
#     return {
#         "name": name,
#         "sci": sci,
#         "math": math
#     }

# students=[
#     cre_stu("John",61,96),
#     cre_stu("David",82,36),
#     cre_stu("Watson",59,16),
#     cre_stu("Ben",93,76),
#     cre_stu("Ailey",36,86)
# ]

# # print("name","tot score","average",sep="\t")
# # for x in students:
# #     tot_score=x["sci"]+x["math"]
# #     average=tot_score/2
# #     print()
# #     print(x["name"],tot_score,average,sep="\t")

# def stu_sum(x):
#     return x["sci"]+x["math"]
# def stu_ave(x):
#     return (x["sci"]+x["math"])/2
# def stu_str(x):
#     return "{}\t{}\t{}".format(x["name"],stu_sum(x),stu_ave(x))

# print("name","tot score","average",sep="\t")

# for x in students:
#     print(stu_str(x))


#객체지향형 프로그래밍을 클래스로 선언

class Stu:
    def __init__(self,name,sci,math):
        self.name=name
        self.sci=sci
        self.math=math
    # def cre_stu(name, sci, math):
    #     return {
    #         "name": name,
    #         "sci": sci,
    #         "math": math
    #     }

    def stu_sum(self):
        return self.sci+self.math
    def stu_ave(self):
        return (self.sci+self.math)/2
    def stu_str(self):
        return "{}\t{}\t{}".format(self.name,self.stu_sum(),self.stu_ave())
    def __eq__(self, value): 
        return self.stu_sum() == value.stu_sum()
    def __ne__(self, value): 
        return self.stu_sum() != value.stu_sum()
    def __gt__(self, value):
        return self.stu_sum() > value.stu_sum()
    def __ge__(self, value):
        return self.stu_sum() >= value.stu_sum()
    def __lt__(self, value):
        return self.stu_sum() < value.stu_sum()
    def __le____(self, value):
        return self.stu_sum() <= value.stu_sum()
# def stu_sum(x):
#     return x["sci"]+x["math"]
# def stu_ave(x):
#     return (x["sci"]+x["math"])/2
# def stu_str(x):
#     return "{}\t{}\t{}".format(x["name"],stu_sum(x),stu_ave(x))

### Class defined

students=[
    Stu("John",61,96),
    Stu("David",82,36),
    Stu("Watson",59,16),
    Stu("Ben",93,76),
    Stu("Ailey",36,86)
]

# students=[
#     cre_stu("John",61,96),
#     cre_stu("David",82,36),
#     cre_stu("Watson",59,16),
#     cre_stu("Ben",93,76),
#     cre_stu("Ailey",36,86)
# ]

print("name","tot score","average",sep="\t")

for x in students:
    print(x.stu_str())

# print("name","tot score","average",sep="\t")

# for x in students:
#     print(stu_str(x))

#클래스 선언하면서 실수하기 쉬웠던 점: self
# self라는 개념은 그냥 갖다붙이면 되는거라 처음 클래스 정의할때는 딕셔너리처럼, 함수정의할때는 매개변수처럼 쓰다가 함수를 사용할때는 다시 딕셔너리의 self로 쓰인다. 그러니까 크게 봤을때는 self는 딕셔너리가 맞는데, 함수정의할때는 매개변수로 쓰일수있게 되어있다.
John=Stu("John",61,96),
David=Stu("David",82,36),
# class Human:
#     def __init__(self):
#         pass
# class Stu(Human):
#     def __init__(self):
#         pass
# student=Stu()
# print("isinstance(student,Human):",isinstance(student,Human))
# print("type(Human):",type(student)==Human)

print("John > David",John.__gt__(David))