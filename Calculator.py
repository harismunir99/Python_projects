
def calculator():
    
    # Initialize variables 
    
    first_number = 0
    second_number = 0
    function = ""
    
    # get first number from user
    while True:
        try:
            first_number = float(input("Please enter a number: "))
            break
        except:
            print("Invalid input. Please try again")
            
            
    # get operation from user 
    while True:
        try:
            function = input("Please choose an operator (+, -, /, *): ")
            if (function in ['+','-','/','*']):
                break
        except:
            print("Invalid input. Please try again")
            
            
    # get second number from user 
    while True:
        try:
            second_number = float(input("Please enter a number:  "))
            break
        except:
            print("Invalid input. Please try again.")
            
            
            
    # perform calculations
    if (function == "+"):
        result = first_number + second_number
    elif (function == "-"):
        result = first_number - second_number
    elif (function == "*"):
        result = first_number * second_number
    elif (function == "/"):
        result = first_number / second_number
    else:
        result = "Invalid operator"
        
        
    # print result to user
    print("Your result is: " , result)
    print("\n")

        
    
    
            
    







if __name__ == "__main__":
    
    # loop
    while True:
        calculator()
