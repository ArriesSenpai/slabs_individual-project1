#Author Lemart

#entering the raw marks for the practical and theory assesments
practical_mark = float(input("Enter your practical mark(0-100): "))
theory_mark = float(input("Enter your theory mark(0-100): "))

#Calculating the final mark
final_mark = (practical_mark * 0.4) + (theory_mark * 0.6)

"""
Boolean function
if its greater or equal to 50 its true which is (1) 
if its less than 50 its a false which is (0)
:status: this will tell us if they passed or not 
"""
status = ("Fail!", "Pass!")[final_mark >=50]

#prints the results
print("Your final mark: ", final_mark)
print("Status: ", status)
