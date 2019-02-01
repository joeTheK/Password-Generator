import random

char_num = int(input("How long does the password need to be? "))
special_char = input("Any special characters? /Answer 'yes' or 'no': ")

char_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',1,2,3,4,5,6,7,8,9,0]
Schar_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','&','-','$','_','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',1,2,3,4,5,6,7,8,9,0]

for i in range(char_num):
    if special_char == 'yes':
        print(random.choice(Schar_list), end="")
    else :
        print(random.choice(char_list), end="")
