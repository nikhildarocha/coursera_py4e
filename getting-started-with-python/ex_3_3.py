
score = input("Enter Score: ")

try:
    sc = float(score)
except:
    print('Error enter numeric')
    quit()
    
if sc > 1.0:
    print("Error: Out of range")
elif (0.0< sc <1.0):
    if sc >= 0.9:
        print('A')
    elif sc >= 0.8:
        print('B')
    elif sc >= 0.7:
        print('C')
    elif sc >= 0.6:
        print('D')
    else :
        print('E')
else:
    print('Score is too less')