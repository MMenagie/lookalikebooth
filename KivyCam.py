from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from FaceDetector import FaceDetector
import os
import time

import pyttsx3


class CameraExample(App):

    def build(self):
        #initialize the FaceDetector by calculating face encodings for all available skype pictures
        self.face_detector = FaceDetector()
        self.face_detector.get_face_encodings()

        self.root = BoxLayout(orientation='vertical')


        """create the first horizontal box with a camera object on the left and a resulting picture on the right"""
        self.horizontalBox1 = BoxLayout(orientation='horizontal')

        # Create a camera object
        self.cameraObject = Camera(play=False)
        self.cameraObject.play = True
        #self.cameraObject.resolution = (1024, 1024)  # Specify the resolution
        #self.cameraObject.size = (500, 500)

        self.im1 = Image(source="input_image.png")

        self.horizontalBox1.add_widget(self.im1)



        """create the second horizontal box with resulting text"""
        self.horizontalBox2 = Label(text="Which colleague looks most like you!?",
                                font_size='20sp')


        """create the third horizontal box with a button to start the lookalike process"""
        self.horizontalBox3 = BoxLayout(orientation='horizontal')

        # Create a button for taking photograph
        self.cameraButton = Button(text="Show me my lookalike!", size_hint=(.3, .3), background_normal = '', background_color=(255,0,0,0.2),
                                   pos_hint={'center_x': 0.5, 'center_y': 0.5})
        # bind the button's on_press to onCameraClick
        self.cameraButton.bind(on_press=self.onCameraClick)
        self.horizontalBox3.add_widget(self.cameraButton)


        """create the second horizontal box with a button to start the lookalike process"""
        self.horizontalBox3 = BoxLayout(orientation='horizontal')

        # Create a button for taking photograph
        self.cameraButton = Button(text="Show me my lookalike!", size_hint=(.3, .3),
                                   pos_hint={'center_x': 0.5, 'center_y': 0.5})
        # bind the button's on_press to onCameraClick
        self.cameraButton.bind(on_press=self.onCameraClick)
        self.horizontalBox3.add_widget(self.cameraButton)


        """add all boxes to the root of the Kivy app"""
        self.root.add_widget(self.horizontalBox1)
        self.root.add_widget(self.horizontalBox2)
        self.root.add_widget(self.horizontalBox3)

        # return the root widget
        return self.root

    # Take the current frame of the video as the photo graph

    def onCameraClick(self, *args):
        #face_detector = FaceDetector()
        camera = self.cameraObject
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))

        #face_distances, lookalike_index = self.face_detector.get_lookalike(os.getcwd() + "/IMG_{}.png".format(timestr))
        face_distances, lookalike_index, lookalike_image_path = self.face_detector.get_lookalike(os.getcwd() + "/input_image.png")

        self.im2 = Image(source=lookalike_image_path)
        self.im2.pos_hint = {'center_y': 0.5}
        self.horizontalBox1.add_widget(self.im2)

        self.horizontalBox2.text = "You look so much like {}!".format(self.face_detector.names[lookalike_index])

        print(face_distances[lookalike_index])
        print(self.face_detector.names[lookalike_index])

        self.speakText("Let me see if I can find a colleague who looks like you")
        self.speakText("You don't have an easy face to explore though")


    def speakText(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()


# Start the Camera App

if __name__ == '__main__':
    CameraExample().run()