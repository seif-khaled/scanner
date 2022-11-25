import re
import tabulate as tbl
import os,sys


class scanner:
    def __init__(self,text):
        self.text=text
        self.text=self.text.split()
        self.items=dict()
        self.dict_keys=["Reserved_word","add","subtract","multiply","division","equal","bigger than","smaller than","not equal to","identifier","left brace","right brace"]
        for i in range(len(self.dict_keys)):
            self.items[self.dict_keys[i]]={}
            
    def idnetifier_chekcer(self):
        pass
    def reserved_words_chekcer(self):
        # skipper=0
        switch=0
        pattern="(Read|Write|Begin|End|Declare|INT|FLOAT|CHAR|STRING|Set|IF|Then|Else|ENDIF|While|DO|ENDWHILE|Until|ENDUNTIL|Call)"
        for i in range(len(self.text)):
            # if(skipper!=0 and switch!=0):
            #     skipper-=1
            #     continue
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
                for i in range(len(self.text)):
                    res=re.match(pattern,self.text[i])
                    if res:






                
            # else:
                



        
    def operator_parnthies_chekcer(self):
        pass
    def comments_chekcer(self):
        pass
pattern="(Read|Write|if|else)"
text="Read if"
res=re.match(pattern,text)
if res:
    print("yes")
else:
    print("no")

# print()
# if identifier==r"[0-9]":
#     print("true")
# print("hello shinfa")