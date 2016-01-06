#!/usr/bin/python

import random

# Third-party dependencies
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

from config import *

c = random.randint(0,len(COLOR_SCHEME)-1)
BG_COLOR = COLOR_SCHEME[c]["bg"]
FONT_COLOR = COLOR_SCHEME[c]["font_color"]
FONT_TYPE = random.choice(FONT_NAME)

def parse_text(quote):
    # declare PIL objects
    img=Image.new("RGBA", (CANVAS_WIDTH,CANVAS_HEIGHT),BG_COLOR)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_TYPE, FONT_SIZE)

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

    return lines, font, draw, img

def text2img(quote, author):
    global FONT_SIZE
    done = False

    while(not done):
        lines, font, draw, img = parse_text(quote)
        line_height = draw.textsize("T",font)[1] + draw.textsize("T",font)[1]/3 # dummy char T + in line buffer
        num_lines = len(lines)
        txt_height = line_height*num_lines

        if txt_height > MAX_HEIGHT: # too tall
            FONT_SIZE-=1
        else:
            Y=CANVAS_HEIGHT/2-txt_height/2-line_height/2 # center it
            done = True


    # Create the img
    for c in range(num_lines):
        x = X
        y = Y+line_height*c

        text = lines[c]

        draw.text((x, y),text, FONT_COLOR, font=font)

    author_y = Y+line_height*num_lines+line_height/3

    if author!='':

        while draw.textsize('-'+author,font)[0]>MAX_WIDTH-x-15:
            print "author name too long! resizing... ",draw.textsize('-'+author,font)
            FONT_SIZE-=1
            font = ImageFont.truetype(FONT_TYPE, FONT_SIZE)

        draw.text((x+100, author_y),'- '+author, FONT_COLOR, font=font)

    img.save("quote_img.png")

if __name__=='__main__':
    text2img('She sells sea shells down by the seashore. ','Mr Albert Einstein Frederick Barney Jr.')