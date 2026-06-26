num = int(input("Enter a number: "))
is_prime = True
if num<=1:
    print("It is not a prime number: ")
else:
 for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

 if is_prime:
    print("Prime number")
 else:
    print("Not prime")