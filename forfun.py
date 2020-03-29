#hledání narcistických čísel
#https://twitter.com/fermatslibrary/status/1243532484991684615
#číslo je narcistické, pokud je součet jeho čísel na počet čísel 153=1 na třetí plus 2 na třetí plus 3 na třetí

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
        

narcissisticNumbers(1000000)