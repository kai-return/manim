from manimlib import *
class test(Scene):
    def construct(self):
        word = Text("你好")
        self.play(Write(word))
        
