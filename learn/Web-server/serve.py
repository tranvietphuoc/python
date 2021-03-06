import http.server
import urllib3


class HTTPServer_RequestHandler(http.server.BaseHTTPRequestHandler):
    # GET method
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # then response a html file
        self.wfile.write(b"<!DOCTYPE html>")
        self.wfile.write(b"<html lang='en'>")
        self.wfile.write(b"<head>")
        self.wfile.write(b"<title>Hello, my test page</title>")
        self.wfile.write(b"</head>")
        self.wfile.write(b"<body>")
        self.wfile.write(b"Hello, I'm tranvietphuoc")
        self.wfile.write(b"</body>")
        self.wfile.write(b"</html>")


port = 8080  # http's port
server_address = ('localhost', port)
httpd = http.server.HTTPServer(server_address, HTTPServer_RequestHandler)
print('server run at http://localhost:8080')
httpd.serve_forever()
# run that Python file and go to the address 0.0.0.0:8080 to see the result