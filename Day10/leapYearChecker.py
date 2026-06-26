"""Part 1: A year is a leap year if it's divisible by 4.

Example: 2024 % 4 == 0 → True → leap year so far.
Part 2 — the tricky exception: 
BUT if the year is also divisible by 100 (like 1900, 2000, 2100),
then dividing by 4 isn't enough anymore. In that special case,
it ALSO needs to be divisible by 400 to count as a leap year."""

year= int(input("Enter the year: "))

if year%4==0:
    if year%100==0:
      if year%400==0:
          print("Its a leap year")
      else:
          print("Its not a leap year")
    else:
        print("Its a leap year")
else:
    print("Its not a leap year")