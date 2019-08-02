
#The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
#Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

thousandDigitNumber = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
#split thousand digit number into individual characters
thousandDigitList = [char for char in thousandDigitNumber]

print(thousandDigitList)

largestValue = 0
count = 0
#for each digit in list, identify next next 12 characters and find product. If product is greater than the currently largest product, then save.
for digit in thousandDigitList:
    try:
        firstFactor = thousandDigitList[count]
        secondFactor = thousandDigitList[count+1]
        thirdFactor = thousandDigitList[count+2]
        fourthFactor = thousandDigitList[count+3]
        fifthFactor = thousandDigitList[count+4]
        sixthFactor = thousandDigitList[count+5]
        seventhFactor = thousandDigitList[count+6]
        eighthFactor = thousandDigitList[count+7]
        ninthFactor = thousandDigitList[count+8]
        tenthFactor = thousandDigitList[count+9]
        eleventhFactor = thousandDigitList[count+10]
        twelvethFactor = thousandDigitList[count+11]
        thirteenthFactor = thousandDigitList[count+12]
    except:
        continue
    count +=1
    multipliedValue = int(firstFactor) * int(secondFactor) * int(thirdFactor) * int(fourthFactor) * int(fifthFactor) * int(sixthFactor) * int(seventhFactor) * int(eighthFactor) * int(ninthFactor) * int(tenthFactor) * int(eleventhFactor) * int(twelvethFactor) * int(thirteenthFactor)
    print("multipliedValue: %d" % multipliedValue)
    if(multipliedValue > largestValue):
        largestValue = multipliedValue
        largestFirstFactor = firstFactor
        largestSecondFactor = secondFactor
        largestThirdFactor = thirdFactor
        LargestFourthFactor = fourthFactor

print("largestValue: %d, firstFactor: %d, secondFactor: %d, thirdFactor: %d, fourFactor: %d" % (largestValue, int(largestFirstFactor), int(largestSecondFactor), int(largestThirdFactor), int(LargestFourthFactor) ))