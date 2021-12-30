import qrcode

#image=qrcode.make("Insert your data here")
#image.save("qr.jpg")

qr=qrcode.QRCode(
    version=1,
    box_size=15,
    border=5
)
data="Enter your data here"
qr.add_data(data)
qr.make(fit=True)
image=qr.make_image(fill='black',back_color='white')
image.save("myQR.jpg")