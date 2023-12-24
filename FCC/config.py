import random

global Web
Web = ""

site = True

if site == False :
    Web = "<CommingSoon>\n"
if site == True :
    Web = ">> https://fonixcommunity.wixsite.com/bots"

nbr_er = random.randint(100, 600)

def error() :
    raise random.choice([ValueError, TypeError, ZeroDivisionError, IndexError])

CR = "\033[0m "

R_T = "\033[1;35m[Test Result] >\033[5;34m "

E_R = f"\033[1;4m\033[33m[Error] : {error} \n\n\033[34m[+]\033[32;1[[ErrorType] : \033[1;0;46mFUEETC-{nbr_er}\033"

R = "\033[1;32m[Result] >\033[1;34m "

W_U = f"\033[1;32m[Message] > \033[1;35mHello User Welcome Here !\n\n\033[31m[#] : \033[4;34m\033[1m This Programe Is Made By (fonix_206) At Discord\n\n\033[0m\033[31m[#] : \033[1;33m Check This WebSit\033[1,4;31m {Web}\033[0;0m"

Ms = f"\033[1;32m[Message] : \033[1;35m "

B_r = "\033[31m[+]\033[32m\033[5;34m (~info-Bot) :\033[0m\033[36m\033[1m "

F_r = "\033[31m[+]\033[0m\033[5;34m (~file) : \033[0m\033[37m\033[1m "

New = "\033[35m[~@~]\033[0m :\033[1;34m  "