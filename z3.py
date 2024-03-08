def getAvg():
    sumOfNums = 0
    for num in lstNum:
        sumOfNums += num
    average = sumOfNums / len(lstNum)
    return average

lstNum = []
while True:
    userInput = input()

    if(userInput == "Done"):
        break

    try:
        lstNum.append(int(userInput))
    except:
        print("Unos nije valjan.")
        
print(len(lstNum))
lstNum.sort()
print(lstNum)
print(min(lstNum))
print(max(lstNum))
avg = getAvg()
print(avg)