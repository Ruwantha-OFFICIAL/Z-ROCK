import zipfile
from zipfile import ZipFile
from .log import Log
import os

# Signels
plus = "\033[0;32m[\033[1;33m+\033[32m]"
mines = "\033[0;32m[\033[0;31m-\033[32m]"
multe = "\033[0;32m[\033[1;31m!\033[32m]"


class cmd:
    def ZipFile(self, file, passwd):
            try:
                with ZipFile(file, "r") as files:
                    files.extractall(path="./Out", pwd=passwd.encode("utf-8"))
                    os.system("clear")
                    Log()
                    print(f"{plus}\033[1;34m FIND PASSWORD:\033[0m {passwd}")
                    self.ethical()
                    return True
            except zipfile.BadZipFile:
                print(f"{multe}\033[0;31m Bad Zip File.\n\n")
                return True
            except zipfile.LargeZipFile:
                print(f"{multe}\033[0;31m Large Zip File.")
                return True
            except Exception as e:
                print(f"{mines} \033[1;33m TRY:\033[0m {passwd}")
                return

    def Crack(self, file, passwd):
        try:
            os.system("rm -rf ./Out")
            with open(passwd, "r") as pwd:
                for line in pwd:
                    key = line.strip()
                    done = self.ZipFile(file, key)
                    if done:
                        break

        except Exception as e:
            print(f"{mines} \033[1;33mError: {e}")

    def ethical(self):
        print(
            """\033[0;31m____________________⚠Warning⚠___________________\n\033[1;33mEthical And Education purposes,private usage only.\033[0m"""
        )


###############################
##Z ROCK 
## 2026.03.18
## cred By lasith ruwantha Amarwansha
###############################