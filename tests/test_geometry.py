import unittest
import logging

log_level = logging.DEBUG
logging.basicConfig(level=log_level)

class Geomtry2DTest(unittest.TestCase):

    def setUp(self):
    #a method to be called everytime before each test
        logging.info()


    def tearDown(self):
    #a method to be called everytime after each test
        logging.info()


    def test_area(self):
        logging.info()



class Geomtry3DTest(unittest.TestCase):

    def setUp(self):
    # a method to be called everytime before each test
        logging.info()


    def tearDown(self):
    # a method to be called everytime after each test
        logging.info()


    def test_volume(self):
        logging.info()


    def test_is_in_plane(self):
        logging.info()
