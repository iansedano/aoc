import os
import sys

import dropbox

# Access token from your Dropbox app
DROPBOX_ACCESS_TOKEN = os.environ["DROPBOX_TOKEN"]

dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)
print(dbx)
result = dbx.files_list_folder(path="")
print(result)


def process_folder_entries(current_state, entries):
    for entry in entries:
        if isinstance(entry, dropbox.files.FileMetadata):
            current_state[entry.path_lower] = entry
        elif isinstance(entry, dropbox.files.DeletedMetadata):
            current_state.pop(
                entry.path_lower, None
            )  # ignore KeyError if missing
    return current_state


files = process_folder_entries({}, result.entries)
print(files)

while result.has_more:
    print("Collecting additional files...")
    result = dbx.files_list_folder_continue(result.cursor)
    files = process_folder_entries(files, result.entries)
    print(files)

# DROPBOX_FOLDER = "/AdventOfCodeInputs"  # Folder in Dropbox
# LOCAL_FOLDER = "./inputs"  # Local folder to store downloaded files

# def download_files_from_dropbox():
#     # Initialize Dropbox client
#     dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)

#     try:
#         # List files in the Dropbox folder
#         files = dbx.files_list_folder(DROPBOX_FOLDER).entries
#         if not files:
#             print("No files found in the Dropbox folder.")
#             return

#         # Ensure local folder exists
#         os.makedirs(LOCAL_FOLDER, exist_ok=True)

#         # Download each file
#         for file in files:
#             if isinstance(file, dropbox.files.FileMetadata):
#                 local_path = os.path.join(LOCAL_FOLDER, file.name)
#                 with open(local_path, "wb") as f:
#                     metadata, response = dbx.files_download(file.path_lower)
#                     f.write(response.content)
#                 print(f"Downloaded {file.name} to {local_path}")

#     except dropbox.exceptions.AuthError as e:
#         print("Authentication error: Check your access token.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# def use_files():
#     # Iterate over the local files and process them
#     for filename in os.listdir(LOCAL_FOLDER):
#         filepath = os.path.join(LOCAL_FOLDER, filename)
#         with open(filepath, "r") as f:
#             content = f.read()
#             print(f"Processing file {filename} with content: {content}")
#             # Add your logic for using the input/solution files here

# if __name__ == "__main__":
#     download_files_from_dropbox()
#     use_files()


# App key
# v6v0qxqvun8bdsf
# App secret
# dw97szgzxu487na
