heating = 0
cooling = 0

temp = int(input("Enter the average daily temperature: "))
while temp >= -459:
    if temp < 60:
        heating = heating + 1
    elif temp > 80:
        cooling = cooling + 1
    temp = int(input("Enter the average daily temperature: "))

print("Heating days:", heating)
print("Cooling days:", cooling)
