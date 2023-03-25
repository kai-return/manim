
import scipy.integrate
from manim_learning.manim集中引用 import *


USE_ALMOST_FOURIER_BY_DEFAULT = True
NUM_SAMPLES_FOR_FFT = 1000
DEFAULT_COMPLEX_TO_REAL_FUNC = lambda z : z.real

#上面三个有啥用，不清楚

def 制备傅里叶作图函数(
    axes,time_func,t_min,t_max,
    n_samples = NUM_SAMPLES_FOR_FFT,
    complex_to_real_func = lambda z : z.real,
    color = RED,
    ):
    # N = n_samples
    # T = time_range/n_samples

    """上述为傅里叶级数计算参数？"""

    time_range = float(t_max - t_min)
    time_step_size = time_range/n_samples
    time_samples = np.vectorize(time_func)(np.linspace(t_min, t_max, n_samples))
    #vectorize 函数向量化
    #linespace 用于在线性空间中以均匀步长生成数字序列。

    fft_output = np.fft.fft(time_samples)
    #计算一维离散傅里叶变换。
    #此函数使用高效的快速傅里叶变换 (FFT) 算法计算一维 n-point 离散傅里叶变换 (DFT)。

    frequencies = np.linspace(0.0,n_samples/(2.0*time_range),n_samples//2)
    #//就是除法

    """
    cycles per second of fouier_samples[1]
    (1/time_range)*n_samples
    freq_step_size = 1./time_range"""

    graph = VMobject()
    graph.set_points_smoothly([
        axes.coords_to_point(
            x, complex_to_real_func(y)/n_samples,
        )
        for  x, y in zip(frequencies,fft_output[:n_samples//2])
    ])
    graph.set_color(color)
    f_min, f_max = [
        axes.x_axis.point_to_number(graph.get_points()[i])
        for i in (0, -1)
    ]
    graph.underlying_function = lambda f : axes.y_axis.point_to_number(
        graph.point_from_proportion((f - f_min)/(f_max - f_min))
    )
    return graph

        
def 制备傅里叶变换函数(
    func, t_min, t_max,
    complex_to_real_func = DEFAULT_COMPLEX_TO_REAL_FUNC,
    use_almost_fourier = USE_ALMOST_FOURIER_BY_DEFAULT,
    **keargs ##just eats these  啥意思？
    ):
    scalar = 1./(t_max - t_min) if use_almost_fourier else 1.0
    def 傅里叶变换函数(f):
        z = scalar*scipy.integrate.quad(
            lambda t :func(t)*np.exp(complex(0, -TAU*f*t)),
            t_min, t_max
        )[0]
        return complex_to_real_func(z)
    return 傅里叶变换函数

class TODOStub(Scene):
    def construct(self):
        pass
##这个是干啥用的？留出来的制图空间？

class Introduction(TeacherStudentsScene): #看样子原文件fourier是3b1b制备自己视频的文件了
    def construct(self):
        title = OldTexText("Fourier Transform")
        title.scale(1.2)
        title.to_edge(UP, buff = MED_SMALL_BUFF)

        func = lambda t : np.cos(2*TAU*t) + np.cos(3*TAU*t)
        #用傅里叶级数方法作图？

        graph = FunctionGraph(func, x_min = 0, x_max = 5)
        #functiongraph 是3b1b专门作图的一类class,使用基于lambda的参数方程？

        graph.stretch(0.25, 1)
        graph.next_to(title, DOWN)
        graph.to_edge(LEFT)
        graph.set_color(BLUE)

        fourier_graph = FunctionGraph(
             制备傅里叶变换函数(func, 0, 5),
             x_min = 0, x_max = 5
        )
        #上面的graph不是制备傅里叶作图函数的返回变量？

        fourier_graph.move_to(graph)
        fourier_graph.to_edge(RIGHT)
        fourier_graph.set_color(RED)

        arrow = Arrow(graph, fourier_graph, color = WHITE)
        self.add(title, graph)

        self.student_thinks(
            "What`s that?",
            look_at = title,
            target_mode = "confused",
            index = 1,
        )#看样子3b1b是提前设置好了基础模板参数及变量，再制备视频时直接调用赋值

        self.play(
            GrowArrow(arrow),
            ReplacementTransform(graph.copy(), fourier_graph)
        )

        self.wait(2)
        self.student_thinks(
            "Pssht, I got this",
            target_mode = "tease",
            index = 2,
            added_anims = [RemovePiCreatureBubble(self.students[1])]
        )
        self.play(self.teacher.change, "hesitant")
        self.wait()

class TODOInsertUnmixingSound(TODOStub):
    CONFIG = {
        "message" : "Show unmixing sound"
    }


class otherContexts(PiCreatureScene):
    def construct(self):
        items = VGroup(*list(map(TexText, [
            "Extracting frequencies from soudn",
            "Uncertainty principle",
            "Riemann Zeta function and primes",
            "Differential equations",
        ])))
        items.arrange(
            DOWN, buff = MED_LARGE_BUFF,
            aligned_edge = LEFT
        )
        items.to_corner(UP+LEFT)
        items[1:].set_fill(opacity=0.2)

        morty = self.pi_creature
        morty.to_corner(UP+RIGHT)

        self.add(items)
        for item in items[1:]:
            self.play(
                LaggedStartMap(
                   ApplyMethod, item, 
                   lambda m : (m.set_fill, {"opacity" : 1}),
            ),
            morty.change, "thinkng",
            )
            self.wait()

class TODOInsertCosineWrappingAroundCircle(TODOStub):
    CONFIG = {
        "message" : "Give a pictire-in-picture \\\\ of cosine wrapping around circel",
    }



