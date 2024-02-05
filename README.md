# QR Code Generator
This Python script (`Create QR Code.py`) generates a QR code for a given URL using the `pyqrcode` library.

## Usage
1. Ensure you have Python installed on your system.
2. Install the `pyqrcode` library if you haven't already:
   pip install pyqrcode
   
3. Run the script by executing the Python file `Create QR Code.py`.
4. The QR code corresponding to the URL provided in the script will be generated and saved as `Qr.png` in the same directory.

## Script Description
- The script utilizes the `pyqrcode` library to generate QR codes.
- It takes a URL (`https://www.youtube.com/@KarthiKeshRobotics` in this case) and creates a QR code representation of it.
- The QR code is saved as `Qr.png` with a scale of 10.

## Dependencies
- Python 3.x
- `pyqrcode` library

## Notes
- Make sure you have proper permissions to access and write files in the directory where you run the script.
- You can modify the `url` variable in the script to generate QR codes for different URLs.

Feel free to reach out if you have any questions or suggestions!
