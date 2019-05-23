# Enter number of tests to be run"
def user_input() -> float:
    while True:
        try:
            return int(input("Please Enter Number of Test Greater then 0 : \n"))
        except ValueError:
            print("Enter only Digit number")


input_test=user_input()

#loop through the number enter by user using range function
while input_test<1:
    print("Error Please Enter Number of Test Greater then 0 \n")
    try:
        input_test=user_input()
    except:
        input_test=user_input()

else:
    for _ in range(input_test):
    #split() function seperate 2 numbers enter by user
    #using map function seperate 2 value and assign to variable 'a' and 'b'
        a,b=map(int,input("Enter integers ​ a, b​​ in a single line seperated by space: ") .split())

    #check if 'a' is greater then 0 and b is less then 10000
    #if one of condition false then Repromt user to Enter Correct Value
        while a<1 and b>pow(10,9):
            if a<1:
                print("Please Enter Number One Greater Then 0")
                a,b=map(int,input("Enter integers ​ a, b​​ in a single line seperated by space: ") .split())
            if b>pow(10,9):
                print("Please Enter Number two Less Then ",pow(10,9))
                a,b=map(int,input("Enter integers ​ a, b​​ in a single line seperated by space: ") .split())

        # if Both a and b Condition true 
        if a>=1 and b<=pow(10,9):
        #Check if a is greater then b
            if a>b:
                sum='' #initialise sum variable as blank
                while a>0:
                    mod_a=a%10   # find Module of a number to Extract the last digit
                    a=int(a/10)  # Divide varaible 'a' number with 10 to remove the last digit
                    mob_b=b%10   # find Module of 'b' number to Extract the last digit
                    b=int(b/10)  # Divide b number with 10 to remove the last digit
                    c=(mod_a+mob_b)%10  #find Module of mob_a and mob_b value to Extract the last digit
                    sum=sum+str(c) #Convert Varaible C to String n concatinate or add with sum variable

        #Check if b is greater then a
            elif b>=a:
                sum=''
                while b>0:
                    mob_b=b%10
                    b=int(b/10)
                    mob_a=a%10
                    a=int(a/10)
                    c=(mob_a+mob_b)%10
                    sum=sum+str(c)

            print(sum[::-1]) # Print Reverse Value of Sum Variable


