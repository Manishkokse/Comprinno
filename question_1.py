from collections import Counter

#check if user enter number or not
def user_input() -> float:
    while True:
        try:
            return int(input("Enter number of tests to be run between 0 to 10 : \n"))
        except ValueError:
            print("Enter only Digit number")


input_test=user_input()


#if Enter input is less then 0 and greater then 10 Show Error and Reprompt to Enter again
while input_test<1 or input_test>10:
    print("Error Please Enter Number of Test Greater then 0 and less then 10")
    try:
        input_test=user_input()
    except:
        input_test=user_input()

#loop through the number enter by user using range function

for t in range(input_test):
#Enter Some lower String 
    S = str(input("Enter Some lower String : "))
#Check length of string greater then 0 and less then pow(10,5) if its false prompt again to enter
    while len(S)<0 :
        print("Error Please Enter Some lower String")
        S=str(input("Enter Some lower String between 0 to 500") )
    try:
#check if string is alphabatical and in lower case
        if S.isalpha() and S.islower() :
            #calculate each repeted letter in string and store in array 
            f = [y for x, y in Counter(S).most_common()]
            #print(f)
            #resverse array
            f = f[::-1]
            #print(f)
            #check if length of string is greater then 3 and value of index 3 is not equal to addition of index 1 and 2
            if len(f) > 3 and f[3] != f[2] + f[1]:
                #if condition is true swap index value
                f[0], f[1] = f[1], f[0]
            #check lenght of repeated string value array is less then 3 or loop through lenght of array to find current index is equal to range index 
            Dynamic = len(f) < 3 or all(f[i] == f[i - 1] + f[i - 2] for i in range(2, len(f)))
            #print(Dynamic)
        #if result is true then its Dynamic otherwise false
        print('Dynamic' if Dynamic else 'Not Dynamic')
    except ValueError:
        print("please enter some lower case string")
        S = str(input("Enter Some lower String : "))
