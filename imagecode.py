import base64

image_path = "modirc.jpeg"
with open(image_path, "rb") as image_file:
    image_data = image_file.read()

base64_encoded_image_data = base64.b64encode(image_data)
base64_encoded_image_data_str = base64_encoded_image_data.decode("utf-8")

print("Base64 Encoded Image Data:")
print(base64_encoded_image_data_str)
