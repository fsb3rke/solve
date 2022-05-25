import cv2
qr_detector = cv2.QRCodeDetector()
val, points, straigh_qrcode = qr_detector.detectAndDecode(cv2.imread("qrcode.png"))
print(val, points, straigh_qrcode, sep="\n")
with open("val.txt", "w") as f:
    f.write(str(val))