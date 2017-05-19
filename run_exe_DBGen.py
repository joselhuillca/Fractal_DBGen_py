import subprocess

class RunDBGen:
    def __init__(self,path,file_exe):
        self.path = path
        self.exe = file_exe

    def execute(self,file_stc):
        comand = "wine " + self.path + self.exe
        comand_all = comand + " " + file_stc
        print(comand_all)
        subprocess.call(comand_all, shell=True)
