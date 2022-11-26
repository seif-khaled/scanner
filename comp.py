import re
import tabulate as tbl
import os,sys


class scanner:
    def __init__(self,text):
        self.text=text
        self.text=self.text.split()
        self.items=dict()
        self.patternkw="(Read|Write|Begin|End|Declare|INT|FLOAT|Set|IF|Then|Else|ENDIF|While|DO|ENDWHILE|Until|ENDUNTIL|Call)"
        self.dict_keys=["Reserved_word","add","subtract","multiply","division","equal","bigger than","smaller than","not equal to","identifier","left brace","right brace","semicolon","constant"]
        for i in range(len(self.dict_keys)):
            self.items[self.dict_keys[i]]={}
            
            
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
                if self.text[i] not in self.patternkw:
                    res=re.match(pattern_ident,text)
                    res2=re.match(pattern_int_const,text)
                    res3=re.match(pattern_float_const,text)
                    if res:
                        self.items["identifier"][self.text[i]]=i
                    else
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
                    self.items["Reserved_word"][self.text[i]]=i
                else:
                    continue

    def operator_parnthies_semicol_chekcer(self):
        switch=0
        pattern=["(",")","+","-","*","/","=","!","<",">",";"]
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
                if self.text[i] in pattern:
                    key_item_index=pattern.index(self.text[i])
                    if pattern[key_item_index]=='+':
                        self.items["add"][pattern[key_item_index]]=i
                    elif pattern[key_item_index]=='-':
                         self.items["subtract"][pattern[key_item_index]]=i
                    elif pattern[key_item_index]=='*':
                         self.items["multiply"][pattern[key_item_index]]=i

                    elif pattern[key_item_index]=='/':
                         self.items["division"][pattern[key_item_index]]=i

                    elif pattern[key_item_index]=='=':
                         self.items["equal"][pattern[key_item_index]]=i

                    elif pattern[key_item_index]=='<':
                         self.items["smaller than"][pattern[key_item_index]]=i

                    elif pattern[key_item_index]=='>':
                         self.items["bigger than"][pattern[key_item_index]]=i

                    elif pattern[key_item_index]=='!':
                         self.items["not equal to"][pattern[key_item_index]]=i

                    elif pattern[key_item_index]=='(':
                         self.items["left brace"][pattern[key_item_index]]=i

                    elif pattern[key_item_index]==')':
                         self.items["right brace"][pattern[key_item_index]]=i

                    elif pattern[key_item_index]==';':
                         self.items["semicolon"][pattern[key_item_index]]=i
                    else:
                        continue

                    # self.items[pattern[key_item_index]][pattern[key_item_index]]=
                # res=re.match(pattern,self.text[i])
                # if res:

# pattern=""
# pattern="(Read|Write|Begin|End|Declare|INT|FLOAT|CHAR|STRING|Set|IF|Then|Else|ENDIF|While|DO|ENDWHILE|Until|ENDUNTIL|Call)"
# text="Read what he has Write and Begin Declarew . in The End , Call your father Else he will hit you Untill you are dead"
# text="125 1588 132 -1355 -1 -56 2.3"
text="_X _X3 x2 X1 x33for valid_identifier_ nothim3 3x1 text_search"
text=text.split()
# pattern="-?\d+\.\d+"
pattern="_?[a-zA-Z_]+[0-9a-zA-Z_]*"
# print(text)
for i in range(len(text)):
    res=re.match(pattern,text[i])
    if res:
        print("yes",text[i])
    else:
        print("no",text[i])
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