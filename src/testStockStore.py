import unittest
import os

from StocksStore import StoreServiceInterface
from testfixtures import tempdir, compare

class TestStocksStore(unittest.TestCase):

    def setUp(self):
        #nothing to do here
        pass

    def tearDown(self):
        #nothing to do here
        pass


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
        storeObject.close_file()
                
        self.assertEqual(os.path.isfile(os.path.join(path, file)), True) 
        if(os.path.isfile(os.path.join(path, file))):
            os.remove(os.path.join(path, file))      

    @tempdir()
    def test_written_contents_to_file(self,dir):
        # dir.write('test.txt', b'some foo thing')
        # foo2bar(dir.path, 'test.txt')
        

        compare(dir.read('test.txt'), b'some bar thing')

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStocksStore)
    unittest.TextTestRunner(verbosity=2).run(suite) 