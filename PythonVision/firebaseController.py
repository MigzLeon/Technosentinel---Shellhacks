import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
#from google.cloud import storage
from firebase_admin import firestore


cred = ""
bucket = ""
def initializeFirebase():
    cred = credentials.Certificate('./technosentinelsServiceKey.json')

    firebase_admin.initialize_app(cred, {
        'databaseURL' : 'https://technosentinels.firebaseio.com/',
        'storageBucket' : 'technosentinels.appspot.com'
    })
    

def uploadToFirebase(image_name, name, temp):
    bucket = storage.bucket()
    imagePath = f"./{image_name}"

    imageBlob = bucket.blob(image_name)
    imageBlob.upload_from_filename(imagePath)

    db = firestore.client()

    ref = db.collection('technosentinels-images').document(image_name[2:][:-4])

    ref.set({
        'Name': name,
        'Temperature' : temp
    })


    



