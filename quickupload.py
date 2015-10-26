from http.server import HTTPServer, CGIHTTPRequestHandler
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", type=int, default="15000", 
                    help="The port to run the server on.")
arguments = parser.parse_args()

httpd = HTTPServer(('', arguments.port), CGIHTTPRequestHandler)
httpd.serve_forever()
