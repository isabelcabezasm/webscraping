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


if __name__ == '__main__':
    unittest.main()