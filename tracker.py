import rumps
import sys
from PyQt4.QtGui import QPixmap, QApplication
import QTKit
from AppKit import NSJPEGFileType
from camera import Camera

app = QApplication(sys.argv)

camera = Camera.alloc().init()

@rumps.timer(5)
def capture_camera(sender):
    camera.capture('/tmp/camera.jpg', NSJPEGFileType)

@rumps.timer(5)
def capture_desktop(sender):
    QPixmap.grabWindow(QApplication.desktop().winId()).save('/tmp/screenshot.png', 'png')

class Capture(rumps.App):
    def __init__(self):
        super(Capture, self).__init__("Capture")
        self.menu = ["Preferences", "Pause"]

    @rumps.clicked("Preferences")
    def prefs(self, sender):
        rumps.alert("todo")

    @rumps.clicked("Pause")
    def pause(self, _):
        rumps.alert("todo")

if __name__ == "__main__":
    Capture().run()
