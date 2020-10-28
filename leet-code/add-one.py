def plusOne(digits):
    num = ""
    summed = []
    for i in digits:
        num = num + str(i)
    
    # Incriment integer and turn back to string
    num = str(int(num) + 1)
    print(num)
    for i in num:
        summed.append(int(i))

    return(summed)

print(plusOne([9]))