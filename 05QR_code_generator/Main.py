# https://pypi.org/project/qrcode/

import qrcode

data = input('Enter the text or URL: ').strip()
fileName = input('Enter the fileName: ').strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)

image = qr.make_image(fill_color = 'black', back_color = 'white')
image.save(fileName)

print(f'QR code Saved as {fileName}')