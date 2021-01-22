allGuest={"Alice":{"apple":5, "pretzels":12},"Bob":{"sanwiches":3,"apple":2},"Carol":{"cups":3, "apple pies":1}}

for i,j in allGuest.items():
    print(i,j)

def totalBrought(guest,item):
    numBrought=0

    for i,j in allGuest.items():
        numBrought=numBrought+j.get(item,0)
    return numBrought

print("   - Apples  " + str(totalBrought(allGuest,"apple"))+" pieces")
print("   - Pretzels  " + str(totalBrought(allGuest,"pretzels"))+" pieces")
print("   - Sanwiches  " + str(totalBrought(allGuest,"sanwiches"))+" pieces")
print("   - Cups  " + str(totalBrought(allGuest,"cups"))+" pieces")
print("   - Apple pies  " + str(totalBrought(allGuest,"apple pies"))+" pieces")