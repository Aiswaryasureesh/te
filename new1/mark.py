print("enter 5 marks")
m1=int(input())
m2=int(input());
m3=int(input());
m4=int(input());
m5=int(input());
sum=m1+m2+m3+m4+m5;
average=sum/5;
if(m1<40 or m2<40 or m3<40 or m4<40 or m5<40):
    print("Grade:E")

elif(average>=91 and average<=100):
    print("Grade:A+");
elif(average>=80 and average<=90):
    print("Grade:A");
elif(average>=60 and average<=80):
    print("Grade:B");
elif(average>=50 and average<=60):
    print("Grade:C+");
elif(average>=40 and average<=50):
    print("Grade:C");
else:
    print("Grade:F");
