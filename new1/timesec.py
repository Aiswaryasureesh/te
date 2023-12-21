class Time:
    def __init__(self):
        self.hours=int(input("enter the hours:"))
        self.minutes=int(input("enter the minutes:"))
        self.second=int(input("enter the seconds:"))
    def __add__(self,t2):
        hours=self.hours+t2.hours
        minutes=self.minutes+t2.minutes
        second=self.second+t2.second
        total=hours*60*60+minutes*60+second
        return self.convert(total)
    def convert(self,second):
        second=second%(24*3600)
        hour=second//3600
        second%=3600
        minutes=second//60
        second%=60
        return hour,minutes,second
 #main
t1=Time()
t2=Time()
print("total time:",t1+t2)
    
