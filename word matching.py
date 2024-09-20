print('\033c')

def match_word(words):
    counter = 0
    lst= []
    
    
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            
            counter = counter + 1
            lst.append(word)
            
            
    print("List of words with first and last character same\n", lst)
    return counter

li = ['abs', 'cfc', 'xyz', 'aba', '1221', 'nahian', 'junairaj', 'rifar']

count = match_word(li)
print("number of words having first and last character same:", count)