str = input()

str_list = str.split(' ')

new_str = ''
for s in str_list:
    new_str += s[::-1]+' '

print( new_str )