list1=[]
with open('new.txt','r') as file:
    for line in file:
        list1.append(line.split())
print(list1)        
