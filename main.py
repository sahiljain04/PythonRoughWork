import math
k=math.pi
print(k)
print('Enter the number of stocks')
stocks=int(input())
print('Enter the rate of interest')
roi=float(input())
print('The total number of stocks are :',stocks)
print('The Rate of Interest is: ',roi,'%')
#print('Enter the unit price of each stock')
#unitprice=[]
#$for i in range(stocks):
 # unitprice[i]=input()
mytuple=()
mytuple=(100,300),(700,22),(500,654),(200,9054)
#mytuple.reshape([2,4])
#for u in range(stocks):
  
print(mytuple)
print(pow(2,4))
print(pow(math.pi,2))
x=10
b=3.14
#print(dir(x))
#print(dir(b))
print(dir())
print(x)
print(type)
k=[1,2,3,4,5,6,7]
print(k[0:4:2])
k_slice=slice(3)
print(k[k_slice])
a=5
#a="High five"
print('The value of a is :',a)
print(type(a))
num=121
num1="121"
num1=int(num1)
num2=num+num1
print(num2)
print(type(5.0))
print(type(5+3j))
myList=[]
myList=[1,2,3,4]
myList=[1,"Hello","121",5.6]
print(type(myList))
print(myList)
mytuple=(100,300,2,'2')#,'2Hello",'122')
#print(mytuple)
print(type(mytuple))
#print(mytuple)
del mytuple
set1={1,2,3}
set1={2,3,4}
print(set1)
set12={}
print(type(set12))
A={1,2,3}
B={1,2,4,5,6}
print(A & B)
print(A ^ B)
numbers=range(1,10)
print(list(numbers))
print(tuple(numbers))
print(set(numbers))
print(type(numbers))
for i in range(1,5):
  for j in range(1,i):
    print(j)
  print("\t")
tup=()
tup1=('Welcome')
count=0
print(tup1)
for i in range(0,7):
  if(tup1[i] == 'e'):
    count=count+1
  else:
    continue
print(count)