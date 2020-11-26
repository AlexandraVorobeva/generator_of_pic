from PIL import Image
from PIL import ImageFont
from PIL import ImageColor
from PIL import ImageDraw

def main():
    image_mode = "RGB"
    image_size = (640, 480)
    imaage_color = "#ffe6f7"
    font_size1 = 58
    font_color = "#000000"
    font_size2 = 34
    font_size3 = 28


    img = Image.new(mode=image_mode, size=image_size, color=imaage_color)
    font1 = ImageFont.truetype("19278.otf", size=font_size1)
    fill1 = ImageColor.getrgb(color=font_color)
    font2 = ImageFont.truetype("19278.otf", size=font_size2)
    fill2 = ImageColor.getrgb(color=font_color)
    font3 = ImageFont.truetype("19278.otf", size=font_size3)
    fill3 = ImageColor.getrgb(color=font_color)


    draw = ImageDraw.Draw(im=img, mode=img.mode)

    text1 = "Aleksandra Vorobeva"
    text_width1, text_height1 = font1.getsize(text1)
    text2 = "traveler, programmer"
    text_width2, text_height2 = font2.getsize(text2)
    text3 = "inst: sparkling_acidity"
    text_width3, text_height3 = font3.getsize(text3)

    x = 1.0 * image_size[0] / 2 - text_width1 / 2
    y = 0.9 * image_size[1] / 2 - text_height1 / 2
    draw.text(xy=(x, y), text=text1, fill=fill1, font=font1, align="center")
    x = 1.0 * image_size[0] / 2 - text_width2 / 2
    y = 1.2 * image_size[1] / 2 - text_height2 / 2
    draw.text(xy=(x, y), text=text2, fill=fill2, font=font2, align="center")
    x = 1.4 * image_size[0] / 2 - text_width3 / 2
    y = 1.4 * image_size[1] / 2 - text_height3 / 2
    draw.text(xy=(x, y), text=text3, fill=fill3, font=font3)





    img.save("result.png")

if __name__ == '__main__':
    main()