from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>TCP/IP Protocol Suite</title>
</head>
<body>
    <h1>List of Protocols in TCP/IP Protocol Suite</h1>
    <ul>
        <li>Application Layer: HTTP, FTP, SMTP, DNS, Telnet</li>
        <li>Transport Layer: TCP, UDP</li>
        <li>Internet Layer: IP, ICMP, IGMP, ARP</li>
        <li>Network Access Layer: Ethernet, Wi-Fi, PPP</li>
    </ul>
</body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()