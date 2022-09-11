import cv2
from pyzbar.pyzbar import decode


class QRReader:

    def __init__(self):
        self.__codes = []

    def codes(self):
        return self.__codes

    def __read_qr_code(self, frame):
        barcodes = decode(frame)
        for barcode in barcodes:
            x, y, w, h = barcode.rect
            barcode_info = barcode.data.decode('utf-8')
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if barcode_info not in self.__codes:
                self.__codes.append(barcode_info)
                return True
            return False

    def read(self):
        camera = cv2.VideoCapture(0)
        ret, frame = camera.read()
        while ret:
            ret, frame = camera.read()

            cv2.imshow('Barcode/QR code reader', frame)
            have_code = self.__read_qr_code(frame)
            if have_code:
                break
            if cv2.waitKey(1) & 0xFF == 27:
                break
        camera.release()
        cv2.destroyAllWindows()
