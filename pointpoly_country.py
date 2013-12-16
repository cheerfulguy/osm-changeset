import sys
from shapely.geometry import Polygon, Point, MultiPoint
import timeit
import ogr
import csv

class MyPoint(Point):
    def __init__(self,lon=-1,lat=-1, pntid=-1, name=""):

        self.pnt = Point(float(lon),float(lat))
        self.name = name.replace('"','').strip()
        self.id = pntid
        self.countyname = ""
        self.countycode = ""

    def setpoly(self, countycode = ""):
        if countycode is not None:
            self.countycode = countycode
        else:
            self.countycode = "nomatch"

    def writepoint(self, fileh):
        line = [str(point.id), str(point.pnt.x), str(point.pnt.y), point.name, point.countycode]
        linestring = (", ").join(line) + "\n"
        if point.countycode != "":
                fileh.write(linestring)

def check(lon, lat):
    # create point geometry
    pt = ogr.Geometry(ogr.wkbPoint)
    pt.SetPoint_2D(0, lon, lat)
    lyr_in.SetSpatialFilter(pt)

    # go over all the polygons in the layer see if one include the point
    for feat_in in lyr_in:

        # roughly subsets features, instead of go over everything
        ply = feat_in.GetGeometryRef()

        # test
        if ply.Contains(pt):

            # TODO do what you need to do here
            # print lon, lat, feat_in.GetFieldAsString(idx_reg)
            return feat_in.GetFieldAsString(idx_reg)

def writetocsv(self, points, outfile="os-highway-county.csv"):
    with open(outfile, "w") as f:
        for point in points:
            pass

def readpoints(pointfile):
    count = 0
    points = []
    with open(pointfile) as f:
        for line in f:
            count=count+1
            if count > 1:
                items = line.split("\t")

                points.append(pnt)
    return points

start = timeit.default_timer()

pointfile = "../rawdata/change-head.csv"
pointfile = "../rawdata/change.csv"
outfile = "../filedata/change_plus_cntry.csv"

filename = '../rawdata/worldmap/world_country_admin_boundary_shapefile_with_fips_codes.shp'

# load the shape file as a layer
drv = ogr.GetDriverByName('ESRI Shapefile')
ds_in = drv.Open(filename)
lyr_in = ds_in.GetLayer(0)

# field index for which i want the data extracted 
# ("satreg2" was what i was looking for)
idx_reg = lyr_in.GetLayerDefn().GetFieldIndex("FIPS_CNTRY")

count = 0

with open(pointfile) as infileh:
    csvreader = csv.DictReader(infileh, delimiter = "\t")
    fields = csvreader.fieldnames
    fields.extend(['fipscode'])

    with open(outfile, "a") as fileh:
        csvwriter = csv.DictWriter(fileh, fields, delimiter="\t")
        for line in csvreader:
            count += 1
            try:
                pt_lon = (float(line['min_lon']) + float(line['max_lon']))/2
                pt_lat = (float(line['min_lat']) + float(line['max_lat']))/2

                line['fipscode'] = check(pt_lon, pt_lat)
            except:
                line['fipscode'] = "NF"

            if (count % 1000) == 0:

                stop = timeit.default_timer()
                print str(stop-start), "(s)", " -- Finished ", str(count)
                
            csvwriter.writerow(line)

stop = timeit.default_timer()
print "wrote " + str(count) + " items in " +  str(stop-start), "(s)"







