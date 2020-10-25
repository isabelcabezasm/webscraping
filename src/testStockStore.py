import unittest
import os

from StocksStore import StoreServiceInterface

class TestStocksStore(unittest.TestCase):
    def test_creation(self):
        path= os.getcwd()
        file = 'file'
        storeObject = StoreServiceInterface(path,file)
                
        self.assertEqual(storeObject.path, path)
        self.assertEqual(storeObject.file_name, file)

    def test_creation_with_empty_values(self):
        path= ''
        file = ''
        storeObject = StoreServiceInterface(path,file)
              
        self.assertEqual(storeObject.path, os.getcwd())
        self.assertEqual(storeObject.file_name, 'StoreServiceFile')

    def test_check_real_directory_exists(self):
        path= os.getcwd()
        file = ''
        storeObject = StoreServiceInterface(path,file)
           
        self.assertEqual(storeObject.check_directory(), True)

    def test_check_fake_directory_not_exists(self):
        path= 'xjxjxj'
        file = ''
        storeObject = StoreServiceInterface(path,file)
                
        self.assertEqual(storeObject.check_directory(), False)

    def test_file_is_create(self):
        path =  os.getcwd()
        file = 'testFile'
        storeObject = StoreServiceInterface(path,file)
        storeObject.open_file()
                
        self.assertEqual(os.path.isfile(os.path.join(path, file)), True) 
        if(os.path.isfile(os.path.join(path, file))):
            os.remove(os.path.join(path, file))      

    # def test_write_row(self):
    #     path =  os.getcwd()
    #     file = 'testFile'
    #     storeObject = StoreServiceInterface(path,file)
    #     storeObject.open_file()
    #     row = [[1],[2]]
    #     storeObject.write_row(row)
                
    #     self.assertEqual(os.path.isfile(os.getcwd()+"/"+file), True) 
    #     if(os.path.isfile(os.getcwd()+"/"+file)):
    #         os.remove(os.getcwd()+"/"+file)     


if __name__ == '__main__':
    unittest.main()