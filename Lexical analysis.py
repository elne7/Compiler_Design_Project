"""
Created on Wed Dec 27 15:03:18 2023

@author: A7MaD_Elne7
"""
import re
import nltk


input_program = input("Enter your code: ")
input_program_tokens = nltk.wordpunct_tokenize(input_program)

print(input_program_tokens)

RE_Keywords = "auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while|string"
RE_Numerals = "^(\d+)$"
RE_Special_Characters = "[\[@&~!#$\^\|{}\]:;<>?,|.']|\(\)|\(|\)|{}|\[\]|\""
RE_Identifiers = "^[a-zA-Z_]+[a-zA-Z0-9_]*"
RE_Header = "([a-zA-Z]+\.[h])"
RE_Operators = "\**|-|=|\*|/|%|--|<=|>="


#To Categorize the tokens

for token in input_program_tokens:
    if(re.findall(RE_Keywords,token)):
        print(token, "--------> Keyword")
    elif(re.findall(RE_Numerals,token)):
        print(token, "--------> Numeral")
    elif(re.findall(RE_Special_Characters,token)):
        print(token, "--------> Special Characters/Sympol")
    elif(re.findall(RE_Identifiers,token)):
        print(token, "--------> Identifiers")
    elif(re.findall(RE_Header,token)):
        print(token, "--------> Header")
    elif(re.findall(RE_Operators,token)):
        print(token, "--------> Operator")
    else:
        print("Unknown Value")