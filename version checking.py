import sys
import platform
import logging

# Set up timestamp and logfile name...
logging.basicConfig(filename='results.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# Check Python and OS version...
if sys.version_info[0] < 3:
    print ('This program requires Python version 3')
else: print ('Current version is '+sys.version[0]+sys.version[1] +sys.version[2])
print ('Operating system is: '+platform.system()+' '+platform.release())
logging.info('Python version is ' +sys.version[0]+sys.version[1] +sys.version[2])
logging.info('Operating system is: '+platform.system()+' '+platform.release())
