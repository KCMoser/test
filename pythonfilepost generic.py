#first install the dropbox API
pip install dropbox

# Include the Dropbox SDK
import dropbox

#Create instance of Dropbox object
dbx = dropbox.Dropbox('') # add access token

#Upload the file
dbx.files_upload("results.log", '/results.log')
