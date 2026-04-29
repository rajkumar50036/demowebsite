import sys
import os
import json

with open('server.py', 'r') as f:
    content = f.read()

if 'import uuid' not in content:
    content = content.replace('import os', 'import os\nimport uuid')
    
get_bookings = '''    def do_GET(self):
        # Serve code.html when root is accessed
        if self.path == '/':
            self.path = '/code.html'
            
        if self.path == '/api/bookings':
            import json, os
            book_file = 'bookings.json'
            bookings = []
            if os.path.exists(book_file):
                with open(book_file, 'r') as bf:
                    try:
                        bookings = json.load(bf)
                    except:
                        pass
            self._send_response(200, {"success": True, "bookings": bookings})
            return
            
        return super().do_GET()'''

content = content.replace('''    def do_GET(self):
        # Serve code.html when root is accessed
        if self.path == '/':
            self.path = '/code.html'
        return super().do_GET()''', get_bookings)

new_booking = '''                # Append the new booking lead
                new_booking = {
                    "id": str(uuid.uuid4()),
                    "name": data.get("name"),
                    "phone": data.get("phone"),
                    "email": email,
                    "date": data.get("date"),
                    "time": data.get("time"),
                    "department": data.get("department"),
                    "symptoms": data.get("symptoms"),
                    "status": "pending",
                    "fee": 500
                }'''

content = content.replace('''                # Append the new booking lead
                new_booking = {
                    "name": data.get("name"),
                    "phone": data.get("phone"),
                    "email": email,
                    "date": data.get("date"),
                    "time": data.get("time"),
                    "department": data.get("department"),
                    "symptoms": data.get("symptoms")
                }''', new_booking)

update_status = '''                self._send_response(200, {"success": True, "message": "Your appointment has been successfully requested!"})
                
            elif self.path == '/api/booking/status':
                booking_id = data.get("id")
                new_status = data.get("status")
                
                if not booking_id or not new_status:
                    self._send_response(400, {"success": False, "message": "Missing booking id or status."})
                    return
                    
                book_file = 'bookings.json'
                bookings = []
                if os.path.exists(book_file):
                    with open(book_file, 'r') as bf:
                        try:
                            bookings = json.load(bf)
                        except:
                            pass
                            
                updated = False
                for b in bookings:
                    if b.get("id") == booking_id:
                        b["status"] = new_status
                        updated = True
                        break
                        
                if updated:
                    with open(book_file, 'w') as bf:
                        json.dump(bookings, bf, indent=4)
                    self._send_response(200, {"success": True, "message": f"Booking {new_status} successfully!"})
                else:
                    self._send_response(404, {"success": False, "message": "Booking not found."})'''

content = content.replace('''                self._send_response(200, {"success": True, "message": "Your appointment has been successfully requested!"})''', update_status)

with open('server.py', 'w') as f:
    f.write(content)
print("Patched successfully")
