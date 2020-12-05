x = int(input("Enter the Amount in the bill : "))
y = int(input("Enter the cash amount recieved : "))


z= y-x
print("The balance amount is ",z)


def computeChange(self,payment):
        billAmount = int(self.billAmount)
        paidAmount = int(self.paidAmount)
        currencyAvailable = [2000,500,200,100,50,20,10,5,2,1]
        changeDenomination = []
        change = 0

        if(paidAmount > billAmount):
            change = paidAmount - billAmount
            while change>0:
                for i in currencyAvailable:
                    if i <= change:
                        changeDenomination.append(i)
                        change-=i
                        break
        print(changeDenomination,"="+str(paidAmount-billAmount))
    
