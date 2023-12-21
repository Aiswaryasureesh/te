ch=0
l=int(input("enter length "))
b=int(input("enter breadth "))
ob=Rectangle()
ob.getdata(l,b)
ob.display()
ob.perimeter()
while ch!=3:
    print("1. area")
    print("2. perimeter")
    print("3. exit")
    ch=int(input("enter your choice"))

if ch==1:
   ob.area()
if ch==2:
   ob.perimeter()
else:
    print("exit")
      
