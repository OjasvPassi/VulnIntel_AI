# backend/app/health.py
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            payload = {"status": "ok", "service": "vulnintel-foundations"}
            self.wfile.write(json.dumps(payload).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()


if __name__ == "__main__":
    print("VulnIntel Foundations backend starting on :8000", flush=True)
    server = HTTPServer(("0.0.0.0", 8000), SimpleHandler)
    server.serve_forever()
