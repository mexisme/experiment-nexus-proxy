# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer
import time
import pprint
import json

# hostName = "localhost"
hostName = "0.0.0.0"
serverPort = 8090

class MyServer(BaseHTTPRequestHandler):
    def get_body(self):
        if not self.headers['Content-Length']:
            print("No body sent.")
            return None

        content_length = int(self.headers['Content-Length'])
        print(f"Reading contents of {content_length} bytes...")
        return self.rfile.read(content_length).decode("utf-8")

    def do_GET(self):
        print("Got a connection:")
        pprint.pp(self)
        body = self.get_body()
        pprint.pp(body)
        try:
            pprint.pp(json.loads(body))
        except Exception as err:
            self.log_message(err)

        self.log_request()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # if not self.wfile.closed:
        #     self.wfile.write(bytes("<html><head><title>HTTP://pythonbasics.org</title></head>", "utf-8"))
        #     self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        #     self.wfile.write(bytes("<body>", "utf-8"))
        #     self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        #     self.wfile.write(bytes("</body></html>", "utf-8"))

    def do_POST(self):
        self.do_GET()

def go():
    webServer = ThreadingHTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()

if __name__ == "__main__":
    go()
