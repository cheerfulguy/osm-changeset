import sys
sys.path.append('/usr/lib/python2.4/site-packages/')
from xml.dom.minidom import parse
from elementtree import ElementTree

class Node(object):

    def __init__(self, node):
        self.id = node.attributes["id"].value
        self.lat = node.attributes["lat"].value
        self.lon = node.attributes["lon"].value
        self.timestamp = node.attributes["timestamp"].value
        self.changeset = node.attributes["changeset"].value
        self.uid = node.attributes["uid"].value
        self.user = node.attributes["user"].value
        pass

    def print_node(self):
        print self.id
        print self.timestamp
        print self.lat, self.lon
        print self.uid, self.user

    def write_node(self, outfile="parsed.csv"):
        with open(outfile,"a") as f:
            line = [self.id, self.timestamp, self.lat, self.lon, self.uid, self.user]
            line = ("\t").join(line)
            f.write(line)

class Region(object):

    def __init__(self, inputfile = "cyprus-latest.osm"):
        self.inputpath = "/mnt/nfs6/wikipedia.proj/osm/rawdata/" + inputfile
        self.outputpath = "parsed.csv" 
        self.nodes = list()
        pass

    def add_node(self, node):
        self.nodes.append(node)
        node.print_node()
        pass

    def read_input(self):
        tree = ElementTree.parse(self.inputpath)
        root = tree.getroot()
        for node in root.findall('node'):
            new_node = Node(node)
            self.add_node(new_node)
        pass
    
    def read_input2(self):
        dom = parse(self.inputpath)
        for node in dom.getElementsByTagName('node'):
            print node
            
    def write_output(self):
        print "hello"
        for node in self.nodes:
            node.write_node(self.outputpath)
        pass

#if __name__ == '__main__':
#    unittest.main()



