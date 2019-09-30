from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image

import pyttsx3


class CameraExample(App):

    def build(self):
        root = BoxLayout(orientation='horizontal')

        box1 = BoxLayout(orientation='vertical')
        box2 = BoxLayout(orientation='vertical')

        # Create a camera object
        self.cameraObject = Camera(play=False)
        self.cameraObject.play = True
        self.cameraObject.resolution = (1024, 1024)  # Specify the resolution
        self.cameraObject.size = (500, 500)

        # Create a button for taking photograph
        self.cameraButton = Button(text="Show me my lookalike!")
        self.cameraButton.size_hint = (.5, .2)
        self.cameraButton.pos_hint = {'x': .25, 'y': .75}

        # bind the button's on_press to onCameraClick
        self.cameraButton.bind(on_press=self.onCameraClick)

        im1 = Image(source="image2.png")

        # add camera and button to the layout
        box1.add_widget(self.cameraObject)
        box1.add_widget(self.cameraButton)

        box2.add_widget(im1)

        root.add_widget(box1)
        root.add_widget(box2)

        # return the root widget
        return root

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