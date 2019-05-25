#!/home/namah/Lab/Python/anaconda3/bin/python

import traceback
from pprint import pprint
import os

alphabet_separator="\n"
word_separator=', '

def read_file(filename):
    with open(filename,'r') as f:
        text=f.read()
        lines=text.split(alphabet_separator)
        words=[]
        for line in lines:
            words += line.split(word_separator)
        return words

def format_file(words):
    assert len(words)>0
    sentence_to_return=""
    alpha=None
    for word in words:
        if not alpha:
            alpha=word[0]
        elif word[0]!=alpha:
            alpha=word[0]
            sentence_to_return+=alphabet_separator
        else:
            sentence_to_return+=word_separator
        sentence_to_return+=word       
    return sentence_to_return

def yes_or_no(sentence):
    while(True):
        res=input(sentence + '[y/n]')
        if res =='y':
            return True
        elif res =='n':
            return False

def add_rhyme(files_rhymes,handle_input):
    my_main_rhymes=set(files_rhymes)
    my_main_rhymes.add(handle_input)
    my_main_rhymes=list(my_main_rhymes)
    my_main_rhymes.sort(key=str.casefold)
    print(f'main_rhymes: {my_main_rhymes}')
    return my_main_rhymes
    
def handle_rhymes(file_path,files_rhymes=[]):
    handle_rhyme=True
    while(handle_rhyme):
        print(f'current rhymes: {files_rhymes}')
        handle_input=input('Type your word: ')
        if handle_input==key_word_out:
            return files_rhymes
        elif handle_input == key_word_remove:
            word_to_remove=input('Which word do you wanna erase?')
            if word_to_remove in files_rhymes:
                files_rhymes.remove(word_to_remove)
        elif handle_input==key_word_save:
            with open(file_path,'w+') as f:
                content=format_file(files_rhymes)
                f.write(content)
            print('file saved')
        else:
            try: 
                files_rhymes=add_rhyme(files_rhymes,handle_input)
            except:
                print('erreur')
                traceback.print_exc()

if __name__ == "__main__":
    keep_on=True
    key_word_out='exit'
    key_word_remove='rm'
    key_word_save='save'
    
    filename= "NewFreezer.txt"
    folder_path="./rhymes/"
    
    while(keep_on):
        rhymes_files=os.listdir(folder_path)
        print("rhymes files:\n",rhymes_files)
        print('\nfinish? tape "exit"\n')
        main_input=input('Enter your rhyme filename without the extension: ')
        filename=main_input+".txt"
        print(filename,'filename')
        file_path=folder_path+filename
        if main_input==key_word_out:
            keep_on=False
        elif filename in rhymes_files:
            files_rhymes=read_file(file_path)
            handled_rhymes=handle_rhymes(file_path,files_rhymes)  
        else:
            handled_rhymes=handle_rhymes(file_path)
            
            
            






