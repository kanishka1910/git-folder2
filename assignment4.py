# : Write a Program to make a simple calculator that can add, subtract, multiply and divide using functions 
'''
def cal(a,b,n):
    if n==1:
        return a+b
    if n==2:
        if a>b:
            return a-b
        else:
            return b-a
    if n==3:
        return a*b
    if n==4:
        if a>b:
            return a/b
        else:
            return b/a

n = int(input("Enter the (1/2/3/4) to get the subtraction,addition,multiplication,division  "))
if n in [1,2,3,4]:
    a=int(input("Enter the First Value"))
    b=int(input("Enter the Second Value"))
    print("Thanks for the use to calculate: ",cal(a,b,n))
else:
    print("Enter the Choice from given number")

'''
# Wap a Function of version of a palindrome recognizer that also accepts phrase palindromes such as
# "Go hanga salami I'm a lasagna hog.", "Was it a rat I saw?"
'''
def pal(s):
    s2=s.split(" ")
    s3=""
    for i in s2:
        if i == i[::-1]:
            s3+=i+" "
    return s3

s=input("Enter the String to be checked is there a palindrome word")
s1="!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~)]"
s2=""
for i in s:
    if i in s1:
        continue
    else:
        s2+=i
print("Pralindrome word in the String ",pal(s2))
'''

# A pangram is a sentence that contains all the letters of the English alphabet at least once,
'''
import string
s="abcdefghijklmnopqrstuvwxyz"
s1=input("Enter the paragraph")
p=set(s1.lower())
p1=set(string.ascii_lowercase)
if p1.issubset(p):
    print("Panagram")
else:
    print("Not panagram")

'''
# Define a function overlapping() that takes two lists and returns True if they have at least one member in common,
# False otherwise
'''
def overlapping(l1,l2):
    for i in l1:
        if i in l2:
            return True

l1=[i for i in input("Enter the list ").split(" ")]
l2=[i for i in input("Enter the list ").split(" ")]

if overlapping(l1,l2) == True:
    print("True")
else:
    print("False")
'''

# Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
'''
def longest (n):
    p = len(n)
    return p
l1 = [i for i in input("Enter the String ").split(" " )]
l2={}
for i in l1:
    l2[i]= longest(i)
sorteddict = dict(sorted(l2.items()))
print(list(sorteddict.items())[1])

'''

#: write a Program to display the Fibonacci sequence up to n-th term where n is provided by the user
'''
n=int(input())
a=0
print(a)
b=1
print(b)
sum=0
for i in range(2,n):
    sum=a+b
    print(sum)
    a=b
    b=sum
'''
#: Write a Python Program to Display Powers of 2 Using Anonymous Function
'''
x=int(input("Enter the value to display the power "))
y = lambda x : x**2
print("Power of the number ",y(x))
'''

#: Write a Python Program to find numbers divisible by thirteen from a list using anonymous function
'''
l1=[int(i) for i in input("Enter the List").split(",")]
y = lambda x : x / 13
res = [y(i) for i in l1]
print(res)
'''

# Write a Python program to display the Fibonacci sequence up to n-th term by using recursive functions
'''
def fibo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fibo(n-1) + fibo(n-2)

n = int(input("Enter the at which u want the fibonacci number "))
print(fibo(n))
'''

# Write a Python program to find the sum of natural numbers up to n using recursive function
'''
def natural(n):
    if n==0:
        return 1
    return n + natural(n-1)
print(natural(5))
'''
