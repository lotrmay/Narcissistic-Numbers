#small python function which can tell you which numbers are narcissistic more on that here:https://twitter.com/fermatslibrary/status/1243532484991684615
def narcissisticNumbers(numOfDigits):
    ret=[]
    length=len(str(numOfDigits))
    for x in range(numOfDigits,numOfDigits*10):
        number=0
        for digit in range(length):
            number+=pow(int(str(x)[digit]),length)
        if(number==x):
            ret.append(x)
    print(ret)
        

narcissisticNumbers(100)
