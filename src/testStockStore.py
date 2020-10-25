import unittest
import os

from StocksStore import StoreServiceInterface
from testfixtures import TempDirectory, compare

class TestStocksStore(unittest.TestCase):

    def setUp(self):
        self.test_dir = TempDirectory()
        
        pass

    def tearDown(self):
        self.test_dir.cleanup()
        pass

    def rowToByte(self,row):
        row = sum(row, [])
        return bytes(','.join(row)+'\r\n','UTF-8')


    def test_creation_object(self):
        path= self.test_dir.path
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
        path= self.test_dir.path
        file = ''
        storeObject = StoreServiceInterface(path,file)
           
        self.assertEqual(storeObject.check_directory(), True)

    def test_check_fake_directory_not_exists(self):
        path= 'xjxjxj'
        file = ''
        storeObject = StoreServiceInterface(path,file)
                
        self.assertEqual(storeObject.check_directory(), False)

    def test_file_is_create(self):
        path =  self.test_dir.path
        file = 'testFile'
        storeObject = StoreServiceInterface(path,file)
        storeObject.open_file()
        storeObject.close_file()
                
        self.assertEqual(os.path.isfile(os.path.join(path, file)), True) 

    def test_write_list_to_file(self):
        path =  self.test_dir.path
        file = 'testFile.csv'
        storeObject = StoreServiceInterface(path,file)
        storeObject.open_file()
        row = ['dato','01','08']
        storeObject.write_row(row)
        storeObject.close_file()

        compare(self.test_dir.read(file), self.rowToByte(row))

    def test_write_string_to_file(self):
        path =  self.test_dir.path
        file = 'testFile.csv'
        storeObject = StoreServiceInterface(path,file)
        storeObject.open_file()
        row = 'hola'
        storeObject.write_row(row)
        storeObject.close_file()

        compare(self.test_dir.read(file), self.rowToByte(row))

    def test_write_list_multiple_rows_to_file(self):
        path =  self.test_dir.path
        file = 'testFile.csv'
        storeObject = StoreServiceInterface(path,file)
        storeObject.open_file()
        row = [['dato','01','08'],['algo','09','08']]
        storeObject.write_row(row)
        storeObject.close_file()

        compare(self.test_dir.read(file), self.rowToByte(row))

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStocksStore)
    unittest.TextTestRunner(verbosity=2).run(suite) 