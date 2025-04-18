from manim import *

class heat_equation(ThreeDScene):
    def construct(self):

        assi = ThreeDAxes(
            x_range=[0, 4.5, 1],
            y_range=[0, 2, 1],
            z_range=[-5, 5, 1],
            axis_config={"color": WHITE},
        ).scale(0.6)

        assi1 = assi.copy().move_to(2* OUT).rotate(-10*DEGREES, axis = LEFT).scale(0.5)
        assi2 = assi1.copy().shift(LEFT*4.1).rotate(10* DEGREES, axis = OUT)
        assi3 = assi1.copy().shift(RIGHT*4.4).rotate(-11*DEGREES, axis = OUT)


        x_label = always_redraw(lambda: assi.get_x_axis_label("x",  buff=0.1).scale(0.7).rotate(PI/2, axis = RIGHT))
        y_label = always_redraw(lambda: assi.get_y_axis_label("t", buff=0.1, rotation = 0).scale(0.7))
        z_label = always_redraw(lambda: assi.get_z_axis_label("T(x,t)",  buff=0.1).scale(0.7))

        axis_labels = VGroup(x_label, y_label, z_label)
        
        
        N_TERMS = 4
        L = 2

        def temperature(x, t_val):
            total = 0
            for n in range(1, N_TERMS + 1):
                A_n = 1 / n
                term = 2*A_n * np.sin(n *PI* x / L) * np.exp(-(n *PI/ L)**2 * t_val)
                total += term
            return total

        t = ValueTracker(0)

        
        slicer1 = ParametricFunction(lambda u:assi2.c2p(
            u,0,2* np.sin(1*PI*u/ L)),
            t_range= [0,4]).set_color_by_gradient([BLUE, RED]) 
        
        slicer2 = ParametricFunction(lambda u:assi1.c2p(
            u,0,np.sin(2*PI*u/ L)),
            t_range= [0,4]).set_color_by_gradient([BLUE, RED])  
        
        slicer3 = ParametricFunction(lambda u:assi3.c2p(
            u,0,2/3 * np.sin(3*PI*u/ L)),
            t_range= [0,4]).set_color_by_gradient([BLUE, RED])  
        
        
        slicers = VGroup(slicer1, slicer2, slicer3)
        
        
        self.set_camera_orientation(theta= -90 * DEGREES, phi = 90* DEGREES)
        self.wait()
        self.play(Create(assi), Create(axis_labels))
        self.wait()    
        self.play(assi.animate.move_to(-1.7* OUT).scale(0.5))
        self.wait(1)
        self.play(Create(assi1), Create(assi2), Create(assi3))
        self.wait()
        self.play(Create(slicers), run_time=3)
        
        slicer = always_redraw(lambda : ParametricFunction(lambda u: assi.c2p(
            u, t.get_value(), temperature(u,t.get_value())),
            t_range = [0, 4]).set_color_by_gradient([BLUE, RED]))
        
        slicers_t = slicers.copy()

        self.play(Create(slicer))
        self.play(ReplacementTransform(slicers_t,slicer))
        self.wait()
        self.wait(2)
        self.play(Uncreate(assi1), Uncreate(assi2), Uncreate(assi3), Uncreate(slicers))
        self.wait()

        self.play(assi.animate.move_to(ORIGIN).scale(2))
        self.wait()
        self.move_camera(phi=80* DEGREES,theta=-80 * DEGREES,run_time=2)

        surface = always_redraw(lambda: Surface(
            lambda u,v: assi.c2p(u,v,temperature(u, v)),
            u_range=[0, 4],
            v_range=[0, 2],  # dummy variable
            fill_opacity=0.1,
            stroke_color= WHITE,
            stroke_width= 0.1).set_color(WHITE))
        
        self.play(Create(surface), run_time=2)
        self.wait()
        self.play(t.animate.set_value(2), run_time=4, rate_func=linear)
        self.wait(2)

class FourierBuildUpWithLabel(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-PI, PI, PI/2],
            y_range=[-PI, PI, PI/2],
            x_length=6,
            y_length=6,
            axis_config={"include_tip": False},
        ).to_edge(LEFT)

        labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.add(axes, labels)

        # Original function f(x) = x
        original = axes.plot(lambda x: x, color=MAROON_C, x_range=[-PI, PI])
        original_label = MathTex("f(x) = x").next_to(original.get_end(), UP).set_color(MAROON_C).scale(0.6)
        self.play(Create(original), Write(original_label))
        self.wait()

        # Add the general Fourier formula
        formula = MathTex(
            r"f(x) = \sum_{n=1}^{\infty} \frac{2(-1)^{n+1}}{n} \sin(nx)",
            font_size=36
        ).to_corner(UR).shift(DOWN * 0.5, LEFT * 0.5)
        
        #colors
        formula[0][7].set_color(BLUE)
        formula[0][15].set_color(BLUE)
        formula[0][19].set_color(BLUE)
        formula[0][24].set_color(BLUE)
        formula[0][25].set_color(MAROON_C)
        formula[0][0].set_color(MAROON_C)
        formula[0][1].set_color(MAROON_C)
        formula[0][2].set_color(MAROON_C)
        formula[0][3].set_color(MAROON_C)


        # General Fourier series and coefficients (MathTex block)
        fourier_block = VGroup(
            MathTex(
                r"f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left( a_n \cos(nx) + b_n \sin(nx) \right)",
                font_size=30
            ),
            MathTex(
                r"a_0 = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x)\,dx",
                font_size=28
            ),
            MathTex(
                r"a_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x)\cos(nx)\,dx",
                font_size=28
            ),
            MathTex(
                r"b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x)\sin(nx)\,dx",
                font_size=28
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        # Put it in a rectangle and position in bottom-right
        rect = SurroundingRectangle(fourier_block, color=WHITE, buff=0.4)
        fourier_box = VGroup(rect, fourier_block).to_corner(DR)

        # Animate appearance
        self.play(Write(fourier_box))

            
        self.play(Write(formula))           
        self.wait()

        # Initial sum function (zero)
        def zero_func(x): return 0
        cumulative = zero_func
        graph = axes.plot(cumulative, color=BLUE, x_range=[-PI, PI], stroke_width=3)
        self.add(graph)

        N_max = 6
        for n in range(1, N_max + 1):
            coef = 2 * (-1) ** (n + 1) / n
            new_term = lambda x, n=n, coef=coef: coef * np.sin(n * x)
            updated_cumulative = lambda x, cumulative=cumulative, new_term=new_term: cumulative(x) + new_term(x)

            # Plot current yellow term
            yellow_term_graph = axes.plot(new_term, x_range=[-PI, PI], color=YELLOW, stroke_opacity=0.7)
            self.play(Create(yellow_term_graph), run_time=0.8)

            # Plot new cumulative sum
            new_graph = axes.plot(updated_cumulative, color=BLUE, x_range=[-PI, PI], stroke_width=3)

            # Animate blue + yellow → new blue
            self.play(
                ReplacementTransform(graph, new_graph),
                ReplacementTransform(yellow_term_graph, new_graph),
                run_time=1.2
            )
            self.remove(graph)
            graph = new_graph
            cumulative = updated_cumulative
            self.wait(0.3)

        self.wait(2)
