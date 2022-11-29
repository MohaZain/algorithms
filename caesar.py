'''
A Caesar cipher is a simple substitution cipher in which each letter of the plain text 
is substituted with a letter found by moving n places down the alphabet. 
'''
import string
def caesar_cipher(txt,n):
    alphabet_list = list(string.ascii_lowercase)
    txt_cipher = ''
    for latter in txt:
        if latter in alphabet_list:
            cip_indx = alphabet_list.index(latter) + n 
            if cip_indx > 25 :
                cip_indx = cip_indx - 26
            txt_cipher = txt_cipher + alphabet_list[cip_indx]
        else:
            txt_cipher = txt_cipher + latter
    return txt,txt_cipher

def rev_caesar_cipher(txt,n):
    alphabet_list = list(string.ascii_lowercase)
    txt_cipher = ''
    for latter in txt:
        if latter in alphabet_list:
            cip_indx = alphabet_list.index(latter) + n 
            # if cip_indx > 25 :
            #     cip_indx = cip_indx - 26
            txt_cipher = txt_cipher + alphabet_list[cip_indx]
        else:
            txt_cipher = txt_cipher + latter
    return txt,txt_cipher

print(caesar_cipher('efgh bcd',-4))
# efgh bcd