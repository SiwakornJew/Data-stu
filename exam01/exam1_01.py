print(" *** Wind classification ***")
num = float(input("Enter wind speed (km/h) : "))

if num < 0:
    print("!!!Wrong value can't classify.")
elif num >= 209:
    print("Wind classification is Super Typhoon.")
elif num>=102.00 and num <=208.99:
    print("Wind classification is Typhoon.")
elif num >= 56 and num<=101.99:
    print("Wind classification is Tropical Storm.")
elif num >= 52 and num<=55.99:
    print("Wind classification is Depression.")
else:
    print("Wind classification is Breeze.")