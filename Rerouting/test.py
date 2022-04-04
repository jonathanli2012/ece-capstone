from pyrosm import OSM, get_data
import geopandas as gpd
import pandas as pd
import networkx as nx
import matplotlib


print("HUUH 1 \n")
osm = OSM("my_data/new-york-latest.osm.pbf")
print("HUUH 2 \n")
roads = osm.get_network(network_type="driving")

print("HUUH 3 \n")
roads.plot(figsize=(10,10))
roads.head(2)
print("HUUH 4 \n")