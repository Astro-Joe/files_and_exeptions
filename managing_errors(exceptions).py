while True:
    prompt = "Enetr a number: "
    try:
        number_ = int(input(prompt))
        number1  = int(input(prompt))

        solve = number1 - number_
        print(solve)
    except ValueError:
        print("Enter a number!\n")
    continue
