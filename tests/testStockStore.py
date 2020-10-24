import unittest
import os

from src.StocksStore import StoreServiceInterface

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

    def test_check_fake_directory_exists(self):
        path= 'xjxjxj'
        file = ''
        storeObject = StoreServiceInterface(path,file)
                
        self.assertEqual(storeObject.check_directory(), False)

if __name__ == '__main__':
    unittest.main()