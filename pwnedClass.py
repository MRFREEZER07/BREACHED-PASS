import requests
from colorama import Fore
from colorama import Back

from prettytable import PrettyTable

class Pwned():
    def __init__(self,email):
        self.email=email
        self.key="5a55de396be770d56804a34d6c586360"
        self.makeRequest()

    def processOutput(self):
        self.dict ={}
        self.op =self.op.split('\n')
        for i in range(len(self.op)-1):
            l=[]
            l=self.op[i].split(':')
            if l != "":
                self.dict[i]=l[1]
            
        return self.dict

    def makeRequest(self):
        r = requests.get(f"https://myrz.org/api/email_search.php?key={self.key}&email={self.email}")
        self.op =""
        
        self.message=""

        if '"success":true' in r.text:
            for i in r.json()["results"]:
                self.op += i["line"] + "\n"
            self.processOutput()
            self.printOp(self.dict)
         
        
        elif '"resultCount":0' in r.text:
            self.printOp("MESSAGE --> Not Found")

        elif 'Введите корректный email или логин для поиска':         
            self.printOp("MESSAGE --> Enter a valid email address")

        else:
            self.printOp("MESSAGE --> Unknown Error")


    def printOp(self,d):
        if(type(d) is dict):
            
            table = PrettyTable()
            table.field_names=['S.no','Password']
            for i in range(len(d.items())):
                table.add_row([i,d[i]])
            print(Fore.GREEN)
            print(table)
        else:
            print(f"{Fore.LIGHTRED_EX}"+d)
        

           


