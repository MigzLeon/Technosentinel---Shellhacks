import os, io
import requests
import shutil
from google.cloud import vision
from google.cloud.vision import types
from draw_verticies import drawVerticies
from thermalFilter import applyThermal
import numpy as np
from firebaseController import initializeFirebase


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'/home/mike/ShellHacks2020/VisionAPI/VideoStreaming-a798b46c871b.json'

temps = []

for x in np.arange(90.0, 97.0, 0.1):
    temps.append(x)


names = ["Michael Duboc", "Aaron Eckhart", "Miguel Saravia", "Miguel deJesus", "Ricardo Lima", "Manuel Kamboykos", "Jessica Alba", "Joh Doe", "Johnny Appleseed", "Michael DeSantos"]

initializeFirebase()
client = vision.ImageAnnotatorClient()

image_url = "http://104.189.92.128:8080/?action=snapshot"
filename="output.jpg"

while True:

    r = requests.get(image_url, stream=True)

    if(r.status_code == 200):
        r.raw.decode_content = True

    with open(filename,'wb') as f:
        shutil.copyfileobj(r.raw, f)

    applyThermal(filename)
    with open(filename, 'rb') as o:
        content = o.read()



    image = vision.types.Image(content=content)
    #image.source.image_uri = 'http://104.189.92.128:8080/?action=snapshot'
    response = client.face_detection(image=image)


    faceAnnotation = response.face_annotations

    for faces in faceAnnotation:
        vertices = faces.bounding_poly.vertices
        drawVerticies(content, vertices, filename, temps, names)

    
