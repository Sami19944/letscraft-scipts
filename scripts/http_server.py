from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import os
import logging
import configparser
 
# HTTPRequestHandler class
class RequestHandler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()

        message = ""
        message = message + '<h3>dev.py</h3>'
        message = message + '<form action="" method="post">'
        message = message + '   <input type="text" name="in_func" placeholder="func" />'
        message = message + '   <input type="submit" value="post" />'
        message = message + '</form>'

        self.wfile.write(message.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()

        message = ""
        message = message + 'func: '

        self.wfile.write(message.encode('utf-8'))

def run(dev):
	create_logger()
	config_file = "main.conf"
	config = configparser.ConfigParser()
	config.read(config_file)
	print('http_server run')
	path = os.getcwd()
	print("   config_file:" + config_file)
	print("   path:" + path)
	print("   config")
	host = config['http_server']['host']
	print("       host: " + host)
	port = int(config['http_server']['port'])
	print("       port: " + str(port))
 
	print('   starting server...')
	# Server settings
	# Choose port 8080, for port 80, which is normally used for a http server, you need root access
	server_address = (host, port)
	httpd = HTTPServer(server_address, RequestHandler)
	print('   running server...')
	httpd.serve_forever()

def create_logger():
	# Create a custom logger
	logger = logging.getLogger(__name__)

	# Create handlers
	c_handler = logging.StreamHandler()
	c_handler.setLevel(logging.DEBUG)
	f_handler = logging.FileHandler(__name__ + ".log")
	f_handler.setLevel(logging.DEBUG)

	# Create formatters and add it to handlers
	c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
	f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	c_handler.setFormatter(c_format)
	f_handler.setFormatter(f_format)

	# Add handlers to the logger
	logger.addHandler(c_handler)
	logger.addHandler(f_handler)