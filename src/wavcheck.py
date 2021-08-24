import os.path
import sys
import wave

def printOKExit():
    sys.stdout.write( 'WAV check OK!' )
    sys.exit( 0 )

def printErrExit( reason ):
    sys.stderr.write( 'WAV check failed.  Reason:\n' )
    sys.stderr.write( ' > ' + str(reason) )
    sys.exit( -1 )
# printErrExit

def printInfo( waveObject ):
    print( 'WAV open success.  Details:' )
    (nchannels,sampwidth,framerate,nframes,comptype,compname) = waveObject.getparams()
    print( ' Channels:', nchannels )
    print( ' Sample Width:', sampwidth )
    print( ' Frame Rate:', framerate )
    print( ' Frame Count:', nframes )
    print( ' Compression Type:', comptype )
# printInfo

def checkSize( f, fileSize ):
    try:
        f.seek(4)
        csBytes = f.read(4)
    except Exception as e:
        raise Exception( 'Trouble reading the filesize from the WAV header' )
    chunkSize = sum( b << (i*8) for i,b in enumerate(csBytes) )
    print( ' Expected size:', chunkSize+8 )
    print( ' Actual size:', fileSize )
    if (fileSize == chunkSize+8):
        print( 'Size check OK.' )
    else:
        raise Exception( 'Size check failed.' )

# checkSize

try:
    fileName = sys.argv[1]
except IndexError:
    printErrExit( 'Please pass the WAV filename to be checked as the sole argument.' )
except Exception as e:
    printErrExit(e)

try:
  fileSize = os.path.getsize(fileName)
  if ( fileSize <= 0):
    printErrExit( 'File is empty.  Not WAV format.' )
  print( 'Trying to open "' + fileName + '"...' )
  f = open( fileName, 'rb' )
except Exception as e:
  printErrExit(e)

try:
  print( 'Passing input to WAV parser...' )
  w = wave.open( f, 'rb' )
  printInfo( w )
  w.close()
  print( 'Checking file length...' )
  checkSize( f, fileSize )
  f.close()
except Exception as e:
  printErrExit( e )

printOKExit()
