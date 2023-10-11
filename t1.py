
l1=list(range(1,11,2))
print(l1)

print("Prime numbers between", 1, "and", 10, "are:")
l2=[]
for num in range(1, 11):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           l2.append(num)
print(l2)
l3=l1+l2
print(l3)
print("Length of l3:",len(l3))
print("Count the number of occurance of 5 in l3:",l3.count(5))
#Add number 10 to l3.
l3.append(10)
print("l3 unsorted:",l3)
l3.sort()
l3.reverse()
print("l3 sorted:  ",l3)
l=list(map(lambda  x:0 if x%2==0 else x,l3))
print(l)
# Q2: Using keys and indexing, grab the 'hello' from the following dictionaries
d = {'k1': {'k2': 'hello'}}
print(d['k1']['k2'])

d = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print(d['k1'][0]['nest_key'][-1][0])

d = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}
print(d['k1'][-1]['k2'][1]['tough'][-1][0])

#Q3: Use list comprehension to create a list of all
# numbers between 1 and 50 that are divisible by 3.
l4=[]
for i in range(1,51):
    if i%3==0:
        l4.append(i)
print(l4)

# Q4: Write a code to find if a positive integer is prime or not.
num=int(input("Enter Number: "))
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

# Generate the numbers of the Fibonacci sequence that are less than 10,000,000.
def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib

a=fibonacci(100)
print(a)