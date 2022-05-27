# Recursive Integer Multiplication Algorithm
Written in Python 3.
by JKL

Summary: Using Karatsuba Multiplication, we can recursively multiply n digit integers, single-digits at a time. 

## Thought Process: 
#### Base Case:  
  if n is less than or equal to 2:
  * Separate input into single digits, a, b, and c, d. 
  * Multiply and form terms ab, (ad + bc), and bd.
  * return (*)Star Equation: ```10 ** n * ac + 10 ** (n // 2) * (ad + bc) + bd``` 
#### Recursive Steps:
  Separate input digits into a, b and c, d halves.\
  <br>Recursively solve for ```a * c```, ```a * d + b * c```, and ```b * d```<br/>
  <br>Input the corresponding terms into the star equation and return result.<br/>

## To user: 
Input your desired "multiplier" and "multiplicand" in the corresponding variables.\
<br>Your inputs have to be integers in powers of 2, i.e. 2, 4, 8, 16 . . . 2^n <br/>

### Note: 
Integers in python are much more precise than floats Python. The star equation is explicitly cast as an integer, but this can be changed if desired. 




