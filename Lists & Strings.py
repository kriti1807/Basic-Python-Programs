#LISTS

names=['kriti', 'tashika', 'manav', 'piyush']
#1. append()-adds an element to the end of the list.
print("list before append",names)
names.append("shweta")
print("list after append",names)

#2. copy()-returns a copy of the List
x=names.copy()
print("Copied list", x)

#3. count()-returns the number of elements with the specified value
y=names.count('tashika')
print("count no of the word=", y)

#4. extend()-add the elements of a list to the eand of the current list
ages=[20,19,21,27]
names.extend(ages)
print("extended list", names)

#5. index()-retuns the index of the first element with the specified value
z=names.index("kriti")
print("indexed position=", z)

#6. insert()-adds an element at the specified position
ages.insert(3,22)
print("inserted age=", ages)

#7. pop()-removes the element at the specified position
ages.pop(3)
print("list after popped out element", ages)

#8. remove()-removes the element with the specified value
names.remove("piyush")
print("list after removal of name", names)

#9. reverse()-reverses the order of the list
ages.reverse()
print("reversed list", ages)

#10. sort()- sorts the list
ages.sort()
print("sorted list=",ages)

ages.sort(reverse=True)
print("sorted list in descending=", ages)

#11. clear()-removes all the elements from the lists
print("list before clear",names)
names.clear()
print("list after clear",names)

#STRINGS

#1. capitalize()-converts the first character to upper case
str="my NAME is kriti"
p=str.capitalize()
print(p)

#2. casefold()-converts string into lower case
p=str.casefold()
print(p)

#3. center()-returns a centered string
p=str.center(30)
print(p)

#4. count()-returns the number of times a specified value occurs in a string
p=str.count('i')
print(p)

#5. encode()-returns an encoded version of the string
str1="I l\tik\te åpple"
p=str1.encode()
print(p)

#6. endswith()-Returns true if the string ends with the specified value
p=str.endswith("i")
print(p)

#7. expandtabs()-Sets the tab size of the string
p=str1.expandtabs(2)
print(p)

#8. find()-Searches the string for a specified value and returns the position of where it was found
p=str.find("is")
print(p)

#9 format()-Formats specified values in a string
str2="I like to study {sname}, i am {age}".format(sname="computers",age=20)
print(str2)

#10. format_map()-Formats specified values in a string
#11. index()-Searches the string for a specified value and returns the position of where it was found
p=str.index("my")
print(p)

#12. isalnum()-Returns True if all characters in the string are alphanumeric
p=str.isalnum()
print(p)

#13. isalpha()-Returns True if all characters in the string are in the alphabet
p=str.isalpha()
print(p)

#14. isascii()-Returns True if all characters in the string are ascii characters
p=str1.isascii()
print(p)

#15. isdecimal()-Returns True if all characters in the string are decimals
num="0336"
p=num.isdecimal()
print(p)

#16. isdigit()-Returns True if all characters in the string are digits
p=num.isdigit()
print(p)

#17. isidentifier()-Returns True if the string is an identifier
str3="hello"
p=str3.isidentifier()
print(p)

#18. islower()-Returns True if all characters in the string are lower case
p=str.islower()
print(p)

#19. isnumeric()-	Returns True if all characters in the string are numeric
p=num.isnumeric()
print(p)

#20. isprintable()-Returns True if all characters in the string are printable
p=str1.isprintable()
print(p)

#21. isspace()-Returns True if all characters in the string are whitespaces
space="      "
p=space.isspace()
print(p)

#22. istitle()-Returns True if the string follows the rules of a title
p=str.istitle()
print(p)

#23. isupper()-Returns True if all characters in the string are upper case
p=str.isupper()
print(p)

#24. join()-Joins the elements of an iterable to the end of the string
p=".".join(str)
print(p)

#25. ljust()-Returns a left justified version of the string
just="Hi"
p=just.ljust(5)
print(p, "I am Kriti")

#26. lower()-Converts a string into lower case
p=str.lower()
print(p)

#27. lstrip()-Returns a left trim version of the string
#28. maketrans()-Returns a translation table to be used in translations
just1=just.maketrans("H","B")
print(just.translate(just1))

#29. partition()-Returns a tuple where the string is parted into three parts
p=str.partition("NAME")
print(p)

#30. replace()-Returns a string where a specified value is replaced with a specified value
p=str.replace("kriti", "tashika")
print(p)

#31. rfind()-Searches the string for a specified value and returns the last position of where it was found
p=str.rfind("is")
print(p)

#32. rindex()-Searches the string for a specified value and returns the last position of where it was found
p=str.rindex("is")
print(p)

#33. rjust()-Returns a right justified version of the string
#34. rpartiiton()-Returns a tuple where the string is parted into three parts
#35. rsplit()-Splits the string at the specified separator, and returns a list
p=str.rsplit(",")
print(p)

#36. rstrip()-Returns a right trim version of the string
#37. split()-	Splits the string at the specified separator, and returns a list
p=str.split()
print(p)

#38. splitlines()-Splits the string at line breaks and returns a list
str5="welcome to study python\nYou will enjoy this session"
p=str5.splitlines()
print(p)

#39. startswith()-Returns true if the string starts with the specified value
p=str.startswith("my")
print(p)

#40. strip()-Returns a trimmed version of the string
#41. swapcase()-Swaps cases, lower case becomes upper case and vice versa
p=str.swapcase()
print(p)

#42. title()-Converts the first character of each word to upper case
p=str2.title()
print(p)

#43. translate()-Returns a translated string
#44. upper()-Converts a string into upper case
p=str.upper()
print(p)

#45. zfill()-Fills the string with a specified number of 0 values at the beginning
a = "hello"
b = "welcome to study python"
c = "10.000"

print(a.zfill(6))
print(b.zfill(30))
print(c.zfill(8))
