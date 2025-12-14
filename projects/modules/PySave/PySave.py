# ----------------------------
# PYSave by Tobble
# © 2025 - do not redistribute
# ----------------------------

# VERSION: BETA (things will change)

# Should the data be encrypted?
# If you already have data it will change to encryption but not back!
# Its also not millitary grade or anything, so dont store super sensitive data.

ENCRYPTED = True

save_file_location = r""

# use a file path here, leave blank for same folder. make sure you end in a double slash '\\' e.g 'C:/users/guy/desktop//'
# make sure the 'r' is present before the string.
# Changing the file path will not copy the data over!

print_status_codes = True

# should status codes print?

#--------------------------------------------------------------

from time import sleep as s
import os

__all__ = ["writeData", "readData", "delData"]

_filePath = "storage.pysave" if save_file_location == "" else f"{save_file_location}storage.pysave"

def _Createfile():
    
    """Attempt to create the storage file. If it already exists, do nothing."""
    
    try:
        
        open(_filePath, "x")
        print("Couldn't find storage file... creating file...")
        
    except FileExistsError:
        
        pass

cip = lambda text: ''.join(
    map(
        lambda char: (
            lambda ascii_val: chr(33 + ((ascii_val - 33 + 47) % 94)) if 33 <= ascii_val <= 126 else chr(ascii_val)
        )(
            (lambda ascii_code: (ascii_code - 65 + 13) % 26 + 65 if 65 <= ascii_code <= 90 else
                                (ascii_code - 97 + 13) % 26 + 97 if 97 <= ascii_code <= 122 else ascii_code)(
                (lambda ascii_code_inner: (ascii_code_inner - 65 + 13) % 26 + 65 if 65 <= ascii_code_inner <= 90 else
                                          (ascii_code_inner - 97 + 13) % 26 + 97 if 97 <= ascii_code_inner <= 122 else ascii_code_inner
                )(ord(char))
            )
        )
    , text)
)


def writeData(varName, data):
    """Write data to the save file (encrypted if enabled)."""

    if ENCRYPTED:
        data = cip(data)

    try:
        with open(_filePath, "r") as storage:
            storageContent = [line.rstrip("\n") for line in storage.readlines()]
    except FileNotFoundError:
        storageContent = []

    if varName in storageContent:
        index = storageContent.index(varName)
        if index + 1 < len(storageContent):
            storageContent[index + 1] = data
        else:
            storageContent.append(data)
    else:
        storageContent.append(varName)
        storageContent.append(data)

    with open(_filePath, "w") as storage:
        for line in storageContent:
            storage.write(line + "\n")


def readData(varName):
    """Read data from the save file (decrypt if enabled)."""

    try:
        with open(_filePath, "r") as storage:
            storageContent = [line.rstrip("\n") for line in storage.readlines()]
    except FileNotFoundError:
        if print_status_codes:
            print("Storage file not found.")
        return None

    if varName not in storageContent:
        if print_status_codes:
            print(f"{varName} not found in save file.")
        return None

    index = storageContent.index(varName) + 1
    data = storageContent[index]

    if ENCRYPTED:
        data = cip(data)

    return data


def delData(varName):
    """Delete the specified variable from storage. CANNOT BE UNDONE."""

    try:
        with open(_filePath, "r") as storage:
            storageContent = [line.rstrip("\n") for line in storage.readlines()]
    except FileNotFoundError:
        if print_status_codes:
            print("Storage file not found.")
        return

    if varName in storageContent:
        index = storageContent.index(varName)
        storageContent.pop(index)
        if index < len(storageContent):
            storageContent.pop(index)

        with open(_filePath, "w") as storage:
            for line in storageContent:
                storage.write(line + "\n")
                
        if print_status_codes:
            print(f"Deleted '{varName}' from storage.")
    else:
        if print_status_codes:
            print(f"'{varName}' not found in storage.")


_Createfile()

writeData("test", "1234")
print(readData("test"))
