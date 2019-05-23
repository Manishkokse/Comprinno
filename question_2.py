
#check if user enter number or not
def user_input() -> float:
    while True:
        try:
            return int(input("Enter number of tests to be run between 0 to 1000 : \n"))
        except ValueError:
            print("Enter only Digit number")


input_test=user_input()

#loop through the number enter by user using range function
#if Enter input is less then 0 and greater then 1000 Show Error and Reprompt to Enter again
while input_test<1 or input_test>1000:
    print("Error Please Enter Number of Test Greater then 0 and less then 1000")
    try:
        input_test=user_input()
    except:
        input_test=user_input()

for _ in range(input_test):
#using map function split the input value and store it in 3 variable 
    s11,s12,s13 = map(int, input("Please Enter Number Greater then 0 and less then 100 ex. 1 2 3 :\n").split())

# check value enter is greater then 0 and less then 100 
    while (s11<1 or s12<1 or s13<1) or (s11>100 or s12>100 or s13>100) :
        print("Error Please Enter Number Greater then 0 and less then 100")
        s11,s12,s13 = map(int, input("Error Please Enter Number Greater then 0 and less then 100 ex. 1 2 3 :\n").split())

# check value enter is greater then 0 and less then 100 
    s21,s22,s23 = map(int, input("Enter Another Combination 2\n").split())
    while (s21<1 or s22<1 or s23<1) or (s21>100 or s22>100 or s23>100) :
        print("Error Please Enter Number Greater then 0 and less then 100")
        s21,s22,s23 = map(int, input("Error Please Enter Number Greater then 0 and less then 100000000 ex. 1 2 3 : \n").split())

# check value enter is greater then 0 and less then 100 
    s31,s32,s33 = map(int, input("Enter Another Combination 3\n").split())
    while (s31<1 or s32<1 or s33<1) or (s31>100 or s32>100 or s33>100) :
        print("Error Please Enter Number Greater then 0 and less then 100")
        s31,s32,s33 = map(int, input("Error Please Enter Number Greater then 0 and less then 100erewrwer ex. 1 2 3 : ").split())
    q = 0
    #print(s11,s12,s13)
#Check here who's value is greater then other by comparing with each other
    if (s11<=s21 and s12<=s22 and s13<=s23) or (s11>=s21 and s12>=s22 and s13>=s23):
        if (s11<s21 or s12<s22 or s13<s23) or (s11>s21 or s12>s22 or s13>s23): 
            q+= 1
    if (s21<=s31 and s22<=s32 and s23<=s33) or (s21>=s31 and s22>=s32 and s23>=s33):
        if (s21<s31 or s22<s32 or s23<s33) or (s21>s31 or s22>s32 or s23>s33):
            q+= 1
    if (s11<=s31 and s12<=s32 and s13<=s33) or (s11>=s31 and s12>=s32 and s13>=s33):
        if (s11<s31 or s12<s32 or s13<s33) or (s11>s31 or s12>s32 or s13>s33):
            q+= 1
    print ("yes" if q==3 else "no")
