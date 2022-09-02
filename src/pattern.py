
# Print the pattern
max = 10
for n in range(1,max):
    line = ''
    if (n - 1 < max/2):
        line = n*'* '
    else:
        line = (max-n)*'* '
    print(line.strip())

        
