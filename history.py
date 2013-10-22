import sys
sys.path.append('/usr/lib/python2.4/site-packages/')
from xml.dom.minidom import parse
from elementtree import ElementTree

class Node(object):

    def __init__(self, node):
        self.id = node.get("id")
        self.lat = node.get("lat")
        self.lon = node.get("lon")
        self.timestamp = node.get("timestamp")
        self.changeset = node.get("changeset")
        self.uid = node.get("uid")
        self.user = node.get("user")
        pass

    def print_node(self):
        print self.id
        print self.timestamp
        print self.lat, self.lon
        print self.uid, self.user

    def write_node(self, outfile="parsed.csv"):
        with open(outfile,"a") as f:
            line = [self.id, self.timestamp, self.lat, self.lon, self.uid, self.user]
            line = ("\t").join(line) + "\n"
            f.write(line.encode('utf-8'))

class Region(object):

    def __init__(self, inputfile = "cyprus-latest.osm"):
        self.inputpath = "/mnt/nfs6/wikipedia.proj/osm/rawdata/" + inputfile
        self.outputpath = "parsed.csv" 
        self.nodes = list()
        pass

    def add_node(self, node):
        self.nodes.append(node)
        #node.print_node()
        pass

    def read_input(self):
        tree = ElementTree.parse(self.inputpath)
        root = tree.getroot()
        for node in root.findall('node'):
            new_node = Node(node)
            self.add_node(new_node)
        pass
            
    def write_output(self):
        print "now writing"
        for node in self.nodes:
            node.write_node(self.outputpath)
        pass

#if __name__ == '__main__':
#    unittest.main()



