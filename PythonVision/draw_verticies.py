import io
import random
from PIL import Image, ImageDraw, ImageFont
from firebaseController import uploadToFirebase

def drawVerticies(image_source, vertices, filename, temps, names):

    

    randTempI = random.randint(0, len(temps) - 1)
    randNameI = random.randint(0, len(names) - 1)

    pillow_img = Image.open(io.BytesIO(image_source))

    draw = ImageDraw.Draw(pillow_img)

    for i in range(len(vertices) - 1):
        draw.line(((vertices[i].x, vertices[i].y), (vertices[i+1].x, vertices[i+1].y)),
                fill='green',
                width=8
        )

    draw.line(((vertices[len(vertices) - 1].x, vertices[len(vertices) - 1].y),
                (vertices[0].x, vertices[0].y)), 
                fill='green', 
                width=8)

    font = ImageFont.truetype('/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf', 36)

    draw.text((vertices[0].x + 10, vertices[0].y),
                font=font, 
                text=names[randNameI] + " " + str(temps[randTempI])[:4] + " °F", 
                fill=(255, 255, 255)
             )
    pillow_img.save(filename)
    uploadToFirebase(filename, names[0], str(temps[randTempI])[:4])
    