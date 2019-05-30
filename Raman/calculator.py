def do(w,n1,n2): # A fuction to subtract, add, multiply and divide
    if w=="add":
        return n1+n2
    elif w=="sub":
        return n1-n2
    elif w=="div":
        if n2==0:
            print("You cannot have 0 in the denominator")
        return "Quotient is: "+str(int(n1//n2))+", remainder is: "+str(int(str(n1%n2)))
    elif w=="mul":
        return n1*n2
    else:
        raise "Error"
def calc():
    print("Welcome to calculator")
    while 1:
        ainput=input("")
        if ainput=="q":
            return None
        else:
            try:
                print(do(ainput.split()[0].lower(),int(ainput.split()[1]),int(ainput.split()[2])))
            except:
                pass

calc()
