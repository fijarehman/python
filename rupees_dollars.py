def rupees_to_dollars(rupees):
    return rupees / 82.5

#  temprature converter : celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    return(celsius * 9/5) + 32

# length converter: inches to feet
def inches_to_feet(inches):
    return inches / 12

#  main program
print("conversion utility")
print("1. rupees to dollars")
print("2. celsius to fahrenheit")
print("3. inches to feet")

choice = int(input("enter your choice (1-3): "))

if choice == 1:
    r = float(input("enter amount in rupees: "))
    print("dollars:", rupees_to_dollars(r))
elif choice == 1:
    r = float(input("enter amount in rupees: "))
    print("dollars:", celsius_to_fahrenheit(r))
elif choice == 3:
    i = float(input("enter length in inches: "))
    print("feet:", inches_to_feet(i))
else:
    print("invelid choice!")
    