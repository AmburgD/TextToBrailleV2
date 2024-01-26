from PIL import Image, ImageDraw, ImageFont

# create an image (mode, size, color)
out = Image.new("RGB", (150, 100), (255, 255, 255))

# get a font
fnt = ImageFont.truetype("GlametrixBold-4dW6.otf", 40)
# get a drawing context
d = ImageDraw.Draw(out)

# draw multiline text
d.multiline_text((10, 10), "Hello\nWorld", font=fnt, fill=(0, 0, 0))

out.show()

with open('MultiLineTest.txt', 'r+') as f:
    for line in f.readlines():
        print(line)