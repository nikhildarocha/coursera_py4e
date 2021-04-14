hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter a numeric input")
    quit()
    
val_2 = h%40
if val_2 > 0:
    new_hrs = h-val_2
    new_r = float(1.5*r)
    gross = float(val_2)*new_r + new_hrs*r
    print(gross)