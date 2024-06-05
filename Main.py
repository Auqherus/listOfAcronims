# Exercise 1

acronyms = ['LOL', 'IDK', 'SMH', 'TBH']
print(acronyms[3]) #  TBH
acronyms.append('ROFL')
acronyms.append('LFMAO')
print(acronyms) # ['LOL', 'IDK', 'SMH', 'TBH', 'ROFL', 'LFMAO']

# Exercise 2

word ='BRB'

if word in acronyms:
    print(word + ' is in acronyms.')
else:
    print(word + ' is not in acronyms.') # BRB is not in acronyms.

# Exercise 3

for acronym in acronyms:
    print(acronym)
    # LOL
    # IDK
    # SMH
    # TBH
    # ROFL
    # LFMAO

