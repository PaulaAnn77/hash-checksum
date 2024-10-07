#  Paula Farebrother
#  Created on 21st July 2024
#  Last updated Oct 2024

# ___________________________________________________________________________

#                 Implementation Notes for sha256.py

# ___________________________________________________________________________

from sha256 import *
# ^^^ imports all from sha256 module

string = concatenate_string("filename.csv")
# ^^^ creates a checksum from received csv file.
# Ensure file is stored in same directory, or provide path.

checksum = "5c14e4599f1d2a39abe6b487ac2a5415c894c6882f5fdd4a40e02c7dd628829a"
# ^^^ Provide the checksum sent with the file

compare_checksum(string, checksum)
# ^^^ Pass the created checksum, then the provided checksum to the function.
# This confirms that they match to ensure documents are identical.

