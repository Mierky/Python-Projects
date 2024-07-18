import qrcode
import re

def extract_domain(url):
    pattern = re.compile(
        r'^(?:https?:\/\/)?'  # http:// or https:// (optional)
        r'(?:www\.)?'         # www. (optional)
        r'([^\/\n\.]+)'       # Capture the domain name excluding dot
        r'(?:\.com)?'         # Optionally match .com
    )
    match = re.search(pattern, url)

    return match.group(1)

def generate_code(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "black",back = "white")

    link_name = extract_domain(text)
    img.save ("qrimg_"+link_name+".png")

if __name__=='__main__':
    text = input("Enter a link: ")
    generate_code(text) if re.match('https://',text) else print("Error: Not a link - Please enter a link")
