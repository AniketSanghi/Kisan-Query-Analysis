import sys

path = "../../plots/maps/"
sys.path.insert(1, path)

from draw_geo_maps import *

csvfile = "../data/"+sys.argv[1]+".csv"
dest = "../plots/"+sys.argv[1]+".png"
make_plot(csvfile, dest, path)