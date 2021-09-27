a={
    "a":1,
    "b":2,
    "c":3,
    "e":5
}
print(a)

a["d"]=4 #append to the tail of dictionary a
print(a)
for k,v in a.items():
    print("key : {}, value: {}".format(k,v))

for i,v in enumerate(a):
    print("idx : {}, value : {}".format(i,v))

#why dictionary doesn't need insert? hash function maybe?

a={
    "a":True,
    "b":True,
    "c":True,
    "e":True
}
msg=input("type any alphabets").split()

for i in msg:
    try:
        print("alphabet {} exist in a:{}".format(i,a[i]))
    except:
        print("{} is not in the list".format(i))

# if we make same searching with array, it could be O(n). this is O(1)

students=[
    {"name": 'A', "science": 61, "math": 96},
    {"name": 'B', "science": 82, "math": 36},
    {"name": 'C', "science": 59, "math": 16},
    {"name": 'D', "science": 93, "math": 76},
    {"name": 'E', "science": 36, "math": 86}
]
print("이름", "총점", "평균", sep="\t")
for student in students:
    score_sum=student["science"]+student["math"]
score_average=score_sum/len(students)
