import kivy
from kivy.config import Config
from kivy.app import App
from ui.layouts import AudioRecorderApp
from kivy.lang import Builder

# Enable debug mode
kivy.Config.set('kivy', 'log_level', 'debug')

if __name__ == '__main__':
    AudioRecorderApp().run()
