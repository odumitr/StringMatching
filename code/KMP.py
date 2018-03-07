from array import array
import sys

pattern = input('Enter the pattern  ')
text = input('Enter the text  ')

if(len(pattern) > len(text)):
        sys.exit('Text has to be at least the same length as pattern')        

#compute all prefixes the pattern can have
def computeAllPrefixes(string):

    allPrefixes = []
    for i in range(0, len(string)):
        substring = string[0:i+1]
        allPrefixes.append(substring)
    return allPrefixes

def findLongestSubstring(prefixes, suffixes, currentCommonSubstring):
    
    #find the length of the longest substring that is a prefix and a suffix
    string = suffixes[len(suffixes)-1]
    #print("common substring received is "+currentCommonSubstring)
    if len(currentCommonSubstring) > 0 and suffixes[0] == string[len(currentCommonSubstring)]:
        #print('i am in if')
        return currentCommonSubstring+suffixes[0]
    else:
        currentCommonSubstring = ''
        #have to find the substring by comparing each pair suffix prefix
        for i in range(0, len(suffixes)-1):
            help = suffixes[len(suffixes)-2-i]
            if help == prefixes[len(help)-1]:
                #print('help is '+help+' , prefix value is '+prefixes[len(help)-1])
                return help
        return str()
 

#for the pattern, compute the array that contains numbers that represent the longest common substring that is a prefix and a suffix
def computeLengthLongestPrefixSuffix(pattern, listPrefixes):

    result = array('i')    
    listCurrentSuffixes = []
    currentCommonSubstring = str()
    
    #compute all suffixes for all substrings in the pattern
    for i in range(0, len(pattern)):
        listCurrentSuffixes.insert(0, pattern[i])
        
        #using the current suffixes, take each one and append as last character the last character in the current substring
        for j in range(1, len(listCurrentSuffixes)):
            suffix = listCurrentSuffixes[j] + pattern[i]
            listCurrentSuffixes[j] = suffix
        
        #test to see that sufixes are computed correctly 
        #print("for substring ending at i "+str(i)+"sufixes are\n")
        #for z in range(0, len(listCurrentSuffixes)):
            #print(listCurrentSuffixes[z])
        
        #find the length of the longest substring that is a prefix and a suffix    
        currentCommonSubstring = findLongestSubstring(listPrefixes, listCurrentSuffixes, currentCommonSubstring)
        result.append(len(currentCommonSubstring))        
        #print("for substring ending at i "+str(i)+" the longest substring that is a prefix and suffix is "+currentCommonSubstring)
    return result

def findPattern(pattern, text, arrayLengthsCommonSubstr):

    indexText = 0
    indexPattern = 0 
    checker = None
    while (indexText < len(text)):
        if len(text)-indexText < len(pattern)-indexPattern:
            break        
        elif pattern[indexPattern] == text[indexText]:
            indexPattern+=1
            indexText+=1
            if indexPattern == len(pattern):                        
                checker = True
                break
        else:   
            if indexPattern == 0:
                indexText+=1
            else:          
                indexPattern = arrayLengthsCommonSubstr[indexPattern-1]

    
    if checker == True:
        indexStartMatched = indexText-indexPattern
        print('You have a match between text and pattern')
        print('The text matches the pattern at index '+str(indexStartMatched))
        print('Important! I am considering indices starting at zero!!!')
    else:
        print('Your pattern didn\'t match the text')


listPrefixes = computeAllPrefixes(pattern)
arrayLengthsCommonSubstr = computeLengthLongestPrefixSuffix(pattern, listPrefixes)
print(arrayLengthsCommonSubstr.tolist())
findPattern(pattern, text, arrayLengthsCommonSubstr)
