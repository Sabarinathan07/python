str = input("Enter a Sentence : ")
x = str.split()
for a in range(-1,-len(x)-1,-1):
    print(x[a],end=" ")
