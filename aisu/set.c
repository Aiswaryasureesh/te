#include<stdio.h>
#include<conio.h>
int u[10],a[10],b[10],n;
void display(int x[]){
int i;
printf("{");
for(i=0;i<n;i++)
printf("%d,",x[i]);
printf("}");
}
void bitdis(int x[]){
int i;
printf("{");
for(i=0;i<n;i++){
if(x[i]==1)
printf("%d,",u[i]);
}
printf("}");
}
int pos(int x){
int i,f=-1;
for(i=0;i<n;i++){
if(u[i]==x)
f=i;
}
return f;
}
void setunion(){
int i;
printf("\nUnion:{");
for(i=0;i<n;i++){
if(a[i]|b[i]==1)
print

