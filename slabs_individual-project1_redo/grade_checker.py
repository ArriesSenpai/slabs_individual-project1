#Author Lemart Bennee

#entering the raw marks for the practical and theory marks

def mark_calculator():
    """
    this functions takes the practical and theory mark to see if the student passed or failed
    """
    practical_mark = float(input("Enter your practical mark(0-100): "))
    theory_mark = float(input("Enter your theory mark(0-100): "))

    final_mark = (practical_mark * 0.4) + (theory_mark * 0.6)
    
    passed = final_mark <= 50
    failed = final_mark >= 50
    
    print("Final Mark: ", final_mark)
    print("Failed: ", failed)
    print("Passed: ", passed)

mark_calculator()
