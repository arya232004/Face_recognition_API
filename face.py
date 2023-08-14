import face_recognition
import fastapi
from fastapi import File, Form, Query, UploadFile
import numpy as np
from typing import List
from fastapi.responses import JSONResponse

app = fastapi.FastAPI()
@app.post("/compare")
def face_compare(encodings: str = Form(...), image_to_compare: UploadFile = File(...)):
    try:
        # Convert the string representation of the list into a list of floats
        encodings_list = [float(value) for value in encodings.strip("[]").split(",")]

        # Load the uploaded image and calculate its encoding
        new_image = face_recognition.load_image_file(image_to_compare.file)
        unknown_encoding = face_recognition.face_encodings(new_image)[0]

        # Convert the list to a numpy array for comparison
        known_encoding = np.array(encodings_list)

        # Calculate the face distance (similarity score)
        face_distance = face_recognition.face_distance([known_encoding], unknown_encoding)[0]

        # Convert the face distance to similarity percentage
        similarity_percentage = (1 - face_distance) * 100
        
        if(similarity_percentage >=60):
           return {"similarity_percentage": similarity_percentage,
                   "result": True}
        else:
              return {"similarity_percentage": similarity_percentage,
                     "result": False}   
    except Exception as e:
        return {"error": str(e)}



@app.post("/encode")     
def encode(file: UploadFile = File(...)):
    image_enco=face_recognition.load_image_file(file.file)
    image_enco=face_recognition.face_encodings(image_enco)[0]
    return {"result": image_enco.tolist()}  


    
