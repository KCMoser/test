#first install the dropbox API
pip install dropbox

# Include the Dropbox SDK
import dropbox

#Create instance of Dropbox object
dbx = dropbox.Dropbox('') # add access token

#Upload the file
with open("results.log", "rb") as f:
    dbx.files_upload(f.read(), '/results.log', mute = True)
