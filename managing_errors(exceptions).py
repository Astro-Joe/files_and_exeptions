while True:
    print("Enter 'q' to quit")
    prompt = "Enter a number: "
    number_ = input(prompt)
    if number_ == 'q':
        break
    number1  = input(prompt)
    if number1 == 'q':
        break
    
   # The except block can be used as much as possible
    try:
        solve = int(number1) / int(number_)
        
    except ZeroDivisionError:
        print("You can't divide by zero!\n")
    except ValueError:
        print('Numbers! not letters!\n')
    else:
        print(str(solve) + '\n')