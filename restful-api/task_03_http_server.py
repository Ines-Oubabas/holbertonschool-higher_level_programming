import http.server
import json

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Handling the /data endpoint to serve JSON data
        if self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = json.dumps({"name": "John", "age": 30, "city": "New York"})
            self.wfile.write(data.encode())
        # Handling the /status endpoint to check API status
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("OK".encode())
        # Default response for root endpoint
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode())
        # Handling undefined endpoints
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("404 Not Found".encode())

def run(server_class=http.server.HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
