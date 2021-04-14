astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
    
print('First', istr)

raw_str = input('Enter a number: ')
try:
    ival = int(raw_str)
except:
    ival = -1

if ival > 0:
    print('Nice work')
else:
    print('Not a number')