
import os

class StoreServiceInterface():

#no hay multiple contructors como hacemos si no envian nada


    def __init__(self, path: str, file_name: str):
        
        if (not path):
            path = os.getcwd()
        if (not file_name):
            file_name = 'StoreServiceFile'
        self.path = path
        self.file_name = file_name
        

    def write_row(self, full_file_name: str):
        new_file=open("newfile.txt",mode="a+",encoding="utf-8")

    def check_directory(self):
        os.DirEntry()
