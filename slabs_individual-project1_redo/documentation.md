Edge Case & Error Analysis


#Invalid Inputs
1. Entering teext like "abc", the Erro type is a Runtime error, when you enter a string into a integer or a float data type.
Prevention methods: use int() or float() to catch invalid data types

2. Entering out of range numbers like 150 or negative 1.5(1.5), the error type is Logic/Semantic error, value accepted but logically invalid. 
Prevention methods: make sure that the mark is between 0 and a 100 (0<= mark <=100)

Type Casting & Validation
Using int() or float() makes sure that the input values entered are either integer or float data types, doing this will help prevent the program from crashing. Range check prevents logically/semantic errors from happening 
