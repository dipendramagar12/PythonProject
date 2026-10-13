import qrcode

print("===== QR Code Generator =====")

name = input("Enter your name or a short message: ")

img = qrcode.make(name)
img.save("my_qrcode.png")

print("Personal QR code generated successfully!")

website = input("Enter your favorite website URL: ")

img = qrcode.make(website)
img.save("website_qrcode.png")

print("Website QR code generated successfully!")
print("Thank you for using the QR Code Generator!")