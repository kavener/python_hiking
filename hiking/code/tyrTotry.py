dict={
    0:["Python"],
    1:"C",
    2:"Ruby"
}
#keys返回的是列表？？？
print(dict.keys())
dict[0].append("haha")
print(dict)
dict[3] = ["dd"]
print(dict[3])
classCount = 10

classCollects = {}
for key_number in range(0, classCount):
    classCollects[key_number] = []
    print(classCollects[key_number])
