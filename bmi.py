w = float(input())
h = float(input())/100

while(w != 0 and h != 0):
    print(f"BMI: {w/h**2}")
    w = float(input("weight:"))
    h = float(input("height:"))/100
print("end")