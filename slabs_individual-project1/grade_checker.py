#Author Lemart

#entering the raw marks for the practical and theory assesments
practical_mark = float(input("Enter your practical mark(0-100): "))
theory_mark = float(input("Enter your theory mark(0-100): "))

#Calculating the final mark
final_mark = (practical_mark * 0.4) + (theory_mark * 0.6)

"""
if the final_mark // 50 = 0, "Fail"
if the final_mark // 50 = anything more than 0, "Pass"
"""
status = ("Fail!" * (1 - int(final_mark // 50))) + ("Pass!" * int(final_mark // 50))


#prints the results
print("Your final mark: ", final_mark)
print("Status: ", status)
