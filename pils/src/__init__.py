
# the necessary imports
import calendar
from pilsLocale import pilsLocale

# define arrays for the calendar names, so they can easily be tranlated
weekdayNames = pilsLocale[ 'en' ][ 'weekdayNames' ]
monthNames   = pilsLocale[ 'en' ][ 'monthNames' ]

def monthName2Number( m ):
    """resolve a month's name to its numerical represantation
    """
    for i in range( 12 ):
        if monthNames[ i ] == m:
            return str( i+1 )

def formatMyTime( t ):
    """resolve a "yyyymmddhhmmss"-timestamp to a nice date-format
    """
    return """
%s %s %s %s:%s:%s %s
""" % ( weekdayNames[ calendar.weekday( int( t[:4] ),
                                        int( t[4:6] ),
                                        int( t[6:8] )
                                      )
                    ],
        monthNames[ int( t[4:6] )-1 ],
        t[6:8],
        t[8:10],
        t[10:12],
        t[12:],
        t[:4]
      )
