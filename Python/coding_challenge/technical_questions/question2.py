# Create  a  function  that  calculates  the  power  of  a  number.
# Then  write  a  unit  test  to  check  the  correctness  of  the function

def power_of_number(base, exponent):
    result = 1

    while exponent != 0:
        result *= base
        exponent -= 1

    return result




result1 = power_of_number(2, 3)
result2 = power_of_number(6, 3)
print(result1)
print(result2)


# Alternately
def power(base, exponent):

    while exponent != 0:
        result = base ** exponent
        exponent -= 1
        return result


res = power(3,3)
print(res)