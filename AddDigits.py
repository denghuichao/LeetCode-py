def addDigits(num):
    """
    :type num: int
    :rtype: int
    """

    while num >= 10:
        sum = 0
        while num > 0:
            sum, num = sum + (num % 10), num / 10

        num = sum

    return num


print (addDigits(10))
