def solution(L, x):
    answer=L
    idx=0
    for i in L:
        if i<x:
            idx+=1
    answer.insert(idx,x)
    return answer

L=[1,5,7,89,3234,1231231423]
x=234234
print(solution(L,x))

print(len([]))

def solution(L, x):
    answer = []
    idx=0
    for i in L:
        if i==x:
            answer+=[idx]
        idx+=1
    if len(answer)==0:
        answer=[-1]
    return answer


def solution(L, x):
    if x in L:
        return [i for i, y in enumerate(L) if y == x]
    else:
        return [-1]

A=['a','b','z','d','adsda']
print(sorted(A,key=lambda x:-len(x)))

print(sorted(L,key=lambda x: (x-89)*(x-89)))
#숫자에 대해서는 key는 입력 함수의 최소값부터 정렬한 리스트 출력.

students=[
    {"name": 'John', "science": 61, "math": 96},
    {"name": 'David', "science": 82, "math": 36},
    {"name": 'Watson', "science": 59, "math": 16},
    {"name": 'Benedict', "science": 93, "math": 76},
    {"name": 'Ailey', "science": 36, "math": 86}
]

print(sorted(students, key=lambda x: x["name"]))
