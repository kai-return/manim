from manimlib import *

class 毕业祝贺信(Scene):

    def construct(self):

        #making objects

        word1 = Text(
            """
            May you have health,happiness and outstanding success in all your future!
            """,
        font = "Times New Roman",
        font_size = 30,
        slant = ITALIC,
        weight = BOLD,
        gradient= (RED,ORANGE,YELLOW,GREEN,BLUE,BLUE_E,PURPLE)
        )

        word2 = Text(
            """
            在毕业之际，祝愿我亲爱的同门秦若珊、崔子威前程似锦！
            """,
        font = "KaiTi",
        font_size = 40,
        weight = BOLD,
        gradient = (RED,BLUE)
        )
        word3 = Text(
            """
            虽然在未来我们将会相隔千里,\n但这三年来建立的友谊却让我们如在咫尺！！
            """,
        font = "SimHei",
        font_size = 40,
        gradient = (ORANGE,GREEN)
        )
        word4 = Text(
            """
            You`re wonderful friends, in the future,\n I treasure the friendship between us more with every year
            """,
        font = "LiSu",
        font_size = 40,
        gradient = (RED,YELLOW)
        )
        word5 = Text(
            """
            At last , 愿将来的我们，终能扶摇而上，\n acquiring a new great achievement.
            """,
        font = "YouYuan",
        font_size = 40,
        gradient = (YELLOW,GREEN)
        )
        word6 = Text(
            """
            OF COURSE ,对于师弟师妹们  \n I AM ALSO SURE THAT JUNIOR WILL BE BETTER AND BETTER
            """,
        font = "SimSun",
        font_size = 40,
        gradient = (RED,PURPLE)
        )
        word7 = Text(
            """
            这三年的共同学习生涯永远值得怀念！\n May the friendship last forever!
            """,
        font = "FangSong",
        font_size = 40,
        gradient = (RED,PURPLE,GREEN)
            )

        author = Text("----HAPPY PRINCE 凯",color = RED,font = "KaiTi",font_size= 25)
        fig01 = ImageMobject("F:\\vscode_project\\raster_source\IMG_20200609_133615.jpg")
        fig02 = ImageMobject("F:\\vscode_project\\raster_source\IMG_20200621_143132.jpg")
        fig03 = ImageMobject("F:\\vscode_project\\raster_source\IMG_20200926_182529.jpg")
        fig04 = ImageMobject("F:\\vscode_project\\raster_source\IMG_20201013_185533.jpg")
        fig05 = ImageMobject("F:\\vscode_project\\raster_source\\figture.jpg")
        fig01.scale(1.5)
        fig02.scale(1.5)
        fig03.scale(1.5)
        fig04.scale(1.5)
        fig05.scale(1.5)
        #position
        word1.to_edge(UP)
        author.next_to(word1.get_corner(DOWN),DOWN)
        
        
        #annimation
      
        self.add_sound("the truth that you leave")   #i will be damned  it worded!!
        self.play(Write(word1),run_time = 10)
        self.play(FadeInFromPoint(author,DOWN),run_time = 10)
        self.wait(2)


        self.play(Transform(word1,word2),ApplyMethod(author.move_to,word2.get_corner(RIGHT+DOWN)+DOWN+2*LEFT),run_time = 5)
        self.play(ApplyMethod(author.scale,1.6),run_time =2)
        author.set_color(ORANGE)
        self.wait()
        self.play(FadeOutToPoint(word1,np.array([0,10,0])),FadeOut(author),run_time = 3)

        self.play(FadeIn(fig01),run_time = 2)
        self.wait(2)
        self.play(FadeOut(fig01),run_time = 2)
        self.wait()

        self.play(FadeIn(fig02),run_time = 2)
        self.wait()
        self.play(FadeOutToPoint(fig02,np.array([0,10,0])),run_time = 2)
        self.wait()

        self.play(Write(word3),run_time = 5)
        self.play(Transform(word3,word4),run_time = 5)
        self.wait()
       
        self.play(FadeOut(word3),run_time = 3)
        self.play(FadeInFromPoint(fig03,np.array([0,-5,0])),run_time = 2)
        self.play(FadeOutToPoint(fig03,np.array([0,10,0])),run_time=2)
        self.wait()

        self.play(FadeIn(word5),run_time =3)
        self.play(Transform(word5,word6),run_time = 5)
        self.wait()
        
        self.play(FadeOut(word5),run_time = 5)
        self.play(FadeIn(fig04),run_time = 2)
        self.play(FadeOut(fig04),run_time=2)
        self.wait()

        self.play(FadeIn(word7),run_time = 5)
        self.play(FadeOut(word7),run_time = 5)
        self.wait()
        self.play(FadeIn(fig05),run_time = 2)
        self.wait()
        self.play(FadeOut(fig05),run_time = 2)
        self.wait()


#不错，但动画时间很难和歌曲时间搭配
#同时，歌曲的添加位置和raster-image的添加位置的不同产生的影响还是得一个个的验证


        


