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
            l = Fore.RED
            r = Fore.LIGHTRED_EX
            turbo ="___ _  _ ____ ___  ____\n"+\
                   " |  |  | |__/ |__] |  |\n"+\
                   " |  |__| |  \ |__] |__|\n"
            spymer=r+"  @@@@@@ @@@@@@@  @@@ @@@ @@@@@@@@@@  @@@@@@@@ @@@@@@@ \n"+\
                   r+" !@@     @@!  @@@ @@! !@@ @@! @@! @@! @@!      @@!  @@@\n"+\
                   r+"  !@@!!  @!@@!@!   !@!@!  @!! !!@ @!@ @!!!:!   @!@!!@! \n"+\
                   l+"     !:! !!:        !!:   !!:     !!: !!:      !!: :!! \n"+\
                   l+" ::.: :   :         .:     :      :   : :: :::  :   : :\n"
            logo=turbo+spymer+Style.RESET_ALL
            print(logo)

    def clear(self):
            os.system('cls' if os.name=='nt' else 'clear')

    def getUserIntegerInput(self, question):
        print(question)
        try:
            iterationsNumber = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
            int(iterationsNumber)
            return iterationsNumber
        except:
            self.printError("Разрешены только цифры!")
            self.getUserIntegerInput(question)



    def getUserChoice(self, question, options):
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
