oms-changeset
=============

This project includes some python tools to work with OpenStreetMap changeset files

./parsefile.py
This parses a changeset .osm file and produces a csv file for further processing

./pointpolt_country.py
This script uses shapely and ogr to process a changeset csv file produced using the parser above -- for each changeset code the country to which each changeset belongs is identified. Specifically, it will take the midpoint of the changeset bounding box and locate that in a file using a worldmap shapefile.
