import http.server
import socketserver
import json
import os
import uuid

PORT = 3001
CRED_FILE = 'credentials.json'
BOOK_FILE = 'bookings.json'

def load_credentials():
    if not os.path.exists(CRED_FILE):
        default_creds = {
            "reception": [
                {"email": "admin@healthtrust.com", "password": "password123"}
            ],
            "patient": [
                {"email": "patient@healthtrust.com", "password": "password123"}
            ]
        }
        save_credentials(default_creds)
        return default_creds
    with open(CRED_FILE, 'r') as f:
        return json.load(f)

def save_credentials(creds):
    with open(CRED_FILE, 'w') as f:
        json.dump(creds, f, indent=4)

def load_bookings():
    if not os.path.exists(BOOK_FILE):
        return []
    with open(BOOK_FILE, 'r') as f:
        return json.load(f)

def save_bookings(bookings):
    with open(BOOK_FILE, 'w') as f:
        json.dump(bookings, f, indent=4)

class AuthHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/code.html'
        if self.path == '/api/bookings':
            import os, json
            if os.path.exists('bookings.json'):
                with open('bookings.json', 'r') as bf:
                    try: self._send_response(200, {"success": True, "bookings": json.load(bf)})
                    except: self._send_response(200, {"success": True, "bookings": []})
            else: self._send_response(200, {"success": True, "bookings": []})
            return
        return super().do_GET()

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        try:
            data = json.loads(post_data.decode('utf-8'))
            email = data.get('email')
            password = data.get('password')
            user_type = data.get('type')
            
            creds = load_credentials()
            
            if self.path == '/api/login':
                if user_type == 'reception':
                    reception_accounts = creds.get("reception", [])
                    authenticated = any(acc["email"] == email and acc["password"] == password for acc in reception_accounts)
                    
                    if authenticated:
                        self._send_response(200, {"success": True, "message": "Reception login successful!", "token": "mock_token_789"})
                    else:
                        self._send_response(401, {"success": False, "message": "Invalid credentials for Reception."})
                else:
                    patient_accounts = creds.get("patient", [])
                    authenticated = any(acc["email"] == email and acc["password"] == password for acc in patient_accounts)
                    
                    if authenticated:
                        self._send_response(200, {"success": True, "message": "Patient login successful!", "token": "mock_token_123"})
                    else:
                        self._send_response(401, {"success": False, "message": "Invalid credentials for Patient."})
            
            elif self.path == '/api/register':
                if user_type == 'reception':
                    reception_accounts = creds.get("reception", [])
                    if any(acc["email"] == email for acc in reception_accounts):
                        self._send_response(400, {"success": False, "message": "This Reception ID is already registered."})
                    else:
                        reception_accounts.append({"email": email, "password": password})
                        creds["reception"] = reception_accounts
                        save_credentials(creds)
                        self._send_response(200, {"success": True, "message": "Reception account created successfully!"})
                else:
                    patient_accounts = creds.get("patient", [])
                    if any(acc["email"] == email for acc in patient_accounts):
                        self._send_response(400, {"success": False, "message": "This Patient email is already registered."})
                    else:
                        patient_accounts.append({"email": email, "password": password})
                        creds["patient"] = patient_accounts
                        save_credentials(creds)
                        self._send_response(200, {"success": True, "message": "Patient account created successfully!"})
                    
            elif self.path == '/api/book':
                bookings = load_bookings()
                
                # Determine fee based on department
                dept = data.get("department", "General Medicine")
                fee = 500
                if dept in ["Cardiology", "Neurology", "Oncology", "Orthopedics", "General Surgery"]:
                    fee = 1000
                
                new_booking = {
                    "id": str(uuid.uuid4())[:8],
                    "name": data.get("name"),
                    "phone": data.get("phone"),
                    "email": email,
                    "date": data.get("date"),
                    "time": data.get("time"),
                    "department": dept,
                    "symptoms": data.get("symptoms"),
                    "status": "Pending",
                    "fee_inr": fee
                }
                bookings.append(new_booking)
                save_bookings(bookings)
                
                self._send_response(200, {"success": True, "message": "Your appointment has been successfully requested!"})
            
            elif self.path == '/api/bookings/update':
                # Update status of a booking
                booking_id = data.get("id")
                new_status = data.get("status")
                
                bookings = load_bookings()
                updated = False
                for b in bookings:
                    if b.get("id") == booking_id:
                        b["status"] = new_status
                        updated = True
                        break
                
                if updated:
                    save_bookings(bookings)
                    self._send_response(200, {"success": True, "message": f"Booking {new_status}!"})
                else:
                    self._send_response(404, {"success": False, "message": "Booking not found."})
                
            else:
                self._send_response(404, {"success": False, "message": "Endpoint not found."})
                
        except Exception as e:
            self._send_response(400, {"success": False, "message": f"Invalid request format: {str(e)}"})
            
    def _send_response(self, status_code, payload):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode('utf-8'))

os.chdir(os.path.dirname(os.path.abspath(__file__)))

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), AuthHandler) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
