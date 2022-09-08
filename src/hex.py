import sys

# This program should take two arguments, a command--either "encode" or "decode"--
# and then a string.

if len(sys.argv) != 3:
    print("Incorrect number of arguments.", file=sys.stderr)
    print(f"Usage: {sys.argv[0]} command string\n", file=sys.stderr)
    sys.exit(1)

command, x = sys.argv[1:3]

match command:
    case "encode":
        # Implement the encoding here
        #transform chars -> int (unicode) -> hexadecimal -> join
        hexadecimal = [hex(ord(i)) for i in x]
        encoding = ''.join(hexadecimal)
        print(encoding)

    case "decode":
        # Implement the decoding here
        split_hex = x.split('0x')
        #throw away the first element -> start range at 1
        decoding = ''
        for i in range(1,len(split_hex)):
            ord = int(split_hex[i], base = 16)
            decoding += chr(ord)
        print(decoding)
