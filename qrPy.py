import qrcode
from PIL import Image, ImageDraw, ImageFont
import pandas as pd

# read in the medical device information from an Excel file
device_info = pd.read_excel('medical_devices.xlsx')

# set the dimensions of the tag
tag_width = 794  # 70mm at 90 DPI
tag_height = 454  # 40mm at 90 DPI

# open the logo image and resize it
logo_img = Image.open("logo.png")
logo_img = logo_img.resize((int(tag_width * 0.4), int(tag_height * 0.4)))

# loop through each row of the device information and create a tag for each
for i, row in device_info.iterrows():
    # create a dictionary of the device properties for this row
    device_properties = {col: row[col] for col in device_info.columns}
    
    # create a new image for the tag with a white background
    base_img = Image.new('RGB', (tag_width, tag_height), color=(255, 255, 255))

    # generate the QR code image with device properties
    qr_data = ''
    for key, value in device_properties.items():
        qr_data += f"{key}: {value}\n"
    qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=6, border=5)
    qr.add_data(qr_data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # create an image draw object to add text to the base image
    draw = ImageDraw.Draw(base_img)

    # define the font and font size
    font = ImageFont.truetype('arial.ttf', size=30)

    # add the logo to the tag
    logo_padding = int(tag_width * 0.02)
    base_img.paste(logo_img, (logo_padding, logo_padding))

    # loop through each device property and add it to the image
    y = logo_img.size[1] + logo_padding * 2
    for key, value in device_properties.items():
        draw.text((logo_padding*3, y), f"{key}: {value}", font=font, fill=(0, 0, 0))
        y += 35

    # add the QR code to the image
    qr_pos_x = int(tag_width * 0.6)
    qr_pos_y = int(tag_height * 0.5 - qr_img.size[1] / 2)
    base_img.paste(qr_img, (qr_pos_x, qr_pos_y))

    # save the tag with a unique name
    base_img.save(f"device_tag_{i}.png")
