import qrcode

img = qrcode.make("https://youtu.be/xvFZjo5PgG0?si=vqPdEXx149L5yY5A")
img.save("qr.png", "PNG")
