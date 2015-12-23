#!/usr/bin/python

# Third-party dependencies
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

from config import *

def parse_text(quote, draw, font):
    lines = []
    line = ''

    for word in quote.split():
        # if added word goes over, create new line
        if draw.textsize(line+word,font)[0]>MAX_WIDTH:
            lines.append(line)
            line=''
            line+=word
            line+=' '
        else:
            line+=word
            line+=' '

    lines.append(line) # add last line

    return lines

def text2img(quote, author):
    # declare PIL objects
    font = ImageFont.truetype(FONT_NAME,FONT_SIZE)
    img=Image.new("RGBA", (CANVAS_WIDTH,CANVAS_HEIGHT),(255,255,255))
    draw = ImageDraw.Draw(img)

    lines = parse_text(quote, draw, font)

    line_height = draw.textsize("T",font)[1] # use dummy char T to find line height

    # Create the img
    for num_lines in range(len(lines)):
        draw.text((20, START_HEIGHT+line_height*num_lines),lines[num_lines],(0,0,0),font=font)

    draw.text((20, START_HEIGHT+line_height*len(lines)+line_height),'-'+author,(0,0,0),font=font)

    img.save("quote_img.png")

if __name__=='__main__':
    text2img('He sells seashells down by the seashore','Albert Einstein')