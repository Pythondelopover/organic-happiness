def tekshirish(javob, num1, num2, amal):
    if amal == '-':
        result = int(num1)-int(num2)
    elif amal == '+':
        result = int(num1)+int(num2)
    if result == javob:
        return True
    else:
        return False