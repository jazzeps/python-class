n=int(input('please enter an integer between 1 and 9999: '))
n_str = str(n)
n_list = []
for item in n_str:
    n_list.append(item)
n_list.reverse()
        
if len(n_list) < 4:
    thousands = ''
elif n_list[3] == '1':
    thousands = 'one thousand'
elif n_list[3] == '2':
    thousands = 'two thousand'
elif n_list[3] == '3':
    thousands = 'three thousand'
elif n_list[3] == '4':
    thousands = 'four thousand'
elif n_list[3] == '5':
    thousands = 'five thousand'
elif n_list[3] == '6':
    thousands = 'six thousand'
elif n_list[3] == '7':
    thousands = 'seven thousand'
elif n_list[3] == '8':
    thousands = 'eight thousand'
elif n_list[3] == '9':
    thousands = 'nine thousand'
    
if len(n_list) < 3 or n_list[2] == '0':
    hundreds = ''
elif n_list[2] == '1':
    hundreds = 'one hundred'
elif n_list[2] == '2':
    hundreds = 'two hundred'
elif n_list[2] == '3':
    hundreds = 'three hundred'
elif n_list[2] == '4':
    hundreds = 'four hundred'
elif n_list[2] == '5':
    hundreds = 'five hundred'
elif n_list[2] == '6':
    hundreds = 'six hundred'
elif n_list[2] == '7':
    hundreds = 'seven hundred'
elif n_list[2] == '8':
    hundreds = 'eight hundred'
elif n_list[2] == '9':
    hundreds = 'nine hundred'
    
if len(n_list) == 1 or n_list[1] == '0':
    tens = ''        
elif n_list[1] == '1':
    if n_list[0] == '0':
        tens = 'ten'
    elif n_list[0] == '1':
        tens = 'eleven'
    elif n_list[0] == '2':
        tens = 'twelve'
    elif n_list[0] == '3':
        tens = 'thirteen'
    elif n_list[0] == '4':
        tens = 'fourteen'
    elif n_list[0] == '5':
        tens = 'fifteen'
    elif n_list[0] == '6':
        tens = 'sixteen'
    elif n_list[0] == '7':
        tens = 'seventeen'
    elif n_list[0] == '8':
        tens = 'eighteen'
    elif n_list[0] == '9':
        tens = 'nineteen'    
elif n_list[1] == '2':
    tens = 'twenty'
elif n_list[1] == '3':
    tens = 'thirty'
elif n_list[1] == '4':
    tens = 'forty'
elif n_list[1] == '5':
    tens = 'fifty'
elif n_list[1] == '6':
    tens = 'sixty'
elif n_list[1] == '7':
    tens = 'seventy'
elif n_list[1] == '8':
    tens = 'eighty'
elif n_list[1] == '9':
    tens = 'ninety'
    
if n_list[0] == '0' or (len(n_list) > 1 and n_list[1] == '1'):
    ones = ''
elif n_list[0] == '1':
    ones = 'one'
elif n_list[0] == '2':
    ones = 'two'
elif n_list[0] == '3':
    ones = 'three'
elif n_list[0] == '4':
    ones = 'four'
elif n_list[0] == '5':
    ones = 'five'
elif n_list[0] == '6':
    ones = 'six'
elif n_list[0] == '7':
    ones = 'seven'
elif n_list[0] == '8':
    ones = 'eight'
elif n_list[0] == '9':
    ones = 'nine'
    
    
if hundreds != "" and len(n_list) > 3:
    th= ' '
else:
    th = ''
    
if tens != "" and len(n_list) > 2:
    ht= ' '
else:
    ht = ''

if ones != "" and len(n_list) > 1:
    to= ' '
else:
    to = ''

print(thousands, sep='', end='')
print(th, sep='', end='')
print(hundreds, sep='', end='')
print(ht, sep='', end='')
print(tens, sep='', end='')
print(to, sep='', end='')
print(ones, sep='', end='')