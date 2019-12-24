num = int( input() )

for i in range( 1, num+1 ):

    if i%15==0:
        print(i)
    elif i%3==0 or i%5==0:
        continue
    else:
        print(i)
    