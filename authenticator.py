from qr_reader import QRReader


def main():
    qr_reader = QRReader()
    qr_reader.read()
    print("%s" % qr_reader.codes())


if __name__ == '__main__':
    main()
