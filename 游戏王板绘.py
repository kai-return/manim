
from manimlib import *
class 游戏王(Scene):
    def construct(self):
        word1 = Text(
            """
            Let the Duel Begin!
            """,
        font = "Sans",
        font_size = 30,
        slant = ITALIC,
        weight = BOLD,
        gradient = (RED,ORANGE,YELLOW,GREEN,BLUE,PURPLE)
        )
        word2 = Text(
            """
            以精美的板绘回望童年
            """,
        font = "KaiTi",
        font_size = 40,
        weight = BOLD,
        gradient = (ORANGE,GREEN)
        )
        figture01 = ImageMobject("F:\programming\python\manim_project\manim\manim_raster\烛龙与凤凰.jpg")
        figture02 = ImageMobject("F:\programming\python\manim_project\manim\manim_raster\巨神兵.jpg")
        figture03 = ImageMobject("F:\programming\python\manim_project\manim\manim_raster\翼神龙.jpg")
        figture04 = ImageMobject("F:\programming\python\manim_project\manim\manim_raster\天空龙和游戏.jpg")
        figture05 = ImageMobject("F:\programming\python\manim_project\manim\manim_raster\三幻神.jpg")
        figture06 = ImageMobject("F:\programming\python\manim_project\manim\manim_raster\破坏龙.jpg")
        figture07 = ImageMobject("F:\programming\python\manim_project\manim\manim_raster\三只青眼白龙.jpg")
        figture08 = ImageMobject("F:\programming\python\manim_project\manim\manim_raster\渊眼白龙.jpg")
        figture09 = ImageMobject("F:\programming\python\manim_project\manim\manim_raster\游戏回冥界.jpg")
        
        figture01.scale(1.5)
        figture02.scale(1.5)
        figture03.scale(1.5)
        figture04.scale(1.5)
        figture05.scale(1.5)
        figture06.scale(1.5)
        figture07.scale(1.5)
        figture08.scale(1.5)
        figture09.scale(1.5)
        
      
        self.add_sound("F:\programming\python\manim_project\manim\manim_sound\天军行阵乐.mp3")
        self.play(Write(word1),run_time = 5)
        self.play(FadeOutToPoint(word1,UP))
        self.wait(2)
        
        self.play(FadeIn(word2),run_time = 5)
        self.play(FadeOut(word2))
        self.wait(2)
        
        self.play(FadeIn(figture01),run_time = 2)
        self.play(FadeOut(figture01),run_time = 2)
        self.wait(2)
        
        self.play(FadeIn(figture02),run_time = 2)
        self.play(FadeOut(figture02),run_time = 2)
        self.wait(2)

        self.play(FadeIn(figture03),run_time = 2)
        self.play(FadeOut(figture03),run_time = 2)
        self.wait(2)

        self.play(FadeIn(figture04),run_time = 2)
        self.play(FadeOut(figture04),run_time = 2)
        self.wait(2)

        self.play(FadeIn(figture05),run_time = 2)
        self.play(FadeOut(figture05),run_time = 2)
        self.wait(2)

        self.play(FadeIn(figture06),run_time = 2)
        self.play(FadeOut(figture06),run_time = 2)
        self.wait(2)

        self.play(FadeIn(figture07),run_time = 2)
        self.play(FadeOut(figture07),run_time = 2)
        self.wait(2)

        self.play(FadeIn(figture08),run_time = 2)
        self.play(FadeOut(figture08),run_time = 2)
        

        self.play(FadeIn(figture09),run_time = 2)
        self.play(FadeOut(figture09),run_time = 2)
        self.clear()

        
