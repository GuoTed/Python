import re

# 0. what is regex? common usages?
'''
-> decribe patterns in text
-> find specific context (have patterns, ie: phone number)
'''
# 1. Practice writing basic regex patterns
text = 'Hi all, \
        Thanks for your participation for this course. \
        Fell free to contact us if you have any further questions.  \
        #phone: 0912345678 \
        Thanks, \
        Ted'

phone_pattern = '\d{10}' # \d: matchs a digit, {10}: matches the previous token exactly 10 times
match = re.search(phone_pattern, text) # return the first match
if match:
    print('Search Result:', match.group())
else:
    print('Pattern not found')

# 2. Practice anchors & quantifiers & Character Classes & Escape Characters
'''
Anchors: used to specify where in the string a match must occur 
'''
text = 'text: 2023 1231'

pattern = '^\d{4}' # ^text : only match if the string starts witht text
match = re.search(pattern, text) 
print(match.group()) if match else print('Pattern not found') # not found

pattern = '\d{4}$' # text$ : only match if the string ends witht text
match = re.search(pattern, text) 
print(match.group()) if match else print('Pattern not found') # 1231

'''
Quantifier: specifies the mathces of a character or a group of characters in a pattern
'''
text = 'text: dec 12/31'

pattern = '\d*' # * : Matches zero or more occurrences 
match = re.search(pattern, text) 
print(match.group()) if match else print('Pattern not found') # zero match

pattern = '\d+' # + : Matches one or more occurrences
match = re.search(pattern, text) 
print(match.group()) if match else print('Pattern not found') # 12

pattern = '\d?' # ? : Matches zero or one occurrence
match = re.search(pattern, text) 
print(match.group()) if match else print('Pattern not found') # zero match

pattern = '\d{2}' # {n} : Matches exactly n occurrences 
match = re.search(pattern, text) 
print(match.group()) if match else print('Pattern not found') # 12

'''
Character Classes : defined by enclosing a group of characters inside square brackets []
'''
text = 'Hello123'
pattern = '[^0-9]*'  # Matches any character that is not a digit
match = re.search(pattern, text) 
print(match.group()) if match else print('Pattern not found') # Hello

'''
Escape Characters : \ which can help characters treated literally
'''
text = 'Good Bye. See you ~'
pattern = '[A-z]+\.'  # Matches 'end.' in the text
match = re.search(pattern, text) 
print(match.group()) if match else print('Pattern not found') # Bye.

'''
Groups
'''
text = 'Ted: 912-345-678'
pattern = '(\d{3})[-.\s]?(\d{3})[-.\s]?(\d{3})'
match = re.search(pattern, text) 
if match:
    print(match.group())
    format_text = '_'.join(match.groups())
    print(format_text) # 912_345_678
else:
    print('Pattern not found')

'''
Lookarounds and 
'''

text = "apple apply application"

pattern = 'appl(?=e)\w+' # Positive lookahead: find pattern that 'appl' is ahead of 'e'
matches = re.findall(pattern, text)
print(matches)  # Outputs: ['apple']

pattern = 'appl(?!e)\w+' # Negative lookahead: find pattern that 'appl' is not ahead of 'e'
matches = re.findall(pattern, text)
print(matches)  # Outputs: ['apply', 'application']

pattern = '\w+(?<=appl)e' # # Positive lookbehind: find pattern that 'e' is behand 'appl'
matches = re.findall(pattern, text)
print(matches)  # Outputs: ['apple']

pattern = '\w+(?<!appl)e' # # Negative lookbehind: find pattern that 'e' is not behand 'appl'
matches = re.findall(pattern, text)
print(matches)  # Outputs: []

'''
Assertions
'''
text = 'ad in yt cannot be blocked by adblock (not a ad)'

pattern = r'\bad\b' # \b : word boundary assertion
matches = re.findall(pattern, text)
print(matches)  # Outputs: ['ad', 'ad']

'''
special metacharacters
'''
pattern = '\s' # represent any whitespace character ex: Space & Tab \t & Newline \n 
pattern = '\d' # represent digits 
pattern = '\w' # equal to [A-z0-9_] (letter & _)

# 3. regex function: search/match/findall/sub
text = "You're unstoppable. Definition of unstoppable."

'''
search() :  used to find the first match
'''
pattern = '\w+(?=\.)'
match = re.search(pattern, text) 
print(match.group()) if match else print('Pattern not found') # unstoppable

'''
match() : used to check if the pattern matches at the beginning of the string (like ^)
'''
pattern = '\w+(?=\.)'
match = re.match(pattern, text) 
print(match.group()) if match else print('Pattern not found') # Pattern not found

'''
findall()
'''
pattern = '\w+(?=\.)'
matches = re.findall(pattern, text) 
print(matches) if matches else print('Pattern not found') # ['unstoppable']

# 4. common patterns
pattern = r'\w+' # Word 
pattern = r'\W+' # not Word
pattern = r'\s+' # Whitespace Characters
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' # Email Address
pattern = r'https?://\S+' # URL
pattern = r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b' # Phone Number
pattern = r'\b(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}\b' # Date (MM/DD/YYYY)

# Bonus: take Regex101 quiz
# ...
