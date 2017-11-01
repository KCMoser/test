#first install the dropbox API
pip install dropbox

# Import the Dropbox SDK
import dropbox

# Open file containing access code for read/write (same dir as .py file)
token = open('access_token.txt','r+')
# Assign file contents to variable
access_token=token.read()
#Create instance of Dropbox object using access token
dbx = dropbox.Dropbox(access_token)
# If there is a previous version of file on dropbox, delete it
dbx.files_delete_v2('/results.log')
#Upload the current file
with open("results.log", "rb") as f:
    dbx.files_upload(f.read(), '/results.log', mute = True)
