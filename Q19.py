def count_vowel(text):
    vowel="aeiouAEIOU"
    count=0
    vowels=[]
    for i in text:
        if i in vowel:
            count += 1
            if i not in vowels:
                vowels.append(i)
    return count,vowels
text=input("Enter the string :")
result,vowel=count_vowel(text)

if result==0:
    print("No vowel present in the word")
else:
    print(f"Total number of vowel in the string is {result} and they are {vowel}")