a=int(input("Enter a number:"))
b=0                                         #is_prime=True
for i in range(2,a):
    if(a%i==0):
        b+=1
        break                                #is_prime=False
if(b==0):                                   #if is_prime:
    print("Given number is a prime number")
else:
    print("Given number is not a Prime number")
