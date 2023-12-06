color=[]
n=int(input("enter total number of colors:"))
print ("enter colors")
for i in range(n):
    ch=input()
    color.append(ch)
print(f"first color is:{color[0]}\nlast color is:{color[-1]}")
