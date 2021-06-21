####1 done
####2
>>> 5**9
1953125
>>> 3//2
1
>>> 7//3
2
>>> 7/3
2.3333333333333335
>>> 6==6
True
>>> a=20;a+=30;a%=3;print(a)
2
>>> True*False
0
>>> True&False
False
>>> True and False
False
>>> ((6>3) and (7<4)or (18==3))and(9>3)
False
>>> True is False
False
>>> False in 'False'
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    False in 'False'
TypeError: 'in <string>' requires string as left operand, not bool

>>> ((True==False) or (False > True)) and (False <= True)
False


####3
>>> s1= "Nice to have it"
>>> s2= "here"
>>> print(s1+' '+s2)
Nice to have it here

####4
a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2])
print(a[-3][-3][-1])

####5
a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
s1="Nice to have it"
s2="Here"
a[0]=s1
a[-1]=s2
print(a)

####6
color_list_1= set(["White","Black","Red"])
color_list_2= set(["Red","Green"])
print(color_list_1.difference(color_list_2))

####7

def ispangram (str):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
        return True

string= "This is assignment no one"
if(ispangram(string)== True):
    print("Given string is pangram")
else:
    print("Given string is not pangram")


####8
n=input("Enter any number:")
d=eval('{0}+{0}{0}+{0}{0}{0}'.format(n))
print(d)

##9
t=input("Enter comma separated sequence of words:")
tuple=t.split(",")
tuple.sort()
print(tuple)

##10
d={'Student':['Rahul','Kishore','Vidhya','Rakhi'],'Marks':[57,87,67,79]}
i=max (d['Marks'])
print (i)
pos=d['Marks'].index(i)
print(d['Student'][pos])
