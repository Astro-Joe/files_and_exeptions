while True:
    prompt = "Enter a number: "
    number_ = input(prompt)
    number1  = input(prompt)
    
   
    try:
        solve = int(number1) / int(number_)
        print(solve)
    except ZeroDivisionError:
        print("You can't divide by zero!\n")
    except ValueError:
        print('Numbers! not letters!\n')