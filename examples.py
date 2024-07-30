'''n=int(input("Enter a Number:"))
for i in range(2,n):
    if n%i==0:
        print(n,'is not prime')
        break
else:
    print(n,'is prime')'''


'''x=int(input('enter first num:'))
y=int(input('enter second num:'))
if x>y:
    print('Bigger number is:',x)
else:
    print('bigger number is:',y)'''

'''n1=int(input('enter first number:'))
n2=int(input('enter second number:'))       
n3=int(input('enter third number:'))
if n1>n2 and n1>n3:
    print('biggest number is:',n1)
elif n2>n3:
    print('biggest number is :',n2)
else :
    print('biggest number is :',n3)

n1=eval(input('enter first number:'))
n2=eval(input('enter second number:'))       
n3=eval(input('enter third number:'))
if n1>n2 and n1>n3:
    print('biggest number is:',n1)
elif n2>n3:
    print('biggest number is :',n2)
else :
    print('biggest number is :',n3)

n=int(input('enter number:'))
if n>=1 and n<=100:  # use if 1<=n>=100 
     print('the number ',n,'is in between 1 and 100')
else:
     print('the number' ,n, 'is not between 1 and 100')
##
x= int(input('enter a number from 0-9:'))
if x==0:
       print('Zero')
elif x==1:
    print('one')
elif x==2:
    print('Two')
elif x==3:
    print('three')
elif x==4:
     print('four')
elif x==5:
     print('five')
elif x==6:
    print('six')
elif x==7:
    print('seven')
elif x==8:
    print('eight')
elif x==9:
    print('nine')
else:
    print('plze enter the number 0 to 9 only')

s='harinath reddy'
for x in s:
    
 print(x)

s=eval(input("enter sample string:"))
count=0
for x in s:
    count+=1
    print(x)
print('the string count is:',count) 


s= input('enter string:')
i=0
for x in s:
    print('the character present at',i,'index is',x)
    i=i+1 

for x in range(10):
 print('Hello')

for x in range(11):
 print(x)

for x in range(21):
    if x%2!=0:
        print('the odd numbers are:',x)

for x in range(10,0,-1):
    print(x)
for x in range(25,9,-1):
    print(x) 

l=eval(input('enter a list:'))
sum=0
for x in l:
    sum=sum+x
print('sum of given list is:',sum


x=1
while x<=10:
    print(x)
    x=x+1    


n=int(input('enter some number:'))
sum=0
i=1
while i<= n:
    sum=sum+i
    i+=1
print('sum of first',n, 'numbers is',sum)


name=""
pwd=""
while (name!='banni') and (pwd!='hari'):
  name=input('enter name')
  pwd=input('enter password')
print('thanks for conformation')  



for i in range(4):
  for j in range(3):
   print('i={} and j={}'.format(i,j))


n=int(input('enter the num of rows'))
for i in range(1,n+1):
    for j in range(1,i+1): # for j in range(i)
        print('*',end='')
    print()               

n=int(input('enter the num:'))
for i in range(n):
    for j in range(n):
        print('*',end='')
    print()          



n=int(input('enter the num:'))
for i in range(n):
    for j in range(n):
        print('*')
    print()    


n=int(input('enter no of rows:'))
for i in range(1,n+1):
    print('*'*i)  
    

n=int(input('enter the num:'))
for i in range(n):
    for j in range(n):
        print('n',end='')
    print() '''

'''i=0
while True: 
    print('Hello')
    i+=1
    if i==5:
        break



i=0
while 1: 
    print('Hello')
    i+=1
    if i==5:  
        break   '''


'''for i in range(10):
    if i==7:
        print('processing is enough..')
        break
    print(i) '''

'''c=[10,20,30,600,80,90]
for i in c:
    if i>=500:
        print('sorry can not proces')
        break
    print('processing',i) '''

'''for i in range(10):
    if i%2==0:
        continue
    print(i) '''

'''c=[10,20,30,600,60,550,70]
for i in c:
    if i>500:
        print('can not process')
        continue
    print(i) '''

'''l=[10,20,0,5,0,3]
for i in l:
    if l==0:
        print('can not divide ')
        continue
    print('100/{}={}'.format(i,100/i)) '''



'''if True:pass
else:
    print('Hello') '''

'''def f1():
    print('Hi')
def f2():
    pass
f1()
f2()'''

'''for i in range(100):
    if i%10==0:
        print(i)
    else:pass    

    
 for i in range(100):
    if i%10==0:
        print(i)   '''

'''x=100
print(x)
del x
print(x)'''

'''s='hari'
print(s)
del(s[1]) '''

'''s='hari'
del s '''

'''x=10
y=20
del x
del y
print(y) '''


'''x=100
y=200
del x
y=None
#print(x)
print(y)'''

'''s1='hari'
s2='hari'
s3='hari'
print(id(s1),id(s2),id(s3))'''

'''s1='hari'
s2='hari'
s3='hari'
del s1
print(s2)
print(s3)'''


'''s='0123456789'
print(s[0])
print(s[3])
print(s[2:5])
print(s[2:])
print(s[:])
print(s[:6])
print(s[::])
print(s[0:6:2])
print(s[::-1]) '''

s='Harinatha Reddy'
(s[::-1])
print(s[2:6:-1])





















































        























        








































     



















    
