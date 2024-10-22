import argparse

import qrcode


class QRGenerator:
    error_correction = qrcode.constants.ERROR_CORRECT_L

    def __init__(self, version: int, box_size: int, border: int):
        self.version = version
        self.box_size = box_size
        self.border = border

    def _create_qr_object_(self):
        return qrcode.main.QRCode(
            version=self.version,
            error_correction=self.error_correction,
            box_size=self.box_size,
            border=self.border,
        )

    @staticmethod
    def _add_data_(qr, data):
        qr.add_data(data)
        qr.make(fit=True)

    def _create_qr(self, data):
        qr = self._create_qr_object_()
        self._add_data_(qr, data)
        return qr

    def _create_img_(self, data, fill, back_color):
        qr = self._create_qr(data)
        img = qr.make_image(fill=fill, back_color=back_color)
        return img

    def save(self, data, fill="black", back_color="white", path="qrcode.png"):
        img = self._create_img_(data, fill, back_color)
        img.save(path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate QR code")
    parser.add_argument("-d", "--data", type=str, help="version of QRCode", required=True)
    parser.add_argument("-v", "--version", type=int, help="version of QRCode", default=2)
    parser.add_argument("-s", "--size", type=int, help="Size of QR code", default=10)
    parser.add_argument("-sb", "--border-size", type=int, help="Thickness of the border", default=2)
    parser.add_argument("-o", "--output", type=str, help="name of output file", default="qrcode.png")
    args = parser.parse_args()

    qr = QRGenerator(version=args.version, box_size=args.size, border=args.border_size)
    qr.save(data=args.data, path=args.output)
