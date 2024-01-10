#vowels = 'aeiou'
vowelCount={}
def FrequentUsedChar(str):
    str = str.lower()
    vowel= list(str)

    for char in str:
      if(char in vowel):
         if(char  != vowelCount):
             vowelCount[char] = 0
         vowelCount[char] = vowelCount[char] + 1

    first_value = list(vowelCount.values())[0]
    allEqual = all(value == first_value for value in vowelCount.values())
    if(allEqual):
        print('All characters are equal')
        return

    frequentlyusedchar=max(zip(vowelCount.values(),vowelCount.keys()))
    print(frequentlyusedchar)
    if frequentlyusedchar > 1:
        print("Most frequently used character is :", frequentlyusedchar[1])
    else:
        print("Character are used only once")


strtobechecked= input("Enter the string to be checked : ")
FrequentUsedChar(strtobechecked)
