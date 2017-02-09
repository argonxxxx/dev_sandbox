# encode utf_8

import sys
import csv
import re

# --------------------------------------
# Function
# --------------------------------------
def replace_crlf_esc(text):
    text = re.sub(r'\\',r"\\\\",text)
    text = re.sub(r'\n',r"\\n",text)
    text = re.sub(r'\r',r"\\r",text)
    return text

# --------------------------------------
# Main
# --------------------------------------
reader = csv.reader(sys.stdin)
header = next(reader)
column_len = len(header)

for line in reader:
    print("{")

    for i in range(0,column_len):
        r = replace_crlf_esc(line[i])
        h = replace_crlf_esc(header[i])
        if str(i) != "0":
            print(",")
        print("    \""+h+"\" : \""+r+"\"", end="")

    print("\n}")

