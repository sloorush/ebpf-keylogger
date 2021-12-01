from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from pydrive import drive

from oauth2client.service_account import ServiceAccountCredentials

import os

cwd = os.getcwd()
SECRETS_FILE = cwd + "/client_secrets.json"
print(SECRETS_FILE)

gauth = GoogleAuth()
scope = ["https://www.googleapis.com/auth/drive"]
gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name(
    SECRETS_FILE, scope
)

drive = GoogleDrive(gauth)


path = os.path.join(cwd, "OUTFILE.txt")
path = cwd + "/OUTFILE.txt"
file1 = drive.CreateFile({"parents": [{"id": "10qtlm8xcOrs15MUhOD9y6WAr0_6rw1M5"}]})
file1.SetContentFile(path)
file1.Upload()
print("title: %s, id: %s" % (file1["title"], file1["id"]))
