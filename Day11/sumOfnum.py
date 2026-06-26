number=input("Enter a string of numbers: " )
s=0
for num in str(number):
    s+=int(num)

print(f"Sum of numbers is : {s}")