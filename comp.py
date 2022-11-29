import re
from tabulate import tabulate as tbl
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
        satsified=0
        switch=0
        pattern_ident="[a-zA-Z_][a-zA-Z0-9_]*"
        pattern_int_const="-?[0-9]+"
        pattern_float_const="-?\d+\.\d+"
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
                    res=re.match(pattern_ident,self.text[i])
                    res2=re.match(pattern_int_const,self.text[i])
                    res3=re.match(pattern_float_const,self.text[i])
                
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


###################################################
def table_list(dictionary,words,actual_number_of_lexmes,num_of_lex):
    Index=0
    final_table=[]
    switch=0
    indcies_to_skip=[]
    index_toput_into=0
    for i in range(actual_number_of_lexmes):
        final_table.append([])
    #loop on each key and get the index of each items
   
    counter=0
    for i in range(len(words)):
        if(words[i]=='{'):
            switch=1
            indcies_to_skip.append(i)
            continue
        if(switch==1 and words[i]!='}' ):
            indcies_to_skip.append(i)
            continue
        if(words[i]=='}'):
            indcies_to_skip.append(i)
            switch=0
            continue
    print(indcies_to_skip)
    flag=0
    while(counter!=actual_number_of_lexmes and flag!=1 ):
        if Index==num_of_lex:
            break
        else:
            for i in dictionary: 
                if Index==num_of_lex:
                    flag=1
                    break
                elif Index in dictionary[i] and Index not in indcies_to_skip:
                    index_of_current_lexem=(dictionary[i].index(Index))-1
                    current_lex=dictionary[i][index_of_current_lexem]
                    final_table[index_toput_into].append(current_lex)
                    final_table[index_toput_into].append(i)
                    Index+=1
                    counter+=1
                    index_toput_into+=1
                    break
                elif Index in indcies_to_skip:
                    Index=(indcies_to_skip.index(Index))+1
           
    return final_table
            
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
    x=scanner(text)
    x.executer()
    print("\n")
    DATA=table_list(x.items,LIST,len(new_list_to_work_on),number_of_lexmes)
    print(table_list(x.items,LIST,len(new_list_to_work_on),number_of_lexmes))
    print(tbl(DATA,headers=["lexeme","Token"],tablefmt='fancy_grid'))
    choice=input("do you want to continue?")
    if choice=='yes':
        os.system('cls||clear')
        continue
    elif choice=='no':
        flag=1

