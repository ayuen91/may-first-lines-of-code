weight = float(input("Enter your weight: "))
unit = input("Enter your unit (L for lbs, K for kg): ").lower()

if unit in("k", "k"):
    converted_weight = weight * 2.205
    print(f"Your weight is {converted_weight:.2f} Lbs")
elif unit in ("L", "l"):
    converted_weight = weight / 2.205
    print(f"Your weight is {converted_weight:.2f} Kgs")
else:
    print(f"Invalid unit: {unit}")