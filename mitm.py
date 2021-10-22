import os
import importlib

col = {"white": "[37m",
       "red": "[31m",
       "green": "[32m"
}

if os.geteuid()==0:
  pass
else:
  print(col["red"]+"[!] user needs to be root!")
  print("[!] re-run as root!"+col["white"])
  quit()
  
def use(mod):
    try:
        my_module = importlib.import_module(mod)
        return my_module, True
    except ModuleNotFoundError:
        print("[!] module ("+mod+") not found!")
        return None, False

def list(t):
    dirs = ["basic","social","exploit"]
    if t == "None":
        files = []
        for d in dirs:
            files.append(os.listdir(str("mod/"+d)))
        
        c = 0
        for c in range(len(files)):
            i = files[c]
            d = dirs[c]
            print("\n\n============["+dirs[c]+"]============")
            for x in i:
                print("mod/"+d+"/"+x)
            print("================================\n\n")

    else:
        try:
            files = os.listdir(str("mod/"+t))
            print("\n\n============["+t+"]============")
            for i in files:
                print("mod/"+t+"/"+i)
            print("================================\n\n")
        except FileNotFoundError:
            print("[!] module file ("+t+") not found!")
            

os.system("clear")
banner = col["red"] +"""

           _ _                               
 _ __ ___ (_) |_ _ __ ___        _ __  _   _ 
| '_ ` _ \| | __| '_ ` _ \ _____| '_ \| | | |
| | | | | | | |_| | | | | |_____| |_) | |_| |
|_| |_| |_|_|\__|_| |_| |_|     | .__/ \__, |"""+col["white"]+"""
================================"""+col["red"]+"""|_|"""+col["white"]+"""===="""+col["red"]+"""|___/"""+col["white"]+"""= 
 """+col["red"]+""" a man in the middle script too with more!  """+col["white"]+"""
=============================================

[?] use the command "help" for a help menu

"""+col["white"]
print(banner)

help = """
use """+col["green"]+""" *module* ->  """+col["white"]+""" select module to use
run          ->   run the selected attack
list """+col["green"]+""" *type*  -> """+col["white"]+"""  list attacks (the type of attack is optional)
clear        ->   clear the screen 

"""

mod = "None"
sel = False

try:
    while True:
        cho = input("\n┌──["+col["green"]+"/mitm/"+mod+col["white"]+"]\n└─$ ")

        if cho == "help":
            print(help)
        elif cho == "clear":
            os.system("clear")
            print(banner)


        elif "list" in cho:
            cho = cho.split(" ")
            try:
                l = cho[1]
            except IndexError:
                l = "None"
            list(l)


        elif "use" in cho:
            cho = cho.split(" ")
            try:
                mod = cho[1]
                mo = mod.replace("/",".")
                mo = mo.replace(".py","")
                m = True
            except IndexError:
                print("[!] no module selected!")
                m = False
            if m:
                run, sel = use(mo)
            else:
                pass
        elif cho == "run":
            if sel:
                run.atk()
            else:
                print("[!] no module selected!")
        
        elif cho == "" or " " or "\n":
            print("\n\n")
        else:
            print("[!] not renonised command!")
except KeyboardInterrupt:
    print("\n[!] qutting...")
    quit()