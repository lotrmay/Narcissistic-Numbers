
def narcissisticNumbers(numOfDigits):
    ret=[]
    length=len(str(numOfDigits))
    for x in range(numOfDigits,numOfDigits*10):
        cislo=0
        for cislice in range(length):
            cislo+=pow(int(str(x)[cislice]),length)
        if(cislo==x):
            ret.append(x)
    print(ret)
        

narcissisticNumbers(100)
