__author__ = 'johnliao'

# Third Party Resources
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

# Settings
CANVAS_HEIGHT=500
CANVAS_WIDTH=500
MAX_HEIGHT=400
MAX_WIDTH=435
FONT_NAME="Arial.ttf"
QUOTE="You learn to speak by speaking, to study by studying, to run by running, to work by working; in just the same way, you learn to love by loving. "
FONT_SIZE=40
START_HEIGHT=100

font = ImageFont.truetype(FONT_NAME,FONT_SIZE)
img=Image.new("RGBA", (CANVAS_WIDTH,CANVAS_HEIGHT),(255,255,255))
draw = ImageDraw.Draw(img)

LINE_HEIGHT = draw.textsize(QUOTE,font)[1]

# Parse the lines

done = False
lines = []
line = ''

for word in QUOTE.split():
    # if added word goes over, create new line
    text_width = draw.textsize(line,font)[0]
    print "for |||", line,"||| the width is", text_width

    if draw.textsize(line+word,font)[0]>MAX_WIDTH:
        lines.append(line)
        line=''
        line+=word
        line+=' '
    else:
        line+=word
        line+=' '

lines.append(line) # add last line

# Create the img

for num_lines in range(len(lines)):
    draw.text((20, START_HEIGHT+LINE_HEIGHT *num_lines),lines[num_lines],(0,0,0),font=font)

draw.text((20, START_HEIGHT+LINE_HEIGHT*len(lines)+LINE_HEIGHT),"- Some pino",(0,0,0),font=font)

draw = ImageDraw.Draw(img)

img.save("a_test.png")