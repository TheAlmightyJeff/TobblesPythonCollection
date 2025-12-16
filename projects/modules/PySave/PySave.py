# ----------------------------
# PYSave by Tobble
# © 2025 - do not redistribute
# ----------------------------

# VERSION: BETA (things will change)

#-----------------------------------
#Edit these, if you want
#-----------------------------------
5
# Should the data be encrypted?
# If you already have data it will change to encryption but not back!
# Its also not millitary grade or anything, so don't store super sensitive data.

ENCRYPTED = True

# use a file path here, leave blank for same folder. make sure you end in a double slash '\\' e.g 'C:/users/tobble/desktop//'
# make sure the 'r' is present before the string. It should be >>> save_file_location = r"" <<<
# Changing the file path will not copy the data over!

save_file_location = r""

# should stuff be printed?

print_status_codes = True

#--------------------------------------------------------------

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



cip = lambda t: ''.join(map(
    lambda c: (
        lambda x: (
            lambda y: (
                lambda z: chr(33 + ((z - 33 + 47) % 94)) if 33 <= z <= 126 else chr(z)
            )(
                (lambda a: (a - 65 + 13) % 26 + 65 if 65 <= a <= 90 else
                           (a - 97 + 13) % 26 + 97 if 97 <= a <= 122 else a
                )(
                    (lambda b: (b - 65 + 13) % 26 + 65 if 65 <= b <= 90 else
                               (b - 97 + 13) % 26 + 97 if 97 <= b <= 122 else b
                    )(ord(x))
                )
            )
        )(c)
    )(c)
, t))


def _enc(text):
    return cip(text) if ENCRYPTED else text


def _dec(text):
    return cip(text) if ENCRYPTED else text


def writeData(varName, data):
    """Write encrypted variable name and data to storage."""

    key = _enc(varName)
    value = _enc(data)

    try:
        with open(_filePath, "r") as storage:
            storageContent = [line.rstrip("\n") for line in storage.readlines()]
    except FileNotFoundError:
        storageContent = []

    if key in storageContent:
        index = storageContent.index(key)
        if index + 1 < len(storageContent):
            storageContent[index + 1] = value
        else:
            storageContent.append(value)
    else:
        storageContent.append(key)
        storageContent.append(value)

    with open(_filePath, "w") as storage:
        storage.write("\n".join(storageContent) + "\n")


def readData(varName):
    """Read data using encrypted variable name."""

    key = _enc(varName)

    try:
        with open(_filePath, "r") as storage:
            storageContent = [line.rstrip("\n") for line in storage.readlines()]
    except FileNotFoundError:
        if print_status_codes:
            print("Storage file not found.")
        return None

    if key not in storageContent:
        if print_status_codes:
            print(f"{varName} not found in save file.")
        return None

    index = storageContent.index(key) + 1
    return _dec(storageContent[index])


def delData(varName):
    
    """Delete variable name and value, even if encrypted. CANNOT BE UNDONE."""

    key = _enc(varName)

    try:
        with open(_filePath, "r") as storage:
            storageContent = [line.rstrip("\n") for line in storage.readlines()]
    except FileNotFoundError:
        if print_status_codes:
            print("Storage file not found.")
        return

    if key in storageContent:
        index = storageContent.index(key)
        storageContent.pop(index)
        if index < len(storageContent):
            storageContent.pop(index)

        with open(_filePath, "w") as storage:
            storage.write("\n".join(storageContent) + "\n")

        if print_status_codes:
            print(f"Deleted '{varName}' from storage.")
    else:
        if print_status_codes:
            print(f"'{varName}' not found in storage.")


_Createfile()
writeData("hello", "1234567890")
print(readData("hello"))
