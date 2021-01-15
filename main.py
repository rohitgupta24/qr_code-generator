import qrcode

qr = qrcode.QRCode()

qr.add_data("https://www.wikipedia.com")
qr.make(fit = True)

img = qr.make_image(fill_color = "orange", back_color='black')
img.save("qr.png")