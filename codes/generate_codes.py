import random
import sys
import qrcode

def main():

    generate_codes()

    with open('codes.txt', 'r') as f:
        codes = f.readlines()

    for code in codes:
        generate_qr_code(code.strip())

def generate_codes():
    if len(sys.argv) != 2:
        sys.exit('Usage: python generate_codes.py <number of codes to generate>')

    codes_to_generate = int(sys.argv[1])
    with open('codes.txt', 'w') as f:
        for i in range(codes_to_generate):
            rnd = str(random.randint(10000, 99999))
            f.write(rnd + '\n')

def generate_qr_code(code):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    qr.add_data(code)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"qrcodes/{code}.png")

if __name__ == '__main__':
    main()