import sys



from draw_geo_maps import *

csvfile = sys.argv[1]+".csv"
dest = sys.argv[1]+".png"
make_plot(csvfile, dest)