#-------------------------------------#
# lime_coBa (c) 2006-2020, DemCreator #
# Ver: 0.0.1                          #
# License: pohui                      #
#-------------------------------------#

#imports
from PIL import Image, ImageDraw, ImageFont

#parameters
img_size = (1000, 1000)
top_text_size = 72
bottom_text_size = 28

#open & resize picture
dem_picture = Image.open("photo.jpg")
res_dem_picture = dem_picture.resize((img_size[0] - 110, img_size[1] - 260))
pix_res_dem_picture = res_dem_picture.load()

#text
top_string = "Срать"
bottom_string = "ладно."

#create image
img = Image.new("RGBA", img_size, "black")
idraw = ImageDraw.Draw(img)

#load fonts
top_text = ImageFont.truetype("times.ttf", size = top_text_size)
bottom_text = ImageFont.truetype("arial.ttf", size = bottom_text_size)

#draw pictuer to demotivator
idraw.rectangle((49, 49, 950, 800), outline = "white", width = 3)

for x in range(0, img_size[0] - 110):
    for y in range(0, img_size[1] - 260):
        idraw.point((x + 55, y + 55), fill = pix_res_dem_picture[x, y])

#draw text
idraw.text((img_size[0] / 2 - (top_text_size * len(top_string)) / 4, 825), top_string, font = top_text)
idraw.text((img_size[0] / 2 - (bottom_text_size * len(bottom_string)) / 4, 920), bottom_string, font = bottom_text)

#showing image
img.show()