import sys
from shapely.geometry import Polygon, Point, MultiPoint
import timeit
import ogr
import csv

''' This script takes a shape file intersects it with an OSM changeset file '''

# some global variables are set here
start = timeit.default_timer()

# insert path for your shapefile here
filename = '../rawdata/worldmap/world_country_admin_boundary_shapefile_with_fips_codes.shp'

# load the shape file as a layer
drv = ogr.GetDriverByName('ESRI Shapefile')
ds_in = drv.Open(filename)
lyr_in = ds_in.GetLayer(0)

# field index for which i want the data extracted 
# ("FIPS_CNTRY" was what i was looking for)
idx_reg = lyr_in.GetLayerDefn().GetFieldIndex("FIPS_CNTRY")

def check(lon, lat):
    # create point geometry
    pt = ogr.Geometry(ogr.wkbPoint)
    pt.SetPoint_2D(0, lon, lat)
    lyr_in.SetSpatialFilter(pt)

    # go over all the polygons in the layer see if one include the point
    for feat_in in lyr_in:

        # roughly subsets features, instead of go over everything
        ply = feat_in.GetGeometryRef()

        if ply.Contains(pt):
            return feat_in.GetFieldAsString(idx_reg)

def main(pointfile, outfilestub, startflag=0, step=10):

    startflag = startflag * 100000
    outfile = outfilestub + "_" + str(startflag) + "-" + str(startflag+step) + ".csv"
    count = startflag 
    logfile = 

    with open(pointfile) as infileh:

        infileh.seek(startflag)
        csvreader = csv.DictReader(infileh, delimiter = "\t")
        fields = csvreader.fieldnames
        fields.extend(['fipscode'])

        with open(outfile, "w") as fileh:
            csvwriter = csv.DictWriter(fileh, fields, delimiter="\t")

            for line in csvreader:
                count += 1
                if count < startflag + step:
                    try:
                        pt_lon = (float(line['min_lon']) + float(line['max_lon']))/2
                        pt_lat = (float(line['min_lat']) + float(line['max_lat']))/2
                        line['fipscode'] = check(pt_lon, pt_lat)
                    except:
                        line['fipscode'] = "--"

                    if (count % 10) == 0:
                        stop = timeit.default_timer()
                        sys.stdout.write('\r')
                        sys.stdout.write(str(round(stop-start,2)) + "(s) -- Finished " + str(count))
                        sys.stdout.flush()
                    
                    # print count, line
                    csvwriter.writerow(line)

                elif count > startflag + step:
                    break

    stop = timeit.default_timer()
    print "\n\nwrote " + str(count) + " items in " +  str(stop-start), "(s)"

if __name__ == "__main__":

    ## this is where you set your input and output files. 
    ## use the other script in this package to convert changesets to csv
    pointfile = "../rawdata/change.csv"

    # specify start and end points here.
    startflag = int(sys.argv[1].strip())
    step = int(sys.argv[2].strip())

    # testing output file
    outfilestub = "../filedata/change/country"
    main(pointfile, outfilestub, startflag, step)
