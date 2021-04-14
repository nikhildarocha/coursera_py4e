hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error ...Please enter numeric")
    quit()

def computepay(h, r):
    val_2 = h%40
    if val_2 > 0:
        new_hrs = h-val_2
        new_r = float(1.5*r)
        gross = float(val_2)*new_r + new_hrs*r
        return gross
    
p = computepay(h,r)
print("Pay",p)