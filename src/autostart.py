import os
import threading as th

def startMain():
    path = os.getcwd()
    print(path)
    os.chdir(path)
    os.system("python main.py")

def openIndexhtml():
    path = os.getcwd()
    print(path)
    os.chdir(path)
    os.system("start index.html")

class AutoStart(th.Thread):
    def __init__(self, ID, scriptName):
        super().__init__()
        self.ID = ID
        self.scriptName = scriptName
        self.start()

    def run(self):
        if self.ID == 1:
            print(f"Starte {self.scriptName}")
            startMain()
            print(f"{self.scriptName} wurde beendet")
        elif self.ID == 2:
            print(f"Starte {self.scriptName}")
            openIndexhtml()
            print(f"{self.scriptName} wurde beendet")



if __name__ == "__main__":
    th1 = AutoStart(1, "main.py")
    th2 = AutoStart(2, "index.html")
