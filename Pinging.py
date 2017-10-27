import sys                                  # For grabbing OS version
import subprocess

os_name=sys.platform                        # Assign OS to variable

host='10.11.32.94'                        # Assigned for testing

# Set parameters as function of OS
if os_name=="win32":
    options=str('-n 1')
else:
    options=str('-c 1')

    # Pinging
pingresult=subprocess.getoutput('ping' +' '+ host+' '+ options)
print(pingresult)
if 'unreachable' in pingresult:
    print(host+ " is Offline")
elif 'Request' in pingresult:
    print(host+ " is Offline")
else:
    print(host+ " is Online")
