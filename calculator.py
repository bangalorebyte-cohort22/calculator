def do(w,n1,n2):
    '''returns the result with n1 and n2 doing the operation w and raises error if w is div and n2 is 0 (denominator is 0)'''
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
def input_check(user_input):
    '''returns None and raises error if the format of user_input is incorrect'''
    if len(user_input)!=3:
        print("Please enter either: div, mul, add, sub followed by 2 numbers separated with spaces")
        raise "Error"
    if not((user_input[1][1:].isdigit() or len(user_input[1])<2) \
           and (user_input[2][1:].isdigit() or len(user_input[1])<2))\
       or not(user_input[1][0]=="-" or user_input[1][0].isdigit()) \
       or not(user_input[2][0]=="-" or user_input[2][0].isdigit()):
        # If second and third element in the list user_input don't have number \
        # or - as their first digit or (have non-number in rest of the digits and length of it > 1)
        print(user_input[1][0].isdigit(),user_input[2][0].isdigit())
        print ("Not two integers entered. Please enter two integers numbers.")
        raise "Error" 
    if not(user_input[0] in ["div","mul","add","sub"]): # If the operation is invalid
        print("Invalid operaion entered, please enter one of div, mul, add or sub followed by 2 numbers separated by spaces")
        raise "Error"
def calc():
    '''returns None but takes input commands for calculation from the user and prints the results after calculations'''
    print("Welcome to calculator")
    while 1: # Keep the calculator running
        user_input = input("Enter your maths operation and numbers or q to quit: ").split()
        if "q" in user_input[:1] or "Q" in user_input[:1]: # Quit if q is passed as an input
            return None
        else:
            try:
                input_check(user_input)
                print(do(user_input[0].lower(),int(user_input[1]),int(user_input[2]))) # Pass correct parameters to do fuction
            except:
                pass
calc()