from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Color, RoundedRectangle, Line
from kivy.graphics import Color, Line,Rectangle
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Canvas, Color, Ellipse, Rectangle

class TransparentBoxLayout(BoxLayout):
    def __init__(self,widget=None ,**kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(0.2, 0.2, 0.2, 1)  # Black color for padding and lines between sections
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[10])
        self.bind(size=self._update_rect, pos=self._update_rect)
        if widget:
            self.add_widget(widget)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class VerticalTextLabel(Label):
    def __init__(self, **kwargs):
        super(VerticalTextLabel, self).__init__(**kwargs)
        self.text = self.transform_text(kwargs.get('text', ''))
        self.valign = 'middle'
        self.halign = 'center'
        self.bind(size=self.update_text_size)
        self.font_size = '10sp'  # Reduced font size
        self.text_size = (self.width, None)
        self.padding_y = -10  # Reduced space between characters vertically

    def transform_text(self, text):
        return '\n'.join(text)
    
    def update_text_size(self, *args):
        self.text_size = (self.width, None)

class TitleStrip(BoxLayout):
    def __init__(self, title,widget=None,**kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.padding = 5
        with self.canvas.before:
            Color(0.5, 0.5, 0.5, 1)  # Grey background
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[10])
        self.bind(size=self._update_rect, pos=self._update_rect)
        if type(title) == type("asdfa"):
            title_label = VerticalTextLabel(text=title, size_hint=(None, 1), width=10, color=(1, 0.5, 0, 1))
        else :
            title_label =title
        title_label.size_hint_x=0.05
        title_label.halign='center'
        title_label.valign='center'
        self.add_widget(title_label)
        
        if widget:
            self.add_widget(TransparentBoxLayout(size_hint=(1, 1),widget=widget))
        else :
            self.add_widget(TransparentBoxLayout(size_hint=(1, 1)))

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class TimelineWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.total_bars = 4  # Example: Total number of bars in the timeline
        self.beats_per_bar = 4  # Example: Beats per bar
        self.sub_beats_per_beat = 4  # Example: Sub-beats per beat
        self.sub_sub_beats_per_sub_beat = 4  # Example: Sub-sub-beats per sub-beat
        self.beat_duration = 2.5  # Example: Duration of each beat in seconds
        self.timeline_height = 50  # Example: Height of the timeline area

    def draw_timeline(self):
        self.canvas.clear()
        
        # Grey background for timeline
        with self.canvas:
            Color(0.2, 0.2, 0.2, 1)
            self.background_rect = Rectangle(pos=self.pos, size=self.size)
        
        # Orange markers and black text
        with self.canvas:
            Color(1, 0.5, 0, 1)  # Orange color for markers
            
            major_line_width = 2
            minor_line_width = 1
            sub_minor_line_width = 0.5  # Width for sub-sub-beat lines
            
            bar_width = self.width / self.total_bars
            beat_width = bar_width / self.beats_per_bar
            
            for bar_index in range(self.total_bars):
                bar_start_x = self.x + bar_index * bar_width
                Line(points=[bar_start_x, self.y, bar_start_x, self.y + self.timeline_height], width=major_line_width)
                
                # Draw text below each bar (only once per bar)
                if bar_index == 0:
                    bar_label = Label(text=f"Bar {bar_index + 1}", pos=(bar_start_x, self.y - 40), font_size=12)
                    self.add_widget(bar_label)
                
                for beat_index in range(self.beats_per_bar):
                    beat_start_x = bar_start_x + beat_index * beat_width
                    Line(points=[beat_start_x, self.y, beat_start_x, self.y + self.timeline_height * 0.8], width=major_line_width)
                    
                    for sub_beat_index in range(self.sub_beats_per_beat):
                        sub_beat_start_x = beat_start_x + sub_beat_index * beat_width / self.sub_beats_per_beat
                        Line(points=[sub_beat_start_x, self.y, sub_beat_start_x, self.y + self.timeline_height * 0.6], width=minor_line_width)
                        
                        for sub_sub_beat_index in range(self.sub_sub_beats_per_sub_beat):
                            sub_sub_beat_start_x = sub_beat_start_x + sub_sub_beat_index * beat_width / (self.sub_beats_per_beat * self.sub_sub_beats_per_sub_beat)
                            Line(points=[sub_sub_beat_start_x, self.y, sub_sub_beat_start_x, self.y + self.timeline_height * 0.4], width=sub_minor_line_width)
                            
                            # Calculate beat, sub-beat, and sub-sub-beat numbers
                            beat_number = bar_index * self.beats_per_bar + beat_index + 1
                            sub_beat_number = sub_beat_index + 1
                            sub_sub_beat_number = sub_sub_beat_index + 1
                            
                            # Calculate time in minutes, seconds, milliseconds
                            time_seconds = (bar_index * self.beats_per_bar * self.beat_duration +
                                            beat_index * self.beat_duration +
                                            sub_beat_index * (self.beat_duration / self.sub_beats_per_beat) +
                                            sub_sub_beat_index * (self.beat_duration / (self.sub_beats_per_beat * self.sub_sub_beats_per_sub_beat)))
                            time_label_text = self.convert_seconds_to_time(time_seconds)
                            
                            # Display beat and time information
                            text_label = Label(text=f"{beat_number}.{sub_beat_number}.{sub_sub_beat_number}\n{time_label_text}",
                                               pos=(sub_sub_beat_start_x, self.y - 80), font_size=10)
                            self.add_widget(text_label)

    def convert_seconds_to_time(self, seconds):
        minutes = seconds // 60
        seconds %= 60
        milliseconds = (seconds - int(seconds)) * 1000
        return f"{int(minutes):02}:{int(seconds):02}:{int(milliseconds):03}"


    def on_size(self, instance, value):
        self.draw_timeline()

    def on_pos(self, instance, value):
        self.draw_timeline()
