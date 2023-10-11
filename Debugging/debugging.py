
import pdb #very useful in terms of tracing codes with debugging

###debugging.py####
def function(num1):
    import pdb; pdb.set_trace()
    return num1 + num1


def function(num1):
    import pdb; pdb.set_trace()
    return int(num1) * int(num1)

number1 = int(input("Enter Number"))
result1 = function(number1)
result2 = function(result1)

import pdb; pdb.set_trace() ##adding for the sake of printing the second result2

print(result2)

1. python debugging.py
2. check the end result of function with 'step'
   2.1 using p result1 -> gives the result of resul1
   2.2 using p result2 -> does not give since pdb.set_trace is before result2, adding after result2 for the sake of tracing
3. check where you are in set_trace (shows all the codes) with 'l'
4. step over the next line with 'n'
5. then you can cgeck with 'l' to see if you moved to a line down

