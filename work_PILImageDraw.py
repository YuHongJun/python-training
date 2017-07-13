from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

# random  letters,num,chinese
def rndChar():
    # return chr(random.randint(65,90))
    # random Upper and lower case letters
    letterChr=chr(random.choice([x for x in range(65,123) if x not in [z for z in range(91,97)]]))
    #random num
    numChr=str(random.randint(0,9))
    # random chinese
    cnChr=random.choice('我是中文汉字')
    return random.choice((letterChr,numChr,cnChr))
# random color1
def rndColor():
    return (random.randint(64,255), random.randint(64,255),random.randint(64,255))

# random color2
def rndColor2():
    return (random.randint(32,127), random.randint(32,127), random.randint(32,127))

# 240 * 60
width = 60 * 4
height = 60
image = Image.new('RGB',(width,height),(255,255,255))
# create font
font = ImageFont.truetype('Arial.ttf',36)
# create draw
draw= ImageDraw.Draw(image)
# fill each pixel
for x in range(width):
    for y in range(height):
        draw.point((x,y), fill=rndColor())

# output text
for t in range(4):
    draw.text((60*t+10,10), rndChar(),font=font,fill=rndColor2())

# fuzzy
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')

