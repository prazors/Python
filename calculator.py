def btnadd(num1, num2):
    return num1 + num2

def btnsubtract(num1, num2):
    return num1 - num2

def btnmultiply(num1, num2):
    return num1 * num2

def btndivision(num1, num2):


    quotient = (num1 / num2)
    remain = float(num1 % num2)
    remdeci = remain / num2
    if num1 % num2 == 0:
        return quotient
    else:
        return quotient + remdeci

def btnexpo(num1, expo):
    return num1 ** expo
