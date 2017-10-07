import sys
import logging

# Set up timestamp and logfile name...
logging.basicConfig(filename='results.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# Check Python version...
if sys.version_info[0] < 3:
    print ('This program requires Python version 3')
else: print ('Current version is '+sys.version)
logging.info('Python version is ' + sys.version)
logging.info('Operating system is: '+ sys.platform)
