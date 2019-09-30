import face_recognition
import os

path = 'C:/Users/MMenagie/PycharmProjects/Lookalikebooth/GUI/input'
known_encodings_dict = {}
for filename in os.listdir(path):

    if filename.endswith(".jpg"):
        name = filename[:-4]
        filepath = os.path.join(path, filename)
        known_image = face_recognition.load_image_file(filepath)
        face_encoding = face_recognition.face_encodings(known_image)[0]
        known_encodings_dict[name] = face_encoding

known_encodings = known_encodings_dict.values()

# Load a test image and get encondings for it
image_to_test = face_recognition.load_image_file(filepath)
image_to_test_encoding = face_recognition.face_encodings(image_to_test)[0]

# See how far apart the test image is from the known faces
face_distances = face_recognition.face_distance(known_encodings, image_to_test_encoding)

for i, face_distance in enumerate(face_distances):
    print("The test image has a distance of {:.2} from known image #{}".format(face_distance, i))
    print("- With a normal cutoff of 0.6, would the test image match the known image? {}".format(face_distance < 0.6))
    print("- With a very strict cutoff of 0.5, would the test image match the known image? {}".format(face_distance < 0.5))
    print()
