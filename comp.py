import re
from tabulate import tabulate as tbl
import os,sys


class scanner:
    def __init__(self,text,actulnooflex):
        self.text=text
        self.actualno=actulnooflex
        self.text=self.text.split()
        self.indexx=0
        self.items=dict()
        self.table=[]
        self.pattern_ident="[a-zA-Z_][a-zA-Z0-9_]*"
        self.pattern_int_const="-?[0-9]+"
        self.pattern_float_const="-?\d+\.\d+"
        self.patternkw="(Read|Write|Begin|End|Declare|INT|FLOAT|Set|IF|Then|Else|ENDIF|While|DO|ENDWHILE|Until|ENDUNTIL|Call)"
        self.patternoperators=["(",")","+","-","*","/","=","!","<",">",";"] 
        self.dict_keys=["Reserved_word","add","subtract","multiply","division","equal","bigger than","smaller than","not equal to","identifier","left brace","right brace","semicolon","constant"]
        for i in range(len(self.dict_keys)):
            self.items[self.dict_keys[i]]=[]
        for i in range(self.actualno):
            self.table.append([])        
    def is_identifirr(self,word):
        if re.match(self.pattern_ident,word):
            return True
        else:
            return False
    def is_constsnt(self,word):
        if re.match(self.pattern_int_const,word) or re.match(self.pattern_float_const,word):
            return True
        else:
            return False
    def is_reserved_word(self,word):
        if word in self.patternkw:
            return True
        else:
            return False
    def is_operstor(self,word):
        if word in self.patternoperators:
            return True
        else:
            return False
    def create_table(self):
        switch=0
        self.indexx=0
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
                    
                if self.is_reserved_word(self.text[i]):
                    self.table[self.indexx].append(self.text[i])
                    self.table[self.indexx].append("resrved word")
                    self.indexx+=1
                elif self.is_constsnt(self.text[i]):
                    self.table[self.indexx].append(self.text[i])
                    self.table[self.indexx].append("constant")
                    self.indexx+=1
                elif  self.is_operstor(self.text[i]):
                    if self.text[i]=="+":
                        self.table[self.indexx].append(self.text[i])
                        self.table[self.indexx].append("add")
                        self.indexx+=1
                    elif self.text[i]=="-":
                        self.table[self.indexx].append(self.text[i])
                        self.table[self.indexx].append("subtract")
                        self.indexx+=1
                    elif self.text[i]=="*":
                        self.table[self.indexx].append(self.text[i])
                        self.table[self.indexx].append("multiply")
                        self.indexx+=1
                    elif self.text[i]=="/":
                        self.table[self.indexx].append(self.text[i])
                        self.table[self.indexx].append("division")
                        self.indexx+=1
                    elif self.text[i]=="=":
                        self.table[self.indexx].append(self.text[i])
                        self.table[self.indexx].append("equal")
                        self.indexx+=1
                    elif self.text[i]=="<":
                        self.table[self.indexx].append(self.text[i])
                        self.table[self.indexx].append("smaller than")
                        self.indexx+=1
                    elif self.text[i]==">":
                        self.table[self.indexx].append(self.text[i])
                        self.table[self.indexx].append("bigger than")
                        self.indexx+=1
                    elif self.text[i]=="!":
                        self.table[self.indexx].append(self.text[i])
                        self.table[self.indexx].append("not equal to")
                        self.indexx+=1
                    elif self.text[i]=="(":
                        self.table[self.indexx].append(self.text[i])
                        self.table[self.indexx].append("left bracket")
                        self.indexx+=1
                    elif self.text[i]==")":
                        self.table[self.indexx].append(self.text[i])
                        self.table[self.indexx].append("right bracket")
                        self.indexx+=1
                    elif self.text[i]==";":
                        self.table[self.indexx].append(self.text[i])
                        self.table[self.indexx].append("semi colon")
                        self.indexx+=1

                elif self.is_identifirr(self.text[i]):
                    self.table[self.indexx].append(self.text[i])
                    self.table[self.indexx].append("identifirr")
                    self.indexx+=1
    def idnetifier_const_chekcer(self):
        satsified=0
        switch=0
        
        for i in range(len(self.text)):
            chekcer=re.match(self.patternkw,self.text[i])
            # print(chekcer)
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
                if (chekcer==None) and (self.text[i] not in self.patternoperators) :
                    # res=is_match_idenetifier(self.text[i])
                    # print(res)
                    res=re.match(self.pattern_ident,self.text[i])
                    res2=re.match(self.pattern_int_const,self.text[i])
                    res3=re.match(self.pattern_float_const,self.text[i])
                
                    if res:
                        self.items["identifier"].append(self.text[i])
                        self.items["identifier"].append(i)
                        
                    elif res2:
                        # print("iam a constant")
                        self.items["constant"].append(self.text[i])
                        self.items["constant"].append(i)
                        
                    elif res3:
                         self.items["constant"].append(self.text[i])
                         self.items["constant"].append(i)
                         
                    else:
                        continue
    def reserved_words_chekcer(self):
        satsified=0
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
        satsified=0
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
                        self.items["add"].append(self.patternoperators[key_item_index])
                        self.items["add"].append(i)
                        
                    elif self.patternoperators[key_item_index]=='-':
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


###################################################
            
#######################################
flag=0
while(flag==0):
    switch=0
    list_to_work_on=[]
    number_of_lexmes=eval(input("enter the number of lexmes you will input:"))
    print("\n")
    text=""
    for i in range(number_of_lexmes):
        lexme=input("enter a lexeme word:")
        text+=lexme
        text+=" "
        list_to_work_on.append(lexme)
    index_to_start_at=1
    new_list_to_work_on=[]
    LIST=text.split()
    for j in range(len(list_to_work_on)):
        if(list_to_work_on[j]=='{'):
            switch=1
            index_to_start_at+=1
            continue
        if(switch==1 and list_to_work_on[j]!='}' ):
            index_to_start_at+=1
            continue
        if(list_to_work_on[j]=='}'):
            switch=0
            index_to_start_at+=1
            continue
        else:
            new_list_to_work_on.append(list_to_work_on[j])
    print(new_list_to_work_on)        
    x=scanner(text,len(new_list_to_work_on))
    x.executer()
    x.create_table()
    print(x.table)
    print("\n")
    # DATA=table_list(x.items,LIST,len(new_list_to_work_on),number_of_lexmes)
    # print(table_list(x.items,LIST,len(new_list_to_work_on),number_of_lexmes))
    print(tbl(x.table,headers=["lexeme","Token"],tablefmt='fancy_grid'))
    choice=input("do you want to continue?")
    if choice=='yes':
        os.system('cls||clear')
        continue
    elif choice=='no':
        flag=1