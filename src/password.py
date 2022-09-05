import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False

# Do all the requirement checks here.
for c in password:
    if(c.islower()):
        lower = 1
    if(c.isupper()):
        upper = 1
    if c in "$#@":
        special_c = 1

if (lower == 1 & upper == 1 and special_c==1 and len(password)>= 6 and len(password)<=12):
    is_valid= True

print(is_valid)
