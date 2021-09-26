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

