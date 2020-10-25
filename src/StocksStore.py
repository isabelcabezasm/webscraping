
import os
import csv

class StoreServiceInterface():

#no hay multiple contructors como hacemos si no envian nada


    def __init__(self, path: str, file_name: str):
        
        if (not path):
            path = os.getcwd()
        if (not file_name):
            file_name = 'StoreServiceFile'
        self.path = path
        self.file_name = file_name
        
    def open_file(self):
        self.new_file=open(os.path.join(self.path, self.file_name),mode="a+",encoding="utf-8", newline='',)

    def close_file(self):
        self.new_file.close()



    def check_directory(self):
        if(os.path.exists(self.path)):
            return True
        else:
            return False


    def write_row(self, row):
        if (not self.new_file):
            self.open_file()
        stocks_writer = csv.writer(self.new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        stocks_writer.writerow(row)