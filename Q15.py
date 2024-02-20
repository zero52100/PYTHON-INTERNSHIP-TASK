def to_check(s1, s2):
    return sorted(s1) == sorted(s2)

input1=input("Enter the string")
input2=input("Enter the string")
if to_check(input1, input2):
    print(f"{input1} and {input2} are anagrams.")
else:
    print(f"{input1} and {input2} are not anagrams.")
