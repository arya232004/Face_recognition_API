import face_recognition
import fastapi
from fastapi import File, Query, UploadFile
import numpy as np
from PIL import Image

app = fastapi.FastAPI()

# @app.get("/my-first-api")
# def face_compare():
#     known_image = face_recognition.load_image_file("modirc.jpeg")
#     unknown_image = face_recognition.load_image_file("messi.jpg")
    
#     biden_encoding = face_recognition.face_encodings(known_image)[0]
#     xd=biden_encoding.tolist()
#     print(biden_encoding.tolist())
#     print(np.array(xd))
#     unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    
#     results = face_recognition.compare_faces([biden_encoding], unknown_encoding,tolerance=0.4)
    
#     # print(results)  # Convert the NumPy boolean to a standard Python boolean
# face_compare()

# def face_compare(file: UploadFile = File(...),file2: UploadFile = File(...)):
#     new_image = face_recognition.load_image_file(file2.file)
#     known_encoding = file.file.read()
#     print(known_encoding)
#     unknown_encoding = face_recognition.face_encodings(new_image)[0]
    
#     results = face_recognition.compare_faces([known_encoding], unknown_encoding,tolerance=0.4)
    
    # return (results[0])
    
res=[-0.1296335905790329,0.11865267902612686,0.042048193514347076,-0.07465116679668427,-0.1339898258447647,0.08268710970878601,-0.1293669193983078,-0.05473081022500992,0.055019885301589966,-0.11365728080272675,0.1535521298646927,-0.004334757104516029,-0.19565416872501373,0.055297598242759705,-0.015104947611689568,0.09905815869569778,-0.15631365776062012,-0.1403791308403015,-0.13622581958770752,-0.12228140980005264,-0.013645041733980179,0.12318163365125656,-0.043524812906980515,0.05943893641233444,-0.1157652884721756,-0.3108506202697754,-0.05474462732672691,-0.05070725455880165,0.08042126148939133,-0.06423744559288025,0.033852823078632355,-0.07063330709934235,-0.15970727801322937,0.054086051881313324,0.10177410393953323,0.06541791558265686,-0.0022023082710802555,2.7478672564029694e-05,0.2184930294752121,-0.03293294459581375,-0.17857684195041656,-0.0036726673133671284,0.10108157247304916,0.22190847992897034,0.07929962128400803,0.05335184931755066,0.004198402166366577,-0.07082074880599976,0.06751064211130142,-0.21772101521492004,0.08031651377677917,0.20793728530406952,0.04705461114645004,0.12276661396026611,0.07078711688518524,-0.17296135425567627,0.010294654406607151,0.19503796100616455,-0.08183661103248596,0.1250942498445511,0.05096941441297531,-0.10738998651504517,-0.06481314450502396,-0.07874201238155365,0.19444122910499573,0.12256152182817459,-0.12076102197170258,-0.2947007417678833,0.1294303983449936,-0.1448253095149994,-0.135600283741951,0.1271834820508957,-0.050301507115364075,-0.09248461574316025,-0.26736578345298767,-0.0009278338402509689,0.40435540676116943,0.1770469844341278,-0.22176037728786469,-0.01987495645880699,-0.05943359062075615,-0.008760842494666576,0.09497836232185364,0.037018418312072754,-0.11041150987148285,-0.05459905415773392,-0.039564475417137146,0.060279689729213715,0.21132014691829681,0.07754091173410416,-0.04349805787205696,0.13885709643363953,0.029455188661813736,0.07773739099502563,0.02155926451086998,0.12526386976242065,-0.11187764257192612,-0.058408819139003754,-0.07126646488904953,-0.0003563491627573967,0.06789117306470871,-0.030092203989624977,0.04301697760820389,0.17149566113948822,-0.18811795115470886,0.24451155960559845,-0.042707864195108414,-0.012110607698559761,0.016888922080397606,0.1773260235786438,-0.056786857545375824,0.016072163358330727,0.19638782739639282,-0.2846164405345917,0.2543637156486511,0.20409247279167175,0.0032053214963525534,0.11205124109983444,0.09461023658514023,0.08517415076494217,-0.02967846766114235,-0.02059059590101242,-0.2152501493692398,-0.16748110949993134,-0.03470742329955101,-0.08433286100625992,0.03541935607790947,0.04673030599951744]    
# def face_compare():
#     new_image = face_recognition.load_image_file('modirc.jpeg')
    
#     # Calculate the encoding of the unknown face
#     unknown_encoding = face_recognition.face_encodings(new_image)[0]
#     print(np.array(res))
#     known=np.array(res)
#     results = face_recognition.compare_faces([known], unknown_encoding, tolerance=0.4)
#     print(results)
#     # Read known encoding from the file
#     known_encoding =open("encode.txt", "r").read()
#     print(list(np.array(known_encoding)))
def face_compare():
    new_image = face_recognition.load_image_file('cr7_copy.jpg')
    
    # Calculate the encoding of the unknown face
    unknown_encoding = face_recognition.face_encodings(new_image)[0]
    
    known_encoding = np.array(res)
    
    # Compare the encodings
    results = face_recognition.compare_faces([known_encoding], unknown_encoding, tolerance=0.4)
    
    print(results)

face_compare()    
    # Load the image to compare
   
    
    # Compare the encodings
   
    
# face_compare()
# face_compare(file=UploadFile(),file2=UploadFile("modric.jpeg"))