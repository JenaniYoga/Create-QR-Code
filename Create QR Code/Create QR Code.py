import pyqrcode

url='https://www.youtube.com/@KarthiKeshRobotics'
k=pyqrcode.create(url)
k.png('Qr.png',scale=10)



