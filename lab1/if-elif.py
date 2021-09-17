print(" *** Wind classification ***")
d=float(input("Enter wind speed (km/h) : "))
if d>=209 :
 print("Wind classification is Super Typhoon.")
elif d>=102.00 and d<=208.99 :
 print("Wind classification is Typhoon.")
elif d>=56.00 and d<=101.99 :
 print("Wind classification is Tropical Storm.")
elif d>=52.00 and d<=55.99 :
 print("Wind classification is Depression.")
else:
 print("Wind classification is Breeze.")

