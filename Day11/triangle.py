rows = int(input("Enter number of rows: "))

for n in range(1, rows + 1):
    row = ""
    for x in range(n):
        row += "*"
    print(row)