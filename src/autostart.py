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
    def __init__(self, ID):
        super().__init__()
        self.ID = ID
        self.start()

    def run(self):
        if self.ID == 1:
            startMain()
        elif self.ID == 2:
            openIndexhtml()



if __name__ == "__main__":
    th1 = AutoStart(1)
    th2 = AutoStart(2)
