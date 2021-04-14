count = 0
sum = 0
print('Before', count)
for value in [9, 41, 12, 3, 74, 15]:
    count = count +1
    sum = sum + value
    print(count, value)
print('After', count)
print('After sum= ', sum, 'Average = ', sum/count)

#filtering in a loop
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print('large number', value)
print('After')

found = False
print('Before', found)
for value in [9, 41, 12, 3, 74]:
    if value == 3:
        found = True
    print(found, value)
print('After', found)

smallest = None
print('Before', smallest)
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)

