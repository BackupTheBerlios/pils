#!/usr/bin/env python

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# pils - Python Irc Log Stats ( http://pils.berlios.de )
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# a tiny python script to analyze logfiles of irc-conversations and
# generate corresponding html-output
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# this file offers the first external module - it generates images.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# (c) 2004 - Nikolaus Schlemm
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import os, md5, math, Image

class pilsImage:
    """ a rather simple base-class for generating graphs
    """
    def __init__( self, width, height, bgcolor=255 ):
        """ the constructor
        """
        self.img    = Image.new( 'L', ( width, height ), bgcolor )
        self.height = height
        sef.width   = width

    def draw( self, x, y, color=0 ):
        """ draw a pixel - if the coordinates are correct
        """
        if x >= 0 and y >= 0 and x < self.width and y < self.height:
            self.img.putpixel( ( x, y ), color )

    def drawBox( self, x1, y1, x2, y2, color=0 ):
        """ draw a box
        """
        if x1 > x2:
            self.drawBox( x2, y1, x1, y2, color )
        elif y1 > y2:
            self.drawBox( x1, y2, x2, y1, color )
        else:
            for x in range( x1, x2+1 ):
                for y in range( y1, y2+1 ):
                    self.draw( x, y, color )

    def save( self, path ):
        """ save the generated image to a specified path
        """
        if os.path.exists( os.path.dirname( path ) ):
            fh = file( path, 'w' )
            self.img.save( fh )
            fh.close()



def nickActivity( channel, nick, activity ):
    """ generates a graph showing a nick's activity
        and returns the location where it's stored
    """
    img = pilsImage( 48, 20 )
    img.drawBox( 0, 0, 49, 19, 0 )
    for x in range( 24 ):
        if not activity.has_key( x ) or activity[ x ] < 0:
            y = 0
        elif activity[ x ] > 10:
            y = 10
        else:
            y = activity[ x ]
        if x > 0:
            img.drawBox( x*2, 18-y-activity[x-1], x*2, 19, 48*math.sqrt( (y+activity[x])/2+1 ) )
            img.drawBox( x*2, 17-y-activity[x-1], x*2, 17-y-activity[x-1], 191 )
        img.drawBox( x*2+1, 18-y*2, x*2+1, 19, 64*math.sqrt( y+1 ) )
        img.drawBox( x*2+1, 17-y*2, x*2+1, 17-y*2, 191 )

    path = os.path.join( os.getcwd(), 'activity', '%s.png' % md5.md5( "%s/%s" % ( channel, nick ) ).hexdigest() )
    img.save( path )
    # return the path relative to the current dir
    return path[ len( os.getcwd() ): ]

