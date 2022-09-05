
# Print the numbers described in the exercise
for n in range(1,12):
    for i in range(1,n):
        ##last number, add \n
        if(i==n-1):
            print(i)
        else:
            print(i,end= ' ')

