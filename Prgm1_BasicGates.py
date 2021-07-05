def main():
    a=False
    b=True
    print("Not operation of a= ",not(a))
    print("OR operation of a and b= ",(a or b))
    print("AND operation of a and b= ", (a and b))
    print("XOR operation of a and b= ", (a ^ b))
    print("XNOR operation of a and b= ", not(a ^ b))
    print("IMPLICATION of a and b= ", imp(a,b))
    print("BIDIRECTIONAL operation of a and b= ",bidir(a,b))


def imp(a,b):
   return (not(a)) or b

def bidir(a,b):
    return (imp(a,b) and imp(b,a))

if __name__ == '__main__':
    main()
