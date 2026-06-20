
#amount is let's say 2660
#2660/5000=0
#2660/1000=2
#2660/500=5
#2660/100=26
#2660/50=53
#2660/10=266
#2660/1=2660

amount = int(input("Enter amount in rupees: "))

n5000 = amount // 5000
amount = amount - (n5000 * 5000)

n1000 = amount // 1000
amount = amount - (n1000 * 1000)

n500 = amount // 500
amount = amount - (n500 * 500)

n100 = amount // 100
amount = amount - (n100 * 100)

n50 = amount // 50
amount = amount - (n50 * 50)

n10 = amount // 10
amount = amount - (n10 * 10)

n5 = amount // 5
amount = amount - (n5 * 5)

n1 = amount // 1

print("5000 x", n5000)
print("1000 x", n1000)
print("500 x", n500)
print("100 x", n100)
print("50 x", n50)
print("10 x", n10)
print("5 x", n5)
print("1 x", n1)