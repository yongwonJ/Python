#2.  리스트 작성 문제
list1 = []
for i in range(1,101):
    if i%2 == 0:
        list1.append(i)

print(list1)

list2 = [i for i in range(1,101) if i%2==0]
print(list2)

list3 = list(filter(lambda x : x%2 ==0, range(1,101)))
print(list3)

list4 = []
num = 0
while num < 101 :
    num+=1
    if num%2 == 0:
        list4.append(num)
    
print(num)
