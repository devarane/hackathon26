def countchars(st):
    count = 0
    for ch in st:
        if ch != " " and ch != "." and ch != "!" and ch != ",":
            count = count + 1
    return count


print(countchars("Listen, Mr. Jones, calm down.") == 21)
print(countchars("hello") == 5)
print(countchars("") == 0)
print(countchars("r2?") == 3)
print(countchars("Hi!!!") == 2)
print(countchars("a b,c.d!") == 4)

s = input("Enter a string: ")
print(countchars(s))
