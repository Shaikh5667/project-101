import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
         # enumerate local files recursively
        for root, dirs, files in os.walk(file_from):

            for filename in files:
                # construct the full local path
                local_path = os.path.join(root, filename)

                # construct the full Dropbox path
                relative_path = os.path.relpath(local_path, file_from)
                dropBox_path = os.path.join(file_to, relative_path)
                # upload the file
                with open(local_path, 'rb') as f:
                    dbx.file_upload(f.read(), dropbox_path, mode=writeMode('overwrite'))

def main():
    access_token = 'sl.BE9ARNLnsDqibFYb1_Y_EN4XgPpD7W45r8blkcHvF7uV8kdp592XXNvjtgCnj3f6by67BiwasSyAI6HO-CrVqPxddNStYK5fvTgYFPSNIx_Kobe_1wLWEtapRIL_5uOGh0Mkswg'
    TransferData = TransferData(access_token)

    file_from = str(input("Enter the folder path to transfer : "))
    file_to = input("enter the full path to upload to dropbox:-") # This is the full path to upload the file to

    # API v2
    TransferData.upload_file(file_from,file_to)
    print("file has been moved !!!")

    main()