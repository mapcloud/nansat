#!/usr/bin/env python
#
# Analog to gdal_translate for Nansat datasets.
# Any gdal_translate-options can be used, 
# but band number refers to the Nansat dataset


import sys
import os

tmpfile = 'nansat_translate_test.VRT'

def main():
    if (len(sys.argv) <= 2):
        sys.exit('Usage: nansat_translate <input_file> <output_file> <gdal_translate options>')
    
    outfile = sys.argv[2]
    options = " ".join(sys.argv[3:])
    
    from nansat import Nansat
    n = Nansat(sys.argv[1])
    n.vrt.export(tmpfile)
    os.system('gdal_translate ' + tmpfile + ' ' + outfile + ' ' + options)
    os.remove(tmpfile)

if __name__ == '__main__':
    main()