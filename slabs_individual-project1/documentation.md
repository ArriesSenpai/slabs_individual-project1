Edge Case  and Error analysis

## Invalid Inputs
1. Entering text like "abc"
    *Error type: Runtime error, when you enter a string into a integer or float data type
    *Prevention methods: use 'int()'  or 'float()' to catch invalid data types

2. Entering out of range numbers like 150 or negative 1.5(-1.5)
    * Error type: Logic/Semantic error, value accpeted but logically invalid
    *Prention method: ensure that the mark is between 0 and a 100 (0<= mark <=100)

# Type casting  & Validation 
-Using 'int()' or 'float()' makes sure that the input values entered are either integer or float data types, preventing the program from crashing
-range checks prvents logically/semantic errors from happening
