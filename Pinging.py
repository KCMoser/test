import sys                                  # For grabbing OS version
import subprocess

os_name=sys.platform                        # Assign OS to variable
from os import system as system_call        # Execute a shell command

host='10.11.32.94'                        # Assigned for testing

# Set parameters as function of OS
if os_name=="win32":
    options=str('-n 1')
else:
    options=str('-c 1')
#print(options)                              # For testing

    # Pinging
#subprocess.run(['ping', host, options], stdout=subprocess.PIPE)
#print('ping '+host+ ' ' +options)
pingresult=subprocess.getoutput('ping' +' '+ host+' '+ options)
print(pingresult)

if 'unreachable' in pingresult:
    print(host+ " is Offline")
elif 'Request' in pingresult:
    print(host+ " is Offline")
else:
    print(host+ " is Online")
