import pyqrcode
import png

QRstr = "HTTP URL"
url = pyqrcode.create(QRstr)
url.png(r'C:\Users\marek\Desktop\PythonProjects\qr.png', scale=8)
