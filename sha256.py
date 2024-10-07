#  Paula Farebrother
#  Created on 21st July 2024
#  Last updated Oct 2024

# ________________________________________________________________
#                       Hashing using SHA256
# ________________________________________________________________

from hashlib import sha256

def concatenate_string(filename):
    """ Accepts a csv filename to open and read each line.
        Concatenates all the values into a single string and returns.
    """
    with open(filename) as file:
        lines = file.readlines()
        data = lines[0].strip().split(",")
        string = "".join(data)
        return string

def calculate_sha256_checksum(string):
    """ Takes a string and calculates a hash using the SHA256 algorithm.
        Returns a hexadecimal result.
    """
    encoded = sha256(string.encode())
    result = encoded.hexdigest()
    return result

def compare_checksum(string, checksum):
    """ Takes a string and calculates the SHA256 hash.
        Compares the calculated hash to the hash sent with the document.
        Confirms whether they match (revealing document alteration).
        Returns a message advising whether a match was found.
    """
    str_checksum = calculate_sha256_checksum(string)
    if str_checksum == checksum:
        print("These are a match, safe to proceed.")
    else:
        print("These are not a match, do not proceed.")
