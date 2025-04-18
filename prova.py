from manim import *

class DerivativeGraph(Scene):
    def construct(self):
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

        func1= always_redraw(lambda:axis.plot(lambda x: 
                                            1/2*(a.get_value()*(x-1)**3 
                                            +b.get_value()*(x-1)**2 
                                            +c.get_value()*(x-1) 
                                            +d.get_value()),
                                            x_range=[-1,3]
                                            ).set_color(MAROON_C))
        
        
        a_point = always_redraw(lambda:Dot(axis.coords_to_point(1,func1.underlying_function(1))).set_color(TEAL_C))
        b_point = always_redraw(lambda: Dot(axis.coords_to_point(3,func1.underlying_function(3))).set_color(TEAL_C))
        a_line = always_redraw(lambda: DashedLine(axis.coords_to_point(1,0), a_point.get_center()).set_color(TEAL_C))
        b_line = always_redraw(lambda: DashedLine(axis.coords_to_point(3,0), b_point.get_center()).set_color(TEAL_C))
        a_label= MathTex("a").next_to(axis.coords_to_point(1,0),DOWN).scale(0.7).set_color(TEAL_C)
        b_label= MathTex("b").next_to(axis.coords_to_point(3,0),DOWN).scale(0.7).set_color(TEAL_C)

        tang1 = always_redraw(lambda: axis.plot(
            lambda x: (
                (func1.underlying_function(3)-func1.underlying_function(1))*x)/2 + 
                func1.underlying_function(1) -
                (func1.underlying_function(3)-
                 func1.underlying_function(1))/2,
                 x_range=[0,4],
                 ).set_color([TEAL_B,GREEN_B]))
        tang1_label = always_redraw(lambda:MathTex(r"\frac{f(b) - f(a)}{b-a}"

        ).next_to(tang1.get_end(),DOWN,buff = -0.2).scale(0.6).set_color([TEAL_B,GREEN_B]))

        tang2 = always_redraw(lambda: axis.plot(
            lambda x: 
                ((3*a.get_value()*(e.get_value()-1)**2)/2 +b.get_value()*(e.get_value()-1) + c.get_value()/2)*x +
                func1.underlying_function(e.get_value())-
                e.get_value()*((3*a.get_value()*(e.get_value()-1)**2)/2 +b.get_value()*(e.get_value()-1) + 
                c.get_value()/2),
                x_range=[0,4]
                ).set_color([BLUE_E, TEAL_B]))
        tang2_label = always_redraw(lambda: MathTex(r"f'(x)"
                                                    ).next_to(tang2.get_end(),DOWN).scale(0.6).set_color([BLUE_E, TEAL_B])
                                    )
        


        cond_cont = MathTex(r"1)\:a,b\in \mathbb{D}:\forall x_0\in [a,b],\lim_{x \to x_0}f(x)= f(x_0)").shift(RIGHT*3,UP*2)
        cond_der = MathTex(r"2)\:a,b\in\mathbb{D}: \forall{x_0}\in]a,b[, f'_-(x_0) = f'_+(x_0)").next_to(cond_cont, DOWN, buff=0.5, aligned_edge=LEFT)

        conditions = VGroup(cond_cont, cond_der).scale(0.6)

        rect_cond = always_redraw(lambda: SurroundingRectangle(conditions, buff=0.2, corner_radius=0.2).set_color([TEAL_B,ORANGE]))
        arrow = always_redraw(lambda: MathTex(r"\Downarrow").next_to(conditions, DOWN, buff=0.5))
        thesis = always_redraw(lambda: MathTex(r"\exists{c}\in]a,b[:{}f'(c)=\frac{f(b) - f(a)}{b-a}").next_to(arrow, DOWN, buff=0.2).scale(0.8))
        
        self.add(axis, axis_labels, func1, a_line,a_point,b_line,b_point,tang1,tang1_label,tang2,tang2_label,a_label,b_label, conditions, rect_cond,arrow, thesis)

class Prova(Scene):
    def construct(self):
        x_0 = ValueTracker(1.8)
        epsilon = ValueTracker(0.1)
        
        axis = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 5, 1],
            x_length=5,
            y_length=5,
            tips=False,
            axis_config={"color": WHITE},
        ).scale(1.3).shift(LEFT*3.5)
        axis_labels = axis.get_axis_labels(x_label="x", y_label="y")

        func = axis.plot(lambda x: -(x-2)**2 +4 , x_range = [0,4]).set_color(MAROON_C)
       
        x_label = always_redraw(lambda: MathTex('x_0').next_to(axis.coords_to_point(x_0.get_value(),0),DOWN).scale(0.5))
        x_dl = always_redraw(lambda: MathTex(r'x_0 - \delta').next_to(axis.coords_to_point(2 - (4 - func.underlying_function(x_0.get_value()) -epsilon.get_value())**(1/2),0),DOWN,buff= 0).scale(0.5))
        x_dr = always_redraw(lambda: MathTex(r'x_0 + \delta').next_to(axis.coords_to_point(2 + (4 - func.underlying_function(x_0.get_value()) -epsilon.get_value())**(1/2), 0),DOWN,buff= 0).scale(0.5))
        
        y_label = always_redraw(lambda: 
                                MathTex('l').next_to(
                                    axis.coords_to_point(
                                        0,func.underlying_function(x_0.get_value())),
                                        LEFT).set_color(YELLOW_B).scale(0.5))
        
    
        f_x_e = always_redraw(lambda: 
                              DashedLine(
                                  axis.coords_to_point(
                                      0,func.underlying_function(x_0.get_value()) - epsilon.get_value()), 
                                      axis.coords_to_point(
                                          2 - (4 - func.underlying_function(x_0.get_value()) -epsilon.get_value())**(1/2),func.underlying_function(x_0.get_value()) - epsilon.get_value()
                                          )).set_color(BLUE_E)
                                          )
        

        f_y_e = always_redraw(lambda: DashedLine(
                                        axis.coords_to_point(
                                            0,func.underlying_function(x_0.get_value()) +epsilon.get_value()), 
                                            axis.coords_to_point(
                                                2 + (4 - func.underlying_function(x_0.get_value()) -epsilon.get_value())**(1/2),func.underlying_function(x_0.get_value()) +epsilon.get_value()
                                            )
                                            ).set_color(TEAL_E))
        
        dot2_line = always_redraw(lambda: DashedLine(
            axis.coords_to_point(
                2 + (4 - func.underlying_function(x_0.get_value()) -epsilon.get_value())**(1/2)),
                f_y_e.get_end()).set_color(TEAL_E))

        dot1_line = always_redraw(lambda: DashedLine(
            axis.coords_to_point(
                2 - (4 - func.underlying_function(x_0.get_value()) -epsilon.get_value())**(1/2)),
                f_x_e.get_end()).set_color(BLUE_E))

        
        func_x_line = always_redraw(lambda: DashedLine(
            axis.coords_to_point(x_0.get_value(), func.underlying_function(x_0.get_value())),
            axis.coords_to_point(x_0.get_value(),0)
        ).set_color(YELLOW_B))
        func_y_line = always_redraw(lambda: DashedLine(
            axis.coords_to_point(x_0.get_value(), func.underlying_function(x_0.get_value())),
            axis.coords_to_point(0,func.underlying_function(x_0.get_value()))
        ).set_color(YELLOW_B))

        #area_x = always_redraw(lambda: 
        #                       axis.get_area(func, 
        #                                     x_range=[x_0.get_value()-delta.get_value(),
        #                                              x_0.get_value()+delta.get_value()],
        #                                     opacity= 0.3).set_color([TEAL_B,MAROON_C]))
        
        horizontal_line = always_redraw(lambda: 
                                     axis.plot(lambda x: 2, x_range=[0,2]))
        bounded_line = always_redraw(lambda:
                                     axis.plot(lambda x: 1))
        #area_y = always_redraw(lambda: 
        #                       axis.get_area(graph =horizontal_line,
       #                                     bounded_graph= bounded_line
        #                                     
        #                           
        #                       ))
        #p = 2-(func.underlying_function())

        self.add(axis,axis_labels,func,dot1_line,
                 dot2_line,x_label,x_dl,x_dr,y_label,
                 f_x_e,f_y_e,func_x_line,func_y_line)
        
class Limiti2(Scene):
    def construct(self):
        
        epsilon = ValueTracker(0.9)
        x_0 = ValueTracker(1)
        dx = ValueTracker(0)
        
        axis = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 5, 1],
            x_length=5,
            y_length=5,
            tips=False,
            axis_config={"color": WHITE},
        ).scale(1.3).shift(LEFT*3.5)
        axis_labels = axis.get_axis_labels(x_label="x", y_label="y")

        function = axis.plot(lambda x: -x**2 +4*x, x_range = [0,4]).set_color(MAROON_C)

        int_x_sinistro = always_redraw(lambda:
                                   DashedLine(
                                        axis.coords_to_point(2-(4-function.underlying_function(x_0.get_value())-epsilon.get_value())**(1/2),0),
                                        axis.coords_to_point(2-(4-function.underlying_function(x_0.get_value())-epsilon.get_value())**(1/2),4)
                                   ).set_color(TEAL_B)
                                   )
        int_x_destro = always_redraw(lambda:
                                   DashedLine(
                                        axis.coords_to_point(2-(4-function.underlying_function(x_0.get_value())+epsilon.get_value())**(1/2),0),
                                        axis.coords_to_point(2-(4-function.underlying_function(x_0.get_value())+epsilon.get_value())**(1/2),4)
                                   ).set_color(TEAL_B)
                                   )
        int_y_sinistro = always_redraw(lambda:
                                   DashedLine(
                                        axis.coords_to_point(0,function.underlying_function(x_0.get_value())-epsilon.get_value()),
                                        axis.coords_to_point(2,function.underlying_function(x_0.get_value())-epsilon.get_value())
                                   ).set_color(GREEN_B)
                                   )
        int_y_destro = always_redraw(lambda:
                                      DashedLine(
                                         axis.coords_to_point(0,function.underlying_function(x_0.get_value())+epsilon.get_value()),
                                         axis.coords_to_point(2,function.underlying_function(x_0.get_value())+epsilon.get_value())
                                      ).set_color(GREEN_B))
        
        int_x_label_r = always_redraw(lambda:
                                    MathTex(r'x_0 - \delta').next_to(int_x_destro, DOWN).scale(0.5).set_color(TEAL_B))
        int_x_label_l = always_redraw(lambda:
                                    MathTex(r'x_0 + \delta').next_to(int_x_sinistro, DOWN).set_color(TEAL_B).scale(0.5))

        func_x_0 = always_redraw(lambda:
                                 DashedLine(
                                     axis.coords_to_point(x_0.get_value(),0),
                                     axis.coords_to_point(x_0.get_value(),function.underlying_function(x_0.get_value()))
                                 ).set_color(YELLOW_B))
        
        func_y_0 = always_redraw(lambda:
                                 DashedLine(
                                     axis.coords_to_point(0,function.underlying_function(x_0.get_value())),
                                     axis.coords_to_point(x_0.get_value(),function.underlying_function(x_0.get_value()))
                                 ).set_color(YELLOW_B))
        
        int_y_label_l = always_redraw(lambda:
                                     MathTex(r'L- \varepsilon ', substrings_to_isolate= 'L').next_to(int_y_sinistro,LEFT).scale(0.5).set_color_by_tex('L',YELLOW_B))
        int_y_label_r = always_redraw(lambda:
                                     MathTex(r'L+ \varepsilon ', substrings_to_isolate= 'L').next_to(int_y_destro,LEFT).scale(0.5).set_color_by_tex('L',YELLOW_B))
        
        rand_x = always_redraw(lambda: DashedLine(
            axis.coords_to_point((-(4-function.underlying_function(x_0.get_value())-epsilon.get_value())**(1/2) + (4- function.underlying_function(x_0.get_value()) + epsilon.get_value())**(1/2))/2 +2 - (4 - function.underlying_function(x_0.get_value()) + epsilon.get_value())**(1/2) +dx.get_value(),0),
            axis.coords_to_point((-(4-function.underlying_function(x_0.get_value())-epsilon.get_value())**(1/2) + (4- function.underlying_function(x_0.get_value()) + epsilon.get_value())**(1/2))/2 +2 - (4 - function.underlying_function(x_0.get_value()) + epsilon.get_value())**(1/2) +dx.get_value(),
                                 function.underlying_function((-(4-function.underlying_function(x_0.get_value())-epsilon.get_value())**(1/2) + (4- function.underlying_function(x_0.get_value()) + epsilon.get_value())**(1/2))/2 +2 - (4 - function.underlying_function(x_0.get_value()) + epsilon.get_value())**(1/2) +dx.get_value()))
        ).set_color(MAROON_C))

        rand_y = always_redraw(lambda: DashedLine(
            axis.coords_to_point(0,
                                 function.underlying_function((-(4-function.underlying_function(x_0.get_value())-epsilon.get_value())**(1/2) + (4- function.underlying_function(x_0.get_value()) + epsilon.get_value())**(1/2))/2 +2 - (4 - function.underlying_function(x_0.get_value()) + epsilon.get_value())**(1/2) +dx.get_value())),
            rand_x.get_end()
        ).set_color(MAROON_C))
        rand_label = always_redraw(lambda: MathTex(
            r'f(x)').next_to(rand_y,LEFT).scale(0.5).set_color(MAROON_C))
        

        part1 = MathTex(r"\forall \epsilon > 0, \exists ", 
                        r"\delta", 
                        r" > 0 \text{ such that }")
        part2 = MathTex(r"0 < |x - c| < ", 
                        r"\delta")
        part3 = MathTex(r"\Rightarrow |f(x) - ", 
                        r"L", 
                        r"| < \epsilon")
        
        #difference1 = always_redraw(lambda: Line(
        #    axis.coords_to_point(x_0.get_value(),function.underlying_function(x_0.get_value())),
        #    axis.coords_to_point(x_0.get_value(),function.underlying_function(x_0.get_value()+dx.get_value()))
        #).set_color(RED))
#
        #difference2 = always_redraw(lambda: Line(
        #    func_y_0.get_start(),
        #    int_y_destro.get_start()
        #).set_color(RED))
        
        
        self.play(Write(axis), Write(axis_labels), Write(function), run_time=2)
        self.wait(2)
        self.play(Create(int_x_destro), Create(int_x_sinistro), Create(int_y_destro), Create(int_y_sinistro), Write(int_x_label_l), Write(int_x_label_r), Write(int_y_label_l), Write(int_y_label_r), run_time=2)
        self.wait(2)
        self.play(Create(func_x_0), Create(func_y_0), run_time=2)
        self.wait(2)
        self.play(Create(rand_x), Create(rand_y), Write(rand_label), run_time=2)
        self.wait(2)
        self.play(dx.animate.set_value(-0.4), run_time=1)
        self.wait()
        self.play(dx.animate.set_value(0.2), run_time=1)
        self.wait(2)
        self.play(dx.animate.set_value(0), run_time=1)
        self.wait(2)
        self.play(x_0.animate.set_value(0.5), run_time=2)
        self.wait()
        self.play(epsilon.animate.set_value(0.3), run_time= 2)
        self.wait()
        
        
        

        
        