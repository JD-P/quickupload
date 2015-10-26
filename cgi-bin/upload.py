#/usr/bin/python3

import cgi
import os
import codecs
import cgitb
cgitb.enable()

def upload_file():
    """Upload a file received from user input to the server."""
    form = cgi.FieldStorage()
    uploaded_file = form["upload"]
    filename = sanitize_filename(uploaded_file.filename)
    file_contents = uploaded_file.file.read()
    with open("uploads/" + filename) as outfile:
        outfile.write(file_contents)
        outfile.flush()
    send_OK()

def sanitize_filename(filename):
    """Sanitize a filename, removing dangerous characters that could be used to 
    escape the uploads directory. Everything except [A-Z a-z 0-9 - _ .] are 
    stripped, along with the pattern '..' which in *nix systems represents going
    up a directory in the filepath.
    """
    filename = filename.replace("..", ".")
    for character in filename:
        if character not in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                             "abcdefghijklmnopqrstuvwxyz",
                             "0123456789",
                             "._-"):
            filename = filename.replace(character, "")
    return filename

def send_OK():
    """Send the OK success message back to the client after the file is done being
    written."""
    writer = codecs.getwriter('utf-8')(sys.stdout.buffer)
    #HTTP Headers
    writer.write("Content-Type: text/html; charset=utf-8" + '\r\n')
    writer.write("Content-Length: " + len("Upload successful!") + '\r\n')
    # Seperator between header and HTML
    writer.write('\r\n')
    # Text
    writer.write("Upload Sucessful!")

