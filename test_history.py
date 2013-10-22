import unittest
from history import Node, Region

class SimpleTest(unittest.TestCase):

    def setUp(self):
        self.place = Region(inputfile = "cyprus-latest.osm")
        pass

    # read input file and parse it
    def test_parse(self):
        print "processing"
        self.place.read_input()
        self.place.write_output()
        pass

    def test_write(self):
        pass


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()


