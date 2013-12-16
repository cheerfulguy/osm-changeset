oms-changeset
=============

This is a python implementation of shapely, fiona and ogr that will take an openstreetmap changeset file, and for each changeset code the country to which each changeset belongs. Specifically, it will take the midpoint of the changeset bounding box and locate that in a file using a worldmap shapefile.