from colorama import Fore, Back, Style
import os
import time


class UserInterface:

    def __init__(self ):
        pass

    def printWarning(self, msg):
        print(Fore.YELLOW+msg+Style.RESET_ALL)

    def printError(self, msg):
        print(Fore.RED+msg+Style.RESET_ALL)

    def logo(self):
            r = Fore.RED
            g = Fore.GREEN
            y = Fore.YELLOW
            s = Style.RESET_ALL
            logo = r+"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n░"+g+"██████"+r+"╗"+g+"██████"+r+"╗░"+g+"██"+r+"╗░░░"+g+"██"+r+"╗"+g+"███"+r+"╗░░░"+g+"███"+r+"╗"+g+"███████"+r+"╗"+g+"██████"+r+"╗░\n"+g+"██"+r+"╔════╝"+g+"██"+r+"╔══"+g+"██"+r+"╗╚"+g+"██"+r+"╗░"+g+"██"+r+"╔╝"+g+"████"+r+"╗░"+g+"████"+r+"║"+g+"██"+r+"╔════╝"+g+"██"+r+"╔══"+g+"██"+r+"╗\n"+r+"╚"+g+"█████"+r+"╗░"+g+"██████"+r+"╔╝░"+r+"╚"+g+"████"+r+"╔╝"+r+"░"+g+"██"+r+"╔"+g+"████"+r+"╔"+g+"██"+r+"║"+g+"█████"+r+"╗░░"+g+"██████"+r+"╔╝\n░"+r+"╚═══"+g+"██"+r+"╗"+g+"██"+r+"╔═══╝░░░"+r+"╚"+g+"██"+r+"╔╝░░"+g+"██"+r+"║╚"+g+"██"+r+"╔╝"+g+"██"+r+"║"+g+"██"+r+"╔══╝░░"+g+"██"+r+"╔══"+g+"██"+r+"╗\n"+g+"██████"+r+"╔╝"+g+"██"+r+"║░░░░░░░░"+g+"██"+r+"║░░░"+g+"██"+r+"║░"+r+"╚═╝░"+g+"██"+r+"║"+g+"███████"+r+"╗"+g+"██"+r+"║░░"+g+"██"+r+"║\n"+r+"╚═════╝░"+r+"╚═╝░░░░░░░░"+r+"╚═╝░░░"+r+"╚═╝░░░░░"+r+"╚═╝╚══════╝╚═╝░░"+r+"╚═╝\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ "+s+"by FSystem88"+r+" ░░░\n"+y+" [ SMS Spammer ~ v.9.0 ~ MPL-2.0 ]\n [ Dev: FSystem88 ~ prod. by Ca$h&Мир® ]"+s
            print(logo)

    def clear(self):
            os.system('cls' if os.name=='nt' else 'clear')

    def getUserInput(self, question, options):
        # print(question)
        availibleAnswer = []
        for i in range(len(options)):
            availibleAnswer.append(i+1)

        for x in range(len(options)):
            print(str(availibleAnswer[x])+". "+options[x]) 

        choice=-1
        while choice not in availibleAnswer:
            userInput=input(Fore.BLUE+question+Style.RESET_ALL+"~/")
            try:
                choice=int(userInput)
                if choice not in availibleAnswer:
                    self.printError("Неверный выбор, попробуйте еще раз! (Чтобы выйти нажмите CTRL-Z)")
            except:
                self.printError("Неверный выбор, попробуйте еще раз! (Чтобы выйти нажмите CTRL-Z)")

        return choice
