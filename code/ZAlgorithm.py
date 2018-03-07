from array import array
import sys

pattern = input('Enter the pattern  ')
text = input('Enter the text  ')

if(len(pattern) > len(text)):
        sys.exit('Text has to be at least the same length as pattern')        

input = pattern+'$'+text

def printResult(zArray, pattern):

        checker = False
        indexMatch = -1
        for i in range(len(pattern)+1, len(zArray)):
                if zArray[i] == len(pattern):
                        checker = True
                        indexMatch = i-len(pattern)-1
                        break
        print(zArray.tolist())
        if checker == True:
                print('Pattern is present in the text')
                print('The index within the text where the pattern matches has value '+str(indexMatch))
                print('Important! I am considering indices starting at zero!!!')
        else:
                print('Pattern is not present in the text')
           

#for each character, compute the longest substring starting at its position that is also a prefix for the concatenated string

def findLengthLongestPrefix(index, currentLength, input):

    result = currentLength
    currentTextIndex = index+currentLength

    indexPrefixStart = 0
    if currentLength == 0:
        indexPrefixStart = 0
    else:
        indexPrefixStart = currentLength    
    
    for currentPrefixIndex in range(indexPrefixStart, len(input)):
        if currentTextIndex < len(input) and input[currentTextIndex] == input[currentPrefixIndex]:
                #print('current text index is '+str(currentTextIndex)+' current prefix index is '+str(currentPrefixIndex))
                result+=1
                currentTextIndex+=1
        else:                
            break
    
    return result
        


def computeZArray(input):

    print(input) 
    zArray = array('i')
    zArray.append(0)
    i = 1
    lengthPrefix = 0
    #print('value of first element in z array is '+str(zArray[0]))
    while (i < len(input)):
        if lengthPrefix == 0:
            lengthPrefix = findLengthLongestPrefix(i, 0, input)                       
        else:
            lengthPrefix = findLengthLongestPrefix(i, lengthPrefix, input)            
        zArray.append(lengthPrefix)            
        if lengthPrefix >=2:
                currentPrefixIndex = 1    
                i+=1
                currentTextIndex = i                
                upperBound = i+lengthPrefix-1                                            
                for j in range(1, lengthPrefix):
                    if (zArray[currentPrefixIndex]+currentTextIndex) < upperBound:
                        zArray.append(zArray[currentPrefixIndex])
                        currentPrefixIndex+=1
                        currentTextIndex+=1
                        i+=1
                    else:                        
                        lengthPrefix = upperBound-currentTextIndex                        
                        break   
                if len(zArray) == upperBound:                                        
                    lengthPrefix = 0                                    
        else:
            i+=1                 
            lengthPrefix = 0
    return zArray


zArray = computeZArray(input)
printResult(zArray, pattern)
