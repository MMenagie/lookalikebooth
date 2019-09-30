from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image

import pyttsx3


class CameraExample(App):

    def build(self):
        self.root = BoxLayout(orientation='vertical')
        self.horizontalBox = BoxLayout(orientation='horizontal')

        # Create a camera object
        self.cameraObject = Camera(play=False)
        self.cameraObject.play = True
        self.cameraObject.resolution = (1024, 1024)  # Specify the resolution
        self.cameraObject.size = (500, 500)

        im1 = Image(source="selfie.png")

        self.horizontalBox.add_widget(self.cameraObject)
        self.horizontalBox.add_widget(im1)

        # Create a button for taking photograph
        self.cameraButton = Button(text="Show me my lookalike!", size_hint = (.3,.3), pos_hint= {'center_x': 0.5, 'center_y': 0.5})
        # bind the button's on_press to onCameraClick
        self.cameraButton.bind(on_press=self.onCameraClick)

        self.root.add_widget(self.horizontalBox)
        self.root.add_widget(self.cameraButton)

        im1 = Image(source="image1.jpg")

        # return the root widget
        return self.root

    # Take the current frame of the video as the photo graph

    def onCameraClick(self, *args):
        self.cameraObject.export_to_png('selfie.png')
        self.speakText("Thank you so much for taking this picture!")

    def speakText(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()


# Start the Camera App

if __name__ == '__main__':
    CameraExample().run()