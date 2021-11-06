import random

cc_num0 = random.randint(1000, 9999)
cc_num1 = random.randint(1000, 9999)
cc_num2 = random.randint(1000, 9999)
cc_num3 = random.randint(1000, 9999)

cc_ccv = random.randint(100, 999)

cc_date13 = random.randint(1, 12)
cc_date14 = random.randint(2021, 2027)

print(f"{cc_num0}{cc_num1}{cc_num2}{cc_num3}|{[0,cc_date13]if cc_date13<=9 else cc_date13}|{cc_date14}")