import re
import tabulate as tbl
import os,sys


class scanner:
    def __init__(self,text):
        self.text=text
        self.text=self.text.split()
        self.items=dict()
        self.patternkw="(Read|Write|Begin|End|Declare|INT|FLOAT|Set|IF|Then|Else|ENDIF|While|DO|ENDWHILE|Until|ENDUNTIL|Call)"
        self.patternoperators=["(",")","+","-","*","/","=","!","<",">",";"] 
        self.dict_keys=["Reserved_word","add","subtract","multiply","division","equal","bigger than","smaller than","not equal to","identifier","left brace","right brace","semicolon","constant"]
        for i in range(len(self.dict_keys)):
            self.items[self.dict_keys[i]]=[]        
            
    def idnetifier_const_chekcer(self):
        switch=0
        pattern_ident="_?[a-zA-Z_]+[0-9a-zA-Z_]*"
        pattern_int_const="-?[0-9]+"
        pattern_float_const="-?\d+\.\d+"
        for i in range(len(self.text)):
            if(self.text[i]=='{'):
                switch=1
                # skipper+=1
                continue
            if(switch==1 and self.text[i]!='}' ):
                continue
            if(self.text[i]=='}'):
                switch=0
                continue
            else:
                if self.text[i] not in self.patternkw and self.text[i] not in self.patternoperators :
                    res=re.match(pattern_ident,self.text[i])
                    res2=re.match(pattern_int_const,self.text[i])
                    res3=re.match(pattern_float_const,self.text[i])
                    r1=re.findall(pattern_ident,self.text[i])
                    r2=re.findall(pattern_int_const,self.text[i])
                    r3=re.findall(pattern_float_const,self.text[i])
                    # print(r1,"\n",r2,"\n",r3,"\n")
                    if res:
                        self.items["identifier"].append(self.text[i])
                        self.items["identifier"].append(i)
                    if res2:
                        # print("iam a constant")
                        self.items["constant"].append(self.text[i])
                        self.items["constant"].append(i)
                    if res3:
                         self.items["constant"].append(self.text[i])
                         self.items["constant"].append(i)
                    else:
                        continue
    def reserved_words_chekcer(self):
        switch=0
        for i in range(len(self.text)):
            if(self.text[i]=='{'):
                switch=1
                # skipper+=1
                continue
            if(switch==1 and self.text[i]!='}' ):
                continue
            if(self.text[i]=='}'):
                switch=0
                continue
            else:
                res=re.match(self.patternkw,self.text[i])
                if res:
                    self.items["Reserved_word"].append(self.text[i])
                    self.items["Reserved_word"].append(i)
                else:
                    continue

    def operator_parnthies_semicol_chekcer(self):
        switch=0
        # pattern="(\(|\)|=|+|-|*|/|>|<|!)"

        for i in range(len(self.text)):
            if(self.text[i]=='{'):
                switch=1
                continue
            if(switch==1 and self.text[i]!='}' ):
                continue
            if(self.text[i]=='}'):
                switch=0
                continue

            else:
                if self.text[i] in self.patternoperators:
                    key_item_index=self.patternoperators.index(self.text[i])
                    if self.patternoperators[key_item_index]=='+':
                        # self.items["add"][self.patternoperators[key_item_index]]=i
                        self.items["add"].append(self.patternoperators[key_item_index])
                        self.items["add"].append(i)

                    elif self.patternoperators[key_item_index]=='-':
                        #  self.items["subtract"][self.patternoperators[key_item_index]]=i
                           self.items["subtract"].append(self.patternoperators[key_item_index])
                           self.items["subtract"].append(i)

                    elif self.patternoperators[key_item_index]=='*':
                           self.items["multiply"].append(self.patternoperators[key_item_index])
                           self.items["multiply"].append(i)
                        #  self.items["multiply"][self.patternoperators[key_item_index]]=i

                    elif self.patternoperators[key_item_index]=='/':
                           self.items["division"].append(self.patternoperators[key_item_index])
                           self.items["division"].append(i)

                        #  self.items["division"][self.patternoperators[key_item_index]]=i

                    elif self.patternoperators[key_item_index]=='=':
                           self.items["equal"].append(self.patternoperators[key_item_index])
                           self.items["equal"].append(i)

                        #  self.items["equal"][self.patternoperators[key_item_index]]=i

                    elif self.patternoperators[key_item_index]=='<':
                          self.items["smaller than"].append(self.patternoperators[key_item_index])
                          self.items["smaller than"].append(i)

                        #  self.items["smaller than"][self.patternoperators[key_item_index]]=i

                    elif self.patternoperators[key_item_index]=='>':
                          self.items["bigger than"].append(self.patternoperators[key_item_index])
                          self.items["bigger than"].append(i)
                        #  self.items["bigger than"][self.patternoperators[key_item_index]]=i

                    elif self.patternoperators[key_item_index]=='!':
                          self.items["not equal to"].append(self.patternoperators[key_item_index])
                          self.items["not equal to"].append(i)
                        #  self.items["not equal to"][self.patternoperators[key_item_index]]=i

                    elif self.patternoperators[key_item_index]=='(':
                          self.items["left brace"].append(self.patternoperators[key_item_index])
                          self.items["left brace"].append(i)
                        #  self.items["left brace"][self.patternoperators[key_item_index]]=i

                    elif self.patternoperators[key_item_index]==')':
                          self.items["right brace"].append(self.patternoperators[key_item_index])
                          self.items["right brace"].append(i)
                        #  self.items["right brace"][self.patternoperators[key_item_index]]=i

                    elif self.patternoperators[key_item_index]==';':
                          self.items["semicolon"].append(self.patternoperators[key_item_index])
                          self.items["semicolon"].append(i)
                        #  self.items["semicolon"][self.patternoperators[key_item_index]]=i
                    else:
                        continue

    def executer(self):
        self.reserved_words_chekcer()
        self.operator_parnthies_semicol_chekcer()
        self.idnetifier_const_chekcer()

                    # self.items[pattern[key_item_index]][pattern[key_item_index]]=
                # res=re.match(pattern,self.text[i])
                # if res:

# pattern=""
# pattern="(Read|Write|Begin|End|Declare|INT|FLOAT|CHAR|STRING|Set|IF|Then|Else|ENDIF|While|DO|ENDWHILE|Until|ENDUNTIL|Call)"
# text="ReadRead what he has Write and Begin Declarew . in The End , Call your father Else he will hit you Untill you are dead"

# text="125 1588 132 -1355 -1 -56 2.3"

# validatign text before excuting the scanner
###################################################
flag=0
while(flag==0):
    number_of_lexmes=eval(input("enter the number of lexmes you will input:"))
    print("\n")
    text=""
    for i in range(number_of_lexmes):
        lexme=input("enter a lexeme word:")
        text+=lexme
        text+=" "
    x=scanner(text)
    x.executer()
    print(x.items)
    print("\n")
    choice=input("do you want to continue?")
    if choice=='yes':
        os.system('cls||clear')
        continue
    elif choice=='no':
        flag=1

#####################################
# dictionary={'key1':[]}
# dictionary["key1"].append("shinfa")
# dictionary["key1"].append(1)

# print(dictionary["key1"])
# text="_X _X3 x2 X1 x33for valid_identifier_ nothim3 3x1 text_search"
# text=text.split()
# pattern="-?\d+\.\d+"
# pattern="_?[a-zA-Z_]+[0-9a-zA-Z_]*"
# print(text)
# for i in range(len(text)):
#     res=re.match(pattern,text[i])
#     if res:
#         print("yes",text[i])
#     else:
#         print("no",text[i])
# res=re.findall(pat,text)
# print(res)
# if res:
#     print("yes")
# else:
#     print("no")

# print()
# if identifier==r"[0-9]":
#     print("true")
# print("hello shinfa")