#Created Dictionary 
Table={
	'B':'BattleShip',
	'C':'Cruiser',
	'D':'Destroyer',
	'F':'Frigate'
}

#check if user enter number or not
def user_input() -> float:
    while True:
        try:
            return int(input("Enter number of tests to be run between 0 to 1000 : \n"))
        except ValueError:
            print("Enter only Digit number")


input_test=user_input()

#loop through the number enter by user using range function
#if Enter input is less then 0 and greater then 10 Show Error and Reprompt to Enter again
while input_test<1 or input_test>1000:
    print("Error Please Enter Number of Test Greater then 0 and less then 1000:\n")
    try:
        input_test=user_input()
    except:
        input_test=user_input()
for i in range(input_test):
#Code to enter id from a dict to output its equivalent value
    try:
        print(Table[str(input("Please Enter Letter B or C or D or F\n")).upper()])
    except :
#if wrong id enter handel exception and promt to Re-Enter
        print("Error : Please Enter Letter B or C or D or F\n")
        print(Table[str(input("Please Enter Letter B or C or D or F\n")).upper()])
