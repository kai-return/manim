from manimlib import *
class tet(Scene):
    def construct(self):
        word = Text("你好",font = "KaiTi")
        self.play(Write(word))
        
