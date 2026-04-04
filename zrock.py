###############################
##Z ROCK 
## 2026.03.18
## cred By lasith ruwantha Amarwansha
###############################


import zipfile
from sys import argv
from time import sleep
from rock.zip import cmd
from rock.log import Log
"""
Cli argv get agrment
"""

multe = "\033[0;32m[\033[1;31m!\033[32m]"

def help():
    print("""
python zrock.py -zip <zipfile.zip> -pwd <passwd.txt>\n
Options:
  -zip: Zip Files Path
  -pwd: passworld list file path 
Exaple:
  python zrock.py -zip file.zip -pwd passworld.txt
  """)


def check(file):
    if zipfile.is_zipfile(file):
        print("✔️\033[0;32m Zip File Is Testd.")
        return True
    else:
        print("️⛔\033[0;31m Is Not Zip File. Or Path Problem")
        return False


def main():
    try:
        if "--help" in argv or "-h" in argv:
            help()
        elif "-zip" in argv and "-pwd" in argv:
            zipIndex = argv.index("-zip") + 1
            pwdIndex = argv.index("-pwd") + 1

            zip_file = argv[zipIndex]
            passwd_file = argv[pwdIndex]
            Log()
            test = check(zip_file)
            if test == False: return
            sleep(2.1)
            unziper = cmd()
            unziper.Crack(zip_file, passwd_file)
        else:
            print(f"{multe} \033[0m\033[1m Worong agrment\ntype:\n  python zrock.py --help")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
