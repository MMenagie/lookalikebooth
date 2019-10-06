import face_recognition
import os
import numpy as np
import glob
import pyttsx3
from PIL import Image


class FaceDetector:

    def __init__(self):
        self.input_images = list(glob.glob(os.getcwd() + '/input/' + '*.jpg'))
        self.known_encodings = []
        self.names = []
        self.face_distances = []


    def get_face_encodings(self):
        for file in self.input_images:
            self.names.append(file.split('/')[-1][:-4])
            known_image = face_recognition.load_image_file(file)
            try:
                face_encoding = face_recognition.face_encodings(known_image)[0]
            except Exception as e:
                print('No face detected')
            self.known_encodings.append(face_encoding)

    def speak_text(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def get_lookalike(self, input_image_path):
        # Load a test image and get encodings for it
        image_to_test = face_recognition.load_image_file(input_image_path)
        image_to_test_encoding = face_recognition.face_encodings(image_to_test)[0]

        # See how far apart the test image is from the known faces
        face_distances = face_recognition.face_distance(self.known_encodings, image_to_test_encoding)
        lookalike_index = np.argpartition(face_distances.flatten(), 1)[1]
        lookalike_image_path = self.input_images[lookalike_index]

        return face_distances, lookalike_index, lookalike_image_path

    # print(face_distances[lookalike_index])
    # print(self.names[lookalike_index])
    # img = Image.open(input_images[lookalike_index])
    # img.show()
    # speak_text('Wow you look so much like'.format(names[lookalike_index]))




