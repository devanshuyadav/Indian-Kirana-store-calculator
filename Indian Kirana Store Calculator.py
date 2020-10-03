# a more interactive calulator


sum = 0

ans = input(str('''DO WANT TO USE THE CALCULATOR?
 Enter y for yes\n'''))

while(True):


    if ans == "y" or ans == "Y":


        while (True):
            userInput = (input("Enter the item price or press q to quit:  \n"))
            if (userInput != 'q'):
                sum = sum + int(userInput)
                print(f"Order total so far: {sum}")
            else:
                print(f"Your bill total is {sum}")
                print('''Thanks for using calculator
Made by: Gurpreet Singh Kochar''')
                break

    else:
        print("""OK.
COME WHEN WANT TO USE IT.""")


    ans2=input(str('''DO WANT TO USE THE CALCULATOR AGAIN?
 Enter y for yes\n'''))

    if ans2 == "y":
        continue
    else:print("""Ok.
VISIT OUR STORE AGAIN.""")
    break
