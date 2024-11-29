import random
login = random.randint(3,20)
print(login)
parol =[]
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
for i in range(1,(login+1)//2):
    for j in range (2,login):
        if i>=j:
            continue
        if login % (i + j) == 0:
            parol.append(i)
            parol.append(j)
print(parol)
