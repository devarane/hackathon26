limit = int(input())
speed = int(input())
over = speed - limit

if speed <= limit - 10:
    print(50)
elif over >= 6 and over <= 20:
    print(75)
elif over >= 21 and over <= 40:
    print(150)
elif over > 40:
    print(300)
else:
    print(0)
