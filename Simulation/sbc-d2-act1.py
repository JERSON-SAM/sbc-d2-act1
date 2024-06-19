'''text = "Hello World"
          012345678910
         1110987654321
print(text[-7])

word = input("word:")
print(text[-9])'''

'''#slicing 
text = "Hello World"
    #   012345678910
    #   1110987654321
#print (text[0:2], text[6:8])

name = "Jerson"
print("{0} {1}".format(text[0:2], text[6:8]))
print(f"{text[0:2]} {text[6:8]}")'''

#string method
'''
word = "hello world"
print(word.upper())
word = "hello world"
print(word.lower())
print(word.capitalize())
print(word.title())
print(word.replace("h", "x"))
print(word.find("h"))"
print(word.isalpha())
print(word.isnumeric())
print(word.isalnum())
'''

word = "summer bootcamp"
       
print(word.title())

print(f"{word[0:14].capitalize() + word[-1].capitalize()}")
print(word[7:11].replace("b","L"))
print(word.replace("summer bootcamp", "loot" ))
print(word.replace("summer bootcamp", "camE" ))
print(word[11:15].replace("p", "E"))
print(word[12].upper()+ word[5].upper())

word = "summer bootcamp"

print(word.replace("","").isalpha())
