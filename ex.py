text = """
\033[1;31moooooooooo.     .oooooo.   ooooooooo.   ooooo        oooooooooooo ooooooooo.\033[0m   
\033[1;31m`888'   `Y8b   d8P'  `Y8b  `888   `Y88. `888'        `888'     `8 `888   `Y88.\033[0m 
\033[1;31m 888      888 888      888  888   .d88'  888          888          888   .d88'\033[0m 
\033[1;31m 888      888 888      888  888ooo88P'   888          888oooo8     888ooo88P'\033[0m  
\033[1;31m 888      888 888      888  888          888          888    "     888`88b.\033[0m    
\033[1;31m 888     d88' `88b    d88'  888          888       o  888       o  888  `88b.\033[0m  
\033[1;31mo888bood8P'    `Y8bood8P'  o888o        o888ooooood8 o888ooooood8 o888o  o888o\033[0m 

\033[1;32mHere is a tool to find & know  it's a Python keyword or not.\033[0m
                                                        Instagram:- @darkweb.zip
"""

print(text)

import keyword
import calendar


#print("\033[1;31mEnter 1 for print all keywords. :  \033[0m")
#print("\033[1;32mEnter 2 for check  it is a keyword or not  :  \033[0m")
#print("\033[1;31mEnter 3 for print calendar :  \033[0m")
#print("\033[1;31mwanna see full calendar of the year enter 4  :  \033[0m")

yy = """ 
=========================================================================
=  \033[1;31mEnter 1 for print all keywords. :  \033[0m                       
=  \033[1;32mEnter 2 for check  it is a keyword or not  :  \033[0m           
=  \033[1;31mEnter 3 for print calendar :  \033[0m                             
=  \033[1;31mwanna see full calendar of the year enter 4  :  \033[0m        
=========================================================================
"""
print(yy)




x = int(input("ENTER :- "))


if x == 1:
    print(keyword.kwlist)
elif x == 2:
    y = input("\033[1;31menter keyword : \033[0m")
    print(y, "\033[1;32m is a keyword in py??? ===  \033[0m" , keyword.iskeyword(y))
#else:
  #  print("Invalid input. Please enter 1 or 2.")
    
    
if x == 3:
    z = int(input("ENTER YEAR "))
    v = int(input("please ENTER Month  "))
    print(calendar.month(z,v))
    
elif x == 4:
     n = int(input("ENTER YEAR "))
     print(calendar.calendar(n))
    
else:
    print("Invalid input. Please enter 1 or 2 or 3/4.")
    