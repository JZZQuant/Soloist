from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.graphics import RoundedRectangle, Color, Line
from ui.widgets import TransparentBoxLayout, VerticalTextLabel, TitleStrip,TimelineWidget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image

class AudioRecorderApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='horizontal', padding=10, spacing=10)
        
        left_column = TransparentBoxLayout(orientation='vertical', size_hint=(0.7, 1), padding=5, spacing=10)
        
        menu = TransparentBoxLayout(size_hint=(1, 0.03))  
        for item in ['File', 'Edit', 'Settings', 'View', 'License']:
            button = Button(text=item, size_hint=(None, 1), width=80 ,background_color=(0.5, 0.5, 0.5, 1), color=(1, 0.5, 0, 1), background_normal='')
            button.bind(on_press=self.on_button_click)  
            button.bind(on_release=self.on_button_release)  
            menu.add_widget(button)
        left_column.add_widget(menu)
        
        notation = TitleStrip(title=Image(source='assets/treble.png'), size_hint=(1, 0.6))  
        left_column.add_widget(notation)
        
        backing = TitleStrip(title=Image(source='assets/wav.png'), size_hint=(1, 0.15))  
        left_column.add_widget(backing)
        
        recording = TitleStrip(title=Image(source='assets/record.png'), size_hint=(1, 0.2))  
        left_column.add_widget(recording)

        timeline_widget = TimelineWidget(size_hint=(1, 1))
        timeline = TitleStrip('', widget=timeline_widget ,size_hint=(1, 0.2))  
        left_column.add_widget(timeline)
        
        controls = TransparentBoxLayout(size_hint=(1, 0.06), spacing=5)  
        icons = ['⏺', '▶', '⏸', '⏹', '🔁']
        for icon in icons:
            button = Button(text=icon, size_hint=(None, 1), width=40, background_color=(0.5, 0.5, 0.5, 1), color=(1, 0.5, 0, 1), background_normal='')
            button.bind(on_press=self.on_button_click)  
            button.bind(on_release=self.on_button_release) 
            controls.add_widget(button)
        controls.add_widget(TextInput(text='120'  , size_hint=(None, 1), width=60, background_color=(0.5, 0.5, 0.5, 1), foreground_color=(1, 0.5, 0, 1)))
        controls.add_widget(TextInput(text='4/4', size_hint=(None, 1), width=60, background_color=(0.5, 0.5, 0.5, 1), foreground_color=(1, 0.5, 0, 1)))
        controls.add_widget(TextInput(hint_text='Search', size_hint=(1, 1), background_color=(0.5,1, 1, 1), foreground_color=(1, 0.5, 0, 1)))
        left_column.add_widget(controls)
        
        main_layout.add_widget(left_column)
        
        right_column = TransparentBoxLayout(orientation='vertical', size_hint=(0.3, 1), padding=5, spacing=10)
        
        video_scroll = ScrollView(size_hint=(1, 0.4))
        video_grid = GridLayout(cols=1, size_hint=(1, None), spacing=5, padding=5)
        video_grid.bind(minimum_height=video_grid.setter('height'))
        video_grid.add_widget(Image(source='assets/record.png', size_hint=(1, None), height=300))
        video_scroll.add_widget(video_grid)
        right_column.add_widget(video_scroll)
        
        mixer_scroll = ScrollView(size_hint=(1, 0.4))
        mixer_grid = GridLayout(cols=4, size_hint=(1, None), spacing=2, padding=5)
        mixer_grid.bind(minimum_height=mixer_grid.setter('height'))
        instruments = ['Guitar', 'Bass', 'Drums', 'Vocals']
        for instrument in instruments:
            mixer_grid.add_widget(Label(text=instrument, color=(1, 0.5, 0, 1)))
            mixer_grid.add_widget(Label(text='Sub', color=(1, 0.5, 0, 1)))
            button1 = Button(text='🔴', size_hint=(None, 1), width=40, background_color=(0.5, 0.5, 0.5, 1), color=(1, 0.5, 0, 1), background_normal='')
            button1.bind(on_press=self.on_button_click)  
            button1.bind(on_release=self.on_button_release)   
            mixer_grid.add_widget(button1)
            button2 = Button(text='FX', size_hint=(None, 1), width=40, background_color=(0.5, 0.5, 0.5, 1), color=(1, 0.5, 0, 1), background_normal='')
            button2.bind(on_press=self.on_button_click)  
            button2.bind(on_release=self.on_button_release)   
            mixer_grid.add_widget(button2)
        mixer_scroll.add_widget(mixer_grid)
        right_column.add_widget(mixer_scroll)
        
        effects_layout = TransparentBoxLayout(orientation='vertical', size_hint=(1, 0.2), spacing=5)
        effects_header = TransparentBoxLayout(size_hint=(1, 0.2))
        effects_header.add_widget(Label(text='Marketplace AI Effects', color=(1, 0.5, 0, 1)))
        button = Button(text='🔄', size_hint=(None, 1), width=40, background_color=(0.5, 0.5, 0.5, 1), color=(1, 0.5, 0, 1), background_normal='')
        button.bind(on_release=self.on_button_release)  
        button.bind(on_press=self.on_button_click)  
        effects_header.add_widget(button)
        effects_layout.add_widget(effects_header)
        
        effects_scroll = ScrollView(size_hint=(1, 0.8))
        effects_grid = GridLayout(cols=3, size_hint=(1, None), spacing=5, padding=5)
        effects_grid.bind(minimum_height=effects_grid.setter('height'))
        for i in range(15):
            button = Button(text=f'Effect {i+1}', size_hint=(1, None), height=50, background_color=(0.5, 0.5, 0.5, 1), color=(1, 0.5, 0, 1), background_normal='')
            button.bind(on_press=self.on_button_click)  
            button.bind(on_release=self.on_button_release) 
            effects_grid.add_widget(button)
        effects_scroll.add_widget(effects_grid)
        effects_layout.add_widget(effects_scroll)
        
        right_column.add_widget(effects_layout)
        
        main_layout.add_widget(right_column)
        
        return main_layout
    
    def on_button_click(self, instance):
        instance.background_color = (1, 0.5, 0, 1)  # Change background color to orange
        instance.color = (0, 0, 0, 1)  # Change text color to black
    
    def on_button_release(self, instance):
        instance.background_color = (0.5, 0.5, 0.5, 1)  # Reset background color
        instance.color = (1, 0.5, 0, 1)  # Reset text color

    