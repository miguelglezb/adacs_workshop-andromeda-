#! /usr/bin/python3
# -*- coding: utf-8 -*-

"""
A script to simulate a population of stars around the Andromeda galaxy """

import random
from math import cos,pi
import argparse
NSRC = 1_000_000


def get_radec():
    """
    Determine the Andromeda location. It uses the coordinates RA and DEC from wikipedia and transforms them into hours.
    This function returns a tuple in the form (ra, dec)
    """
    RA = '00:42:44.3'
    DEC = '41:16:09'

    d, m, s = DEC.split(':')
    dec = int(d)+int(m)/60+float(s)/3600 #Converts dec into hours

    h, m, s = RA.split(':')
    ra = 15*(int(h)+int(m)/60+float(s)/3600) #Converts ra into hours
    ra = ra/cos(dec*pi/180)
    return (ra, dec)

def make_stars(ra,dec,num_stars):
    """
    Make num_stars (number of stars) within 1 degree of Andromeda
    """
    ras = []
    decs = []
    for i in range(NSRC):
        ras.append(ra + random.uniform(-1,1))
        decs.append(dec + random.uniform(-1,1))
    return(ras, decs)



def main():
    ra,dec = get_radec()
    ras,decs = make_stars(ra,dec,NSRC)
    with open ('catalog.csv','w', encoding="utf-8") as f:
        print("id,ra,dec", file=f)
        for i in range(NSRC):
            print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f)



def skysim_parser():
    """
    Configure the argparse for skysim

    Returns
    -------
    parser : argparse.ArgumentParser
        The parser for skysim.
    """
    parser = argparse.ArgumentParser(prog='sky_sim', prefix_chars='-')
    parser.add_argument('--ra', dest = 'ra', type=float, default=None,
                        help="Central ra (degrees) for the simulation location")
    parser.add_argument('--dec', dest = 'dec', type=float, default=None,
                        help="Central dec (degrees) for the simulation location")
    parser.add_argument('--out', dest='out', type=str, default='catalog.csv',
                        help='destination for the output catalog')
    return parser

if __name__ == "__main__":
    parser = skysim_parser()
    options = parser.parse_args()
    # if ra/dec are not supplied the use a default value
    if None in [options.ra, options.dec]:
        ra, dec = get_radec()
    else:
        ra = options.ra
        dec = options.dec
    
    ras, decs = make_stars(ra,dec,NSRC)
    # now write these to a csv file for use by my other program
    with open(options.out,'w') as f:
        print("id,ra,dec", file=f)
        for i in range(NSRC):
            print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f)
    print(f"Wrote {options.out}")


if __name__  == '__main__':
    main()
