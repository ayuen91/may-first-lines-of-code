principle = 0
rate = 0
time = 0
import math
while principle <= 0:
    principle = float(input("Enter the principle amount: "))
while rate <= 0:
    rate = float(input("Enter the rate amount: "))
while time <= 0:
    time = int(input("Enter the time amount: "))

compound_Interset = principle * math.pow((1 + rate * 0.01), time) 
print (f"copound interest for the principle amount ${principle:,} at the rate of {rate}% for the period of {time} year/s is ${compound_Interset:,.2f}")   