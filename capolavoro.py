from manim import *
import numpy as np
import math

class derivative(Scene):
    def construct(self):
        
        x = ValueTracker(0)
        e = ValueTracker(-4)
        dx = ValueTracker(2)
        g = ValueTracker(-4)

        plane = NumberPlane(x_range=[-8, 8, 2], 
                            y_range=[-16, 16, 4], 
                            x_length=5, 
                            y_length=5,
                            background_line_style={
                                "stroke_color": BLUE,
                                "stroke_width": 2,
                                "stroke_opacity": 0.5
                            }).shift(LEFT*4) 
        
        plane2 = NumberPlane(x_range=[-8, 8, 2], 
                            y_range=[-16, 16, 4], 
                            x_length=5, 
                            y_length=5,
                            background_line_style={
                                "stroke_color": BLUE,
                                "stroke_width": 2,
                                "stroke_opacity": 0.5
                            }).shift(RIGHT*4) 
        
        lim = MathTex("\\lim_{dx \\to 0} ", substrings_to_isolate= "dx").next_to(plane,DOWN, buff = 0.2).set_color_by_tex("dx", YELLOW_C)
        
        assi = Axes(
            x_range=[-8, 8, 2],
            y_range=[-16, 16, 4],
            x_length=5,
            y_length=5,
            tips=False,
            axis_config={"color": WHITE},
        ).shift(LEFT*4)
        assi_labels = assi.get_axis_labels(x_label="x", y_label="y")

        assi2 = Axes(
            x_range=[-8, 8, 2],
            y_range=[-16, 16, 4],
            x_length=5,
            y_length=5,
            tips=False,
            axis_config={"color": WHITE},
        ).shift(RIGHT*4)
        assi_labels2 = assi2.get_axis_labels(x_label="x", y_label="y")

        func1 = always_redraw(lambda: assi.plot(lambda x: x**2, x_range=[-4, e.get_value()], color=BLUE_E))
        tang1 = always_redraw(lambda: assi.get_secant_slope_group(x = x.get_value(),
                                                                   graph =func1, 
                                                                   secant_line_length= 3,
                                                                   secant_line_color = TEAL_D,
                                                                   dx_label= MathTex("dx").scale(0.7),
                                                                   dy_label=MathTex("dy").scale(0.7),
                                                                   dy_line_color= GREEN_B,
                                                                    dx = dx.get_value()))
        
        func2 = always_redraw(lambda: assi2.plot(lambda x: 2*x, x_range=[-4, g.get_value()], color=TEAL_D))
        

        dl1 = always_redraw(lambda: DashedLine(assi.coords_to_point(x.get_value(), x.get_value()**2),
                                               assi.coords_to_point(x.get_value(), 0), color=YELLOW_C))
        dl2 = always_redraw(lambda: DashedLine(assi.coords_to_point(x.get_value()+dx.get_value(),   
                                                                    (x.get_value())**2),
                                               assi.coords_to_point(x.get_value()+dx.get_value(), 0), color=YELLOW_C))
        
        dot1 = always_redraw(lambda: Dot().scale(0.7).move_to(assi.coords_to_point(x.get_value(), 
                                                                        x.get_value()**2)))
        dot2 = always_redraw(lambda: Dot().scale(0.7).move_to(assi.coords_to_point(x.get_value()+dx.get_value(), 
                                                                        (x.get_value()+dx.get_value())**2)))
        h = always_redraw(lambda: Line(assi.coords_to_point(x.get_value(),0), 
                                       assi.coords_to_point(x.get_value()+dx.get_value(),0), color=YELLOW_C))
        
        t1 = MathTex("f(x) = x^2").scale(0.8).shift(UP*2.5)
        
        slope_text = always_redraw(lambda : MathTex("f`(").scale(0.8).next_to(t1, DOWN, aligned_edge=LEFT,buff=0.2).shift(LEFT*0.5, DOWN*0.3))
        x_value = always_redraw(lambda : DecimalNumber(num_decimal_places=2).set_value(g.get_value()).scale(0.8).next_to(slope_text, RIGHT).shift(LEFT*0.1))
        slope_text2 = always_redraw(lambda : MathTex(") =").scale(0.8).next_to(x_value, RIGHT, buff=0.1))
        slope_value = always_redraw(lambda : DecimalNumber(num_decimal_places=2).set_value(func2.underlying_function(g.get_value())).scale(0.8).next_to(slope_text2, RIGHT).shift(LEFT*0.1))
        
        der =VGroup(slope_text, x_value, slope_text2, slope_value)
        dot3 = always_redraw(lambda: Dot().scale(0.7).move_to(assi2.coords_to_point(g.get_value(), func2.underlying_function(g.get_value()))))

        self.play(Write(assi), Write(plane))
        self.play(Write(assi_labels))
        self.play(Create(func1))
        self.play(Write(t1))
        self.play(e.animate.set_value(4), run_time=1, rate_func=linear)
        self.wait()
        self.play(Create(tang1),run_time = 1)
        self.play(Write(dot1),Write(dot2), run_time = 1)
        self.play(Create(dl1), Create(dl2), run_time = 1)
        self.play(Create(h), run_time = 1)  
        self.play(x.animate.set_value(2), run_time=3, rate_func=linear)
        self.wait()
        self.play(Write(lim))
        self.play(dx.animate.set_value(0.001), run_time=3, rate_func=linear)
        self.play(Uncreate(dl1), Uncreate(dl2))
        self.play(Unwrite(lim))
        self.wait()
        self.play(x.animate.set_value(-4), run_time=3, rate_func=linear)
        self.wait(1)
        self.play(Write(assi2), Write(plane2))
        self.play(Write(assi_labels2))
        self.play(Write(der))
        self.wait()
        self.play(Create(func2), Create(dot3))
        self.play(g.animate.set_value(4),x.animate.set_value(4), run_time=8, rate_func = smoothererstep)
        self.wait()

class TeoremiRolle(Scene):
    def construct(self):
        

        x = ValueTracker(1)
    
        axis = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 5, 1],
            x_length=5,
            y_length=5,
            tips=False,
            axis_config={"color": WHITE},
        ).scale(1.3).shift(LEFT*3.5)
        axis_labels = axis.get_axis_labels(x_label="x", y_label="y")

        func1 = axis.plot(lambda x: x**3-8*x**2+19*x-10, x_range=[0.73, 4.5], color=MAROON_C)
        func1_label = MathTex("f(x)", color=MAROON_C).next_to(func1.get_end(), RIGHT, buff=0.1)


        #interval
        a = DashedLine(
            axis.coords_to_point(1, 0), 
            axis.coords_to_point(1, func1.underlying_function(1)), 
            color=YELLOW_C)
        a_label = MathTex("a").scale(0.7).next_to(a, DOWN, buff=0.3).set_color(RED_B)
        b = DashedLine(axis.coords_to_point(4, 0), axis.coords_to_point(4,func1.underlying_function(4)), color=YELLOW_C) 
        b_label = MathTex("b").scale(0.7).next_to(b, DOWN, buff=0.3).set_color(PURPLE_B)

        #tangent
        tan = always_redraw(
            lambda: axis.get_secant_slope_group(
                x= x.get_value(),
                graph=func1,
                dx=0.01,
                secant_line_length=3,
                secant_line_color=BLUE_C,
                dx_label=MathTex("dx").scale(0.7),
                dy_label=MathTex("dy").scale(0.7),
                dy_line_color=GREEN_B,
            )
        )
        
        #conditions
        
        cond_cont = MathTex(r"1)\:a,b\in \mathbb{D}:\forall x_0\in [a,b],\lim_{x \to x_0}f(x)= f(x_0)").shift(RIGHT*3,UP*2)
        cond_der = MathTex(r"2)\:a,b\in\mathbb{D}: \forall{x_0}\in]a,b[, f'_-(x_0) = f'_+(x_0)").next_to(cond_cont, DOWN, buff=0.5, aligned_edge=LEFT)
        cond_rol = MathTex(r"3)\:a,b\in\mathbb{D}: f(a) = f(b)").next_to(cond_der, DOWN, buff=0.5, aligned_edge=LEFT)
        conditions = VGroup(cond_cont, cond_der, cond_rol).scale(0.6)
        
          
        #cs
        dot = always_redraw(lambda: Dot(axis.coords_to_point(x.get_value(),func1.underlying_function(x.get_value())), color=TEAL_D))
        c1 = Dot(axis.coords_to_point(1.78,0), color=TEAL_D)
        c2 = Dot(axis.coords_to_point(3.55,0), color=TEAL_D)
        c1_line = DashedLine(axis.coords_to_point(1.78,0), axis.coords_to_point(1.78,func1.underlying_function(1.78)), color=TEAL_D)
        c2_line = DashedLine(axis.coords_to_point(3.5485,0), axis.coords_to_point(3.5485,func1.underlying_function(3.5485)), color=TEAL_E)
        c1_label = MathTex(r"c_1").scale(0.7).next_to(c1, DOWN, buff=0.2).set_color(TEAL_D)
        c2_label = MathTex(r"c_2").scale(0.7).next_to(c2, DOWN, buff=0.2).set_color(TEAL_E)
        

        self.play(Write(axis), Write(axis_labels))
        self.play(Create(func1), Write(func1_label))
        self.play(Create(a), Write(a_label))
        self.play(Create(b), Write(b_label))
        self.play(Create(dot), Create(tan), run_time = 2)
        self.wait()
        self.play(Write(conditions), run_time = 4)
        self.wait()

    
        self.play(ApplyMethod(conditions.shift, UP*1.85,RIGHT*0.95))
        self.wait()
        
        rect_cond = always_redraw(lambda: SurroundingRectangle(conditions, buff=0.2, corner_radius=0.2).set_color([TEAL_B,ORANGE]))
        arrow = always_redraw(lambda: MathTex(r"\Downarrow").next_to(conditions, DOWN, buff=0.5))
        thesis = always_redraw(lambda: MathTex(r"\exists{c}\in]a,b[\::f'(c) =0").next_to(arrow, DOWN, buff=0.2).scale(0.8))
        
        self.play(Create(rect_cond), Create(arrow), Create(thesis))
        self.wait(3)

        #der
        func_tex = MathTex(r"f(x) =x^3 -8x^2 +19x -10").scale(0.8).next_to(thesis, DOWN, buff=0.5)
        der = MathTex("f'(x) = 3x^2 -16x +19").scale(0.8).next_to(func_tex, DOWN, buff=0.5)
        der0 = MathTex(r"f(c) = 3c^2 -16c +19 = 0",substrings_to_isolate="c").set_color_by_tex("c",TEAL_D).scale(0.8).next_to(der, DOWN, buff=0.5)
       
        
        self.play(x.animate.set_value(4), run_time=4, rate_func=smooth)
        self.wait()
        self.play(x.animate.set_value(1), run_time=4, rate_func=smooth)
        self.wait(2)
        self.play(x.animate.set_value(1.78), run_time=2, rate_func=smooth)
        self.play(Create(c1), Create(c1_line), Write(c1_label),run_time = 2)
        self.wait()
        self.play(x.animate.set_value(3.5485), run_time=3, rate_func=smooth)
        self.play(Create(c2), Create(c2_line), Write(c2_label))
        self.wait()
        self.play(Write(func_tex), Write(der), Write(der0))
        self.wait(3)

class TeoremiLagrange(Scene):
    def construct(self):
        
        #assi
        a = ValueTracker(-1)
        b = ValueTracker(1)
        c = ValueTracker(1)
        d= ValueTracker(1)
        e = ValueTracker(1)
        
        axis = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 5, 1],
            x_length=5,
            y_length=5,
            tips=False,
            axis_config={"color": WHITE},
        ).scale(1.3).shift(LEFT*3.5)
        axis_labels = axis.get_axis_labels(x_label="x", y_label="y")

        #funzione
        func1= always_redraw(lambda:axis.plot(lambda x: 
                                            1/2*(a.get_value()*(x-1)**3 
                                            +b.get_value()*(x-1)**2 
                                            +c.get_value()*(x-1) 
                                            +d.get_value()),
                                            x_range=[-1,3.5]
                                            ).set_color(MAROON_C))
        
        
        a_point = always_redraw(lambda:Dot(axis.coords_to_point(1,func1.underlying_function(1))).set_color(TEAL_C))
        b_point = always_redraw(lambda: Dot(axis.coords_to_point(3,func1.underlying_function(3))).set_color(TEAL_C))
        a_line = always_redraw(lambda: DashedLine(axis.coords_to_point(1,0), a_point.get_center()).set_color(TEAL_C))
        b_line = always_redraw(lambda: DashedLine(axis.coords_to_point(3,0), b_point.get_center()).set_color(TEAL_C))
        a_label= MathTex("a").next_to(axis.coords_to_point(1,0),DOWN).scale(0.7).set_color(TEAL_C)
        b_label= MathTex("b").next_to(axis.coords_to_point(3,0),DOWN).scale(0.7).set_color(TEAL_C)

        #secante a-b
        tang1 = always_redraw(lambda: axis.plot(
            lambda x: (
                (func1.underlying_function(3)-func1.underlying_function(1))*x)/2 + 
                func1.underlying_function(1) -
                (func1.underlying_function(3)-
                 func1.underlying_function(1))/2,
                 x_range=[0,4],
                 ).set_color([TEAL_B,GREEN_B]))
        
        #derivata
        tang2 = always_redraw(lambda: axis.plot(
            lambda x: 
                ((3*a.get_value()*(e.get_value()-1)**2)/2 +b.get_value()*(e.get_value()-1) + c.get_value()/2)*x +
                func1.underlying_function(e.get_value())-
                e.get_value()*((3*a.get_value()*(e.get_value()-1)**2)/2 +b.get_value()*(e.get_value()-1) + 
                c.get_value()/2),
                x_range=[e.get_value()-2,e.get_value()+2]
                ).set_color([BLUE_E, TEAL_B]))
        tang2_label = always_redraw(lambda: MathTex(r"f'(x)"
                                                    ).next_to(tang2.get_end(),DOWN).scale(0.6).set_color([BLUE_E, TEAL_B])
                                    )
        

        p1 = (6*a.get_value()-2*b.get_value() - ((-6*a.get_value() +2*b.get_value())**2 -4*(3*a.get_value())*(3*a.get_value() -
        2*b.get_value()+c.get_value() +func1.underlying_function(1) - func1.underlying_function(3)))**(1/2))/(6*a.get_value())
        

        c_dot = always_redraw(lambda: Dot(tang2.get_center()).set_color([BLUE_E, TEAL_B])) 
        c_line = always_redraw(lambda: DashedLine(tang2.get_center(), axis.coords_to_point(e.get_value(),0)).set_color([BLUE_E, TEAL_B]))
        c_label = always_redraw(lambda: MathTex('c').next_to(axis.coords_to_point(e.get_value(),0), DOWN).set_color([BLUE_E, TEAL_B]).scale(0.7))

        #conditions
        cond_cont = MathTex(r"1)\:a,b\in \mathbb{D}:\forall x_0\in [a,b],\lim_{x \to x_0}f(x)= f(x_0)").shift(RIGHT*3,UP*2)
        cond_der = MathTex(r"2)\:a,b\in\mathbb{D}: \forall{x_0}\in]a,b[, f'_-(x_0) = f'_+(x_0)").next_to(cond_cont, DOWN, buff=0.5, aligned_edge=LEFT)

        conditions = VGroup(cond_cont, cond_der).scale(0.6)

        rect_cond = always_redraw(lambda: SurroundingRectangle(conditions, buff=0.2, corner_radius=0.2).set_color([TEAL_B,ORANGE]))
        arrow = always_redraw(lambda: MathTex(r"\Downarrow").next_to(conditions, DOWN, buff=0.5))
        thesis = always_redraw(lambda: MathTex(r"\exists{c}\in]a,b[:{}f'(c)=\frac{f(b) - f(a)}{b-a}").next_to(arrow, DOWN, buff=0.2).scale(0.8))

        #self.add(axis_labels, axis, a_point, b_point, func1, tang1, a_line, b_line, tang2, c_dot, c_line,tang2_label, tang1_label)
        self.play(Create(axis), Create(axis_labels))
        self.play(Create(func1), Create(tang1), Create(tang2), Write(tang2_label))
        self.play(Create(a_line),Create(b_line), Write(a_label), Write(b_label), Create(a_point), Create(b_point))
        self.wait()
        self.play(Create(c_dot), Create(c_line), Write(c_label))
        self.wait()
        self.play(Write(conditions))
        self.play(Create(rect_cond))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        self.play(Create(arrow), Create(thesis))
        self.wait()
        self.play(e.animate.set_value(p1),run_time = 3)
        self.wait()
        self.play(e.animate.set_value(1), run_time = 3)
        self.wait()
        self.play(a.animate.set_value(-1/2),d.animate.set_value(4),c.animate.set_value(1),b.animate.set_value(1/2))
        self.wait()
        self.play(e.animate.set_value(p1), run_time = 3)
        self.wait()
        self.play(e.animate.set_value(1), run_time=  3)
        self.wait()
        self.play(a.animate.set_value(0),b.animate.set_value(1),c.animate.set_value(1),d.animate.set_value(1), run_time =2)
        self.wait()
        

        p2 = (func1.underlying_function(3)- func1.underlying_function(1) -c.get_value() +2*b.get_value())/(2*b.get_value())
        
        self.play(e.animate.set_value(p2),run_time = 3)
        self.wait()
        
class TeoremiLagrange_Proof(Scene):
    def construct(self):
        big_f = MathTex(r"F(x) = f(x) -kx").shift(UP*3)  
        rolle_conditions = MathTex(r"F(a) = F(b)").shift(UP*1)
        rolle_conditions2= MathTex(r"f(a) -ka =f(b) -kb").next_to(rolle_conditions, DOWN, buff = 0.5)
        rolle_conditions3 = MathTex(r"k = \frac{f(b)-f(a)}{b-a}").next_to(rolle_conditions2, DOWN, buff = 0.5)
        big_f2= MathTex(r"F(x) = f(x) -\frac{f(b)-f(a)}{b-a}x").shift(UP*3)
        derivative = MathTex(r"F'(x) = f'(x) -\frac{f(b)-f(a)}{b-a}").next_to(big_f2,DOWN, buff = 0.7)
        der =derivative.copy()
        rolle = MathTex(r"F'(c) = f'(c) -\frac{f(b)-f(a)}{b-a}=0").next_to(derivative,DOWN,buff =0.7 )
        rol = rolle.copy()
        lagrange = MathTex(r"f'(c) = \frac{f(b)-f(a)}{b-a}").next_to(rolle,DOWN,buff = 0.7)

        
        self.play(Write(big_f))
        self.wait()
        self.play(Write(rolle_conditions))
        self.wait()
        self.play(Write(rolle_conditions2))
        self.wait()
        self.play(Write(rolle_conditions3))
        self.wait()
        self.play(Indicate(big_f[0][10]), Indicate(rolle_conditions3[0][0]))
        self.play(ReplacementTransform(big_f,big_f2))
        self.wait()
        self.play(Unwrite(rolle_conditions), Unwrite(rolle_conditions2), Unwrite(rolle_conditions3))
        self.wait()
        self.play(Write(derivative))
        self.wait()
        self.play(Transform(der,rolle))
        self.wait()
        self.play(Transform(rol,lagrange))
        self.wait()

class integral(Scene):
    def construct(self):

        # Value trackers
        h = ValueTracker(3)

        #Creare gli assi
        axis = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 7, 1],
            x_length=5,
            y_length=5,
            tips=False,
            axis_config={"color": WHITE},
        ).shift(LEFT*3.5)
        axis_labels = axis.get_axis_labels(x_label="x", y_label="y")

        #Creare le linee tratteggiate
        a = DashedLine(
            axis.coords_to_point(1, 0), 
            axis.coords_to_point(1, 9/4), 
            color=YELLOW_C)
        a_label = MathTex("a").scale(0.7).next_to(a, DOWN, buff=0.2).set_color(RED_B)
        b = DashedLine(axis.coords_to_point(4, 0), axis.coords_to_point(4,3), color=YELLOW_C) 
        b_label = MathTex("b").scale(0.7).next_to(b, DOWN, buff=0.2).set_color(PURPLE_B)

        #Creare la funzione
        func1 = axis.plot(
            lambda x: ((x-3)*(x-1)*(x-3)+ 9)/4, x_range=[0, 5], color=MAROON_C
            )
        func1_label = MathTex(
            "f(x)", color=MAROON_C
            ).next_to(func1.get_end(), RIGHT, buff=0.1)

        #Creare i rettangoli di Riemann e la vera area sotto la funzione
        rienmann = always_redraw(
            lambda : axis.get_riemann_rectangles(
            graph = func1, 
            fill_opacity=0.75, 
            stroke_width=0.5,
            x_range=[1, 4],
            dx = h.get_value()
            ).set_color_by_gradient(RED_C, PURPLE_C)
            )
        real_area = axis.get_area(
            func1,
            x_range = [1, 4],
            color = [RED_C, PURPLE_C],
        )
        
        #Creare la lunghezza e l'altezza dei rettangoli
        length = always_redraw(
            lambda: Line(
                axis.coords_to_point(1, 0), 
                axis.coords_to_point(1 + h.get_value(), 0), 
                color=YELLOW_C)
                )
        length_brace = always_redraw(
            lambda: Brace(
                length, direction=DOWN, buff=0.1, sharpness= 0.5
                ).scale(0.7)
                )
        
        length_label = always_redraw(
            lambda: MathTex(r" \boldsymbol{\Delta x}").scale(0.7).next_to(length_brace, DOWN, buff=0.1)
            )
        
        l = VGroup(length, length_brace, length_label)

        height_brace = Brace(
            a, direction=LEFT, buff=0.1, sharpness= 0.5
            ).scale(0.7)
        height_label = MathTex(r"\boldsymbol{f(x)}").scale(0.7).next_to(height_brace, LEFT, buff=0.1)
        

        #Creare le formule
        delta_x = MathTex(
            r"\Delta x = \frac{b-a}{i}").scale(0.8).shift(UP*2.5, LEFT*3.5)
        xi = MathTex(r"x_i = a +i\Delta x").scale(0.8).next_to(delta_x, DOWN, buff=0.5)
        area1 = MathTex(r"A\approx\sum_{i}^{}A_{ir}=\sum_{i}^{}f(x_i)\Delta x").shift(RIGHT*3.8,UP*1).scale(0.8)
        area2 = MathTex(r"A =\lim_{n \to +\infty}  \sum_{i}^{n }f(x_i)\Delta x=").next_to(area1, DOWN, buff =0.3).shift(LEFT*1.2).scale(0.8)
        integral = MathTex(r"\int_{a}^{b}f(x)dx").next_to(area2, RIGHT).next_to(area2, buff = -0.1).scale(0.8)

        i_label = MathTex(r"i = ").next_to(area1, UP, buff=1).shift(LEFT*0.5)
        
        
        i =always_redraw(
            lambda: DecimalNumber(
                num_decimal_places=0
                ).set_value(3/h.get_value()).scale(0.7).next_to(i_label, RIGHT, buff=0.2))
        
        i_inf = MathTex(r"\infty").scale(0.7).next_to(i_label, RIGHT, buff=0.2)
        
        
        
        #colors 
        delta_x[0][3].set_color(PURPLE_B)
        delta_x[0][5].set_color(RED_B)
        xi[0][3].set_color(RED_B)
        integral[0][1].set_color(PURPLE_B)
        integral[0][2].set_color(RED_B)



        self.play(Write(axis), Write(axis_labels))
        self.play(Create(func1), Write(func1_label))
        self.play(Create(a), Write(a_label))
        self.play(Create(b), Write(b_label))
        self.wait()
        self.play(DrawBorderThenFill(rienmann))
        self.play(Create(l), Create(height_brace), Write(height_label), run_time = 2)
        self.wait(2)
        self.play(Write(area1), Write(i), Write(i_label))
        self.play(h.animate.set_value(1), run_time=2, rate_func= smooth)
        self.play(Write(delta_x), Write(xi))
        self.wait(3)
        self.play(h.animate.set_value(0.1), run_time=2, rate_func= smooth)
        self.wait(3)
        self.play(h.animate.set_value(0.01), run_time=2, rate_func= smooth)
        self.wait(3)
        self.play(FadeOut(rienmann),FadeIn(real_area), ReplacementTransform(i, i_inf), run_time=2)
        self.play(Write(area2), Unwrite(l), Unwrite(height_brace), Unwrite(height_label))
        self.wait()
        self.play(Write(integral))
        self.wait(3)
        

        self.add(area2, integral)
        #self.play(Indicate(area3[0][2]), Indicate(a_label))
        #self.play(Indicate(area3[0][1]), Indicate(b_label))

