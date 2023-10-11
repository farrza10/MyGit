
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

print(result2)

1. python debugging.py
2. check the result with 'step'
3. check where you are in set_trace (shows all the codes) with 'l'
4. step over the next line with 'n'
5. then you can cgeck with 'l' to see if you moved to a line down

