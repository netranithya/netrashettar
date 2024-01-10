#Python Program to calculate the total number of vowels and count of individual vowel

vowelCount = {}
vowels = 'aeiou'

def countChars(str):
    str = str.lower()
    for char in str:
        if(char in vowels):
            if(char not in vowelCount):
                vowelCount[char] = 0
            vowelCount[char] = vowelCount[char] + 1

    print(vowelCount)

countChars('Guvi Geeks Network private limited')