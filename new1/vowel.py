'''word=input("enter a word:")
listvowel=[i for i in word if i in 'aeiouAEIOU']
print(f"vowels are {listvowel}")'''
'''w=input("enter any character:")
listOrdinals=[ord(i) for i in w]
print(listOrdinals)'''
s=input("enter a sentance:");
print(s)
wordsList=s.split()
print (wordsList)
for i in wordsList:
    print(f"{i} occurs {wordsList.couunt(i)} times")
