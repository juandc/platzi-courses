"""
factorial = 5
acum = 1
while factorial>0:
    acum = acum * factorial
    factorial = factorial -1
    print "%i" % acum
print "Resultado : %i" % acum
"""

# 5!  = 5 * 4!
# 10! = 10 * 9!
# 9!  = 9 * 8!
#...
# 2! = 2 * 1
# 1! = 1 * 0 = 1

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x -1)

print factorial(10)
