from manimlib import *
import numpy as np 

class Surface(ThreeDScene):
    def construct(self):
        self.add_sound("F:\programming\python\\new_manim\manim\manim-sound\所念皆星河.mp3")
        surface_text= Text("可以使用surfaces来展示3d景色，并将平面图改为3d图",font='KaiTi')
        surface_text.fix_in_frame()#  将字体纳入整体模型中，具体信息不知
        surface_text.to_edge(UP)#将元素放置在上端边缘（0，1，0）
        self.add(surface_text)
        self.wait(0.1) #单位是秒，

        torus1 = Torus(r1=1,r2=1)
        torus2 = Torus(r1=3,r2=1)
        sphere = Sphere(radius=3,resolution=torus1.resolution)
        #torus 三维环形，甜甜圈形状,环面，具体参数因不清楚环面的数学构建无法理解
        #sphere 球面
        #resolution -the number of samples taken of the Sphere. A tuple can be used to define different resolutions for u and v respectively.
        #这个resolution具体是干啥的不清楚，采样？

        """
        3b1b原始文件中的介绍
        # You can texture（使得某个物体具有某种结构和特征） a surface with up to two images, which will
        # be interpreted as the side towards the light, and away from
        # the light.（一张图片对光，一张远离光）  These can be either urls, or paths to a local file
        # in whatever you've set as the image directory in
        # the custom_config.yml file

        # day_texture = "EarthTextureMap"
        # night_texture = "NightEarthTextureMap"
        """

        night_texture = "F:\programming\python\\new_manim\manim\manim-raster\\beauty01.jpg"
        day_texture = "F:\programming\python\\new_manim\manim\manim-raster\\beauty02.jpg"

        surfaces = [
            TexturedSurface(surface,day_texture,night_texture)
            for surface in [sphere,torus1,torus2]
        ]
        """texturesurface曲面贴图---文档里的介绍都不全"""
        for mob in surfaces:
            mob.shift(IN)
            mob.mesh = SurfaceMesh(mob)
            mob.mesh.set_stroke(BLUE,1,opacity=0.5)
        """
        surfacemesh 表面网格，传入一个关于U,V的参数方程
        resolution:分割精度
        """
        surface = surfaces[0]

        self.play(
             FadeIn(surface),
             ShowCreation(surface.mesh,lag_ratio=0.01,run_time = 3)#单位应该是秒
        )
        for mob in surfaces:
            mob.add(mob.mesh)
        surface.save_state()#还能保存所用的表面？
        #mob应该是构建表面网格的，但是具体逻辑不清楚
        self.play(Rotate(surface,PI/2),run_time=2)#旋转特效？
        for mob in surfaces[1:]:
            mob.rotate(PI/2)
        
        self.play(
            Transform(surface,surfaces[1]),
            run_time=3#表面转换？从球体换成环面？
        )
        
        self.play(
            Transform(surface,surfaces[2]),
            #move camera frame during the transition(转换) 转移摄像头角度？
            self.frame.animate.increment_phi(-10 *DEGREES),
            self.frame.animate.increment_theta(-20*DEGREES),
            run_time = 3
        )
        #add ambient rotation 添加环境旋转,难不成这就是成型的元素的界面操作？
        self.frame.add_updater(lambda m,dt:m.increment_theta(-0.1*dt))

        #play around with the light is 
        light_text = Text("可以移动光源",font="KaiTi")
        light_text.move_to(surface_text)
        light_text.fix_in_frame()

        self.play(FadeTransform(surface_text,light_text))#这步才是球体到环面的转换？
        light= self.camera.light_source
        self.add(light)
        light.save_state()
        self.play(light.animate.move_to(3*IN),run_time=5)
        self.play(light.animate.shift(10*OUT),run_time = 5)

        drag_text = Text("可以通过按压d或者f键并同时移动鼠标的方式操作界面",font="KaiTi")
        drag_text.move_to(light_text)
        drag_text.fix_in_frame()

        self.play(FadeTransform(light_text,drag_text))
        self.wait()

       

    