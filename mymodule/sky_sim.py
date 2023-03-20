#! /usr/bin/python3
# -*- coding: utf-8 -*-

"""
A script to simulate a population of stars around the Andromeda galaxy """

import random
from math import cos,pi

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


if __name__  == '__main__':
    main()
