import sys, os

def interpolate( font1, font2, fileName ):
    file = open( fileName, 'r' )

    for line in file:
        fontInfo = [ x.strip() for x in line.split( "," ) ]
        
        os.system( "./interpolate.pe " + font1 + " "
                   + font2 + " " + "\"" + fontInfo[0]
                   + "\"" + " " + "\"" + fontInfo[1] + "\""
                   + " " + "\""  + fontInfo[2] + "\"" 
                   +  "  "  + "\"" + fontInfo[3] + "\""
                   + " " + fontInfo[4]  )
        
def main( argv ):
    try:
        interpolate( argv[1], argv[2], argv[3] )
    except:
        interpolate( argv[1], argv[2], "default-spec" )

if __name__ == "__main__":
    main( sys.argv )
