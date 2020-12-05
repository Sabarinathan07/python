import re

str = input("Enter a char and num[0-99] : ")

splitStr = str.split()

for x in splitStr:

    temp = re.compile("([a-zA-Z]+)([0-9]+)") 
    tupleStr = temp.match(x).groups() 

    character1 = tupleStr[0]
    numberStr = tupleStr[1]

    num = int(numberStr)

    print(character1*num)
