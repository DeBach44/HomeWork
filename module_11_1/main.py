from PIL import Image,ImageFilter,ImageDraw,ImageFont
from urllib.request import urlopen

def make_fon(): #Создание фона
    url = ('https://img.desktopwallpapers.ru/newyear/pics/wide/1920x1080/a97d95afbba363234de229e808e46817.jpg')
    with Image.open(urlopen(url)) as img_fon:
        w, h = img_fon.size
        img_fon = img_fon.resize((w//2,h//2))     #Изменение размера
        img_fon = img_fon.transpose(Image.FLIP_LEFT_RIGHT)    #Отражение
        img_fon = img_fon.filter(ImageFilter.BLUR)    #Наложение фильтра
        img_fon = img_fon.filter(ImageFilter.GaussianBlur(5))
        img_fon = img_fon.crop((200, 0, 820, 540))
        img_fon.show()
        return img_fon

def paste_img(): #Соединение изображения с фоном
    img1 = make_fon()
    with Image.open('zm.jpg') as img2:
        mask_img = Image.new("L", img2.size, 0)     #Создание маски
        draw = ImageDraw.Draw(mask_img)
        draw.ellipse((20, 20, 380, 380), fill=255)
        mask_img_blur = mask_img.filter(ImageFilter.GaussianBlur(10))
        w = img1.width//2-img2.width//2 #Вставка по центру
        img1.paste(img2, (w,120), mask_img_blur)
        img1.show()
        return img1

def make_text_in_img(): #Добавление текста
    img = paste_img()
    font = ImageFont.truetype("Bohema_Pink.ttf", size=52)
    text = 'С Новым 2025\nГодом'
    draw = ImageDraw.Draw(img)
    draw.text((150,60),text,font=font, align='center')
    img.show()
    return img

if __name__ == '__main__':
    img = make_text_in_img()
    img.save('NewYear.jpg')