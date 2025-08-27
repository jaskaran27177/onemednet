from flask import Flask, jsonify
import time
import uuid
from datetime import datetime, timezone
import pytz

app = Flask(__name__)


@app.route('/')
def hello_world():
    """
    This is a Simple Get request for Steven. 
    """
    unique_id = uuid.uuid4()

    current_utc_time = datetime.now(timezone.utc)
    
    # Define the Vancouver timezone.
    vancouver_timezone = pytz.timezone('America/Vancouver')
    
    # Convert the UTC time to Vancouver time.
    current_vancouver_time = current_utc_time.astimezone(vancouver_timezone)

    output=jsonify({
        "id": str(unique_id), 
        "timestamp": current_utc_time.strftime("%a, %d %b %Y %H:%M:%S GMT"),
        "vancouver_time": current_vancouver_time.strftime("%a, %d %b %Y %H:%M:%S %Z")
        })
    return output

    

if __name__ == '__main__':

    import os
    port = int(os.environ.get('PORT', 8080))  
    app.run(host='0.0.0.0', port=port)