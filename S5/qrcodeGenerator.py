#pip install qrcode pillow
import qrcode

data="http://google.com"
qr=qrcode.QRCode(version=None)
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="white")
img.save("qrcode.png")
