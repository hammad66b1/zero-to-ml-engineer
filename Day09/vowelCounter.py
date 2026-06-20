s = input("Enter a String: ")
text = s.lower()
an = text.count("a")
en = text.count("e")
in_ = text.count("i")
on = text.count("o")
un = text.count("u")

total = an + en + in_ + on + un
print(f"Total vowels: {total}")