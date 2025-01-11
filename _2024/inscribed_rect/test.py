from _2024.inscribed_rect.helpers import *
class test_dot(InteractiveScene):
    def construct(self):
        # init
        frame=self.frame
        # start
        frame.reorient(-8, 51, 0, (-0.72, -0.16, 0.0), 1.84)
        ax=ThreeDAxes()
        self.add(ax)
        dot=get_special_dot()
        truedot=TrueDot()
        truedot.move_to(ax.c2p(-1,0,0))
        glowdot=GlowDot()
        glowdot.move_to(ax.c2p(1,0,0))
        self.add(glowdot)
        self.add(truedot)
        self.add(dot)
        glowdot.move_to(truedot)
        truedot.set_color(YELLOW)
        truedot.make_3d()
        self.clear()

        # polygon
        polygon = Polygon(LEFT, RIGHT)
        self.add(polygon)
        self.clear()

        # svg
        svg1 = SVGMobject("example_loop2").family_members_with_points()[0]
        svg2= SVGMobject("example_loop2")
        svgs=Group(svg1,svg2).arrange(RIGHT).set_width(FRAME_WIDTH)
        for svg in svgs:
            svg.set_stroke(color=WHITE,width=3,opacity=1)
        self.add(svgs)
        svg1.insert_n_curves(50)
        svg2.insert_n_curves(50)
        svg1.quick_point_from_proportion
