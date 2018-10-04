import gi
from kivy.app import App
from mainwindow.MainWindow import MainWindow

gi.require_version('Gtk', '3.0')


class Main(App):
    def build(self):

        return MainWindow()


if __name__ == '__main__':
    Main().run()
