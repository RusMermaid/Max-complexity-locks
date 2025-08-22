# manim code used in chapters 4 to 6.

from manim import *
import math
from chapter_1to3 import Dots, PatternPath, PatternLines, Pattern, SlopeGroup

class Image4by4(Scene) :
  def construct(self) :
    dots = Dots(4, 4)
    self.add(dots)

class Image5by5(Scene) :
  def construct(self) :
    dots = Dots(5, 5)
    self.add(dots)

class ImageRect(Scene) :
  def construct(self) :
    dots1 = Dots(3, 2).shift(LEFT*3)
    dots2 = Dots(4, 3).shift(RIGHT*3)
    self.add(dots1, dots2)

# 2x2 grid
class Scene8(Scene) :
  def construct(self) :
    dots = Dots(2, 2).shift(UP)
    self.play(FadeIn(dots), run_time=0.5)
    self.wait(0.5)

    slopes = [[1,0], [0,1], [1,1], [1,-1]]
    slope_texts = ['0', r'\infty', '1', '-1']

    slope_list = VGroup()
    for (w, h) in slopes :
      slopegroup = SlopeGroup(w, h).scale(0.5)
      slope_list.add(slopegroup)
    slope_list.arrange_in_grid(rows=1, buff=0.8, row_alignments='d').shift(DOWN)
    self.play(Create(slope_list), run_time=0.5)
    self.wait(0.5)

    # draw
    def slope_text(i) :
      text = MathTex(slope_texts[i]).next_to(slope_list[i], DOWN*1.5)
      text.move_to([text.get_x(), -2.2, 0])
      return text
    
    def slope_text_group(i) :
      return AnimationGroup(
        Flash(slope_list[i], color=WHITE, run_time=0.5, num_lines=8, flash_radius=0.5),
        FadeIn(slope_text(i), run_time=0.5),
      )
    
    self.play(AnimationGroup(
      *[slope_text_group(i) for i in range(4)],
      lag_ratio=1
    ))
    self.wait()

    pattern = [1, 4, 3, 2]
    pattern_slopes = [3, 0, 2]

    lines = PatternLines(dots, pattern)

    anim_list = []
    for i in range(len(lines)) :
      anim_list.append(AnimationGroup(
        Create(lines[i], run_time=0.3),
        # Flash(slope_list[pattern_slopes[i]], run_time=0.5, num_lines=8, flash_radius=0.5),
        slope_list[pattern_slopes[i]].animate(run_time=0.3).set_color(YELLOW)
      ))
    
    self.play(AnimationGroup(*anim_list, lag_ratio=1))
    self.play(slope_list[1].animate.set_color(RED))
    self.wait()

# 4x4 grid
class Scene9(Scene) :
  def construct(self) :
    dots = Dots(4, 4)
    self.play(FadeIn(dots), run_time=0.5)
    self.wait(0.5)

    slopes = [[1,0], [0,1]]
    slope_list = VGroup()
    for (w, h) in slopes :
      slopegroup = SlopeGroup(w, h).scale(0.5)
      slope_list.add(slopegroup)
    slope_list.add(MathTex(r'\textup{Positive}\times7').scale(0.7))
    slope_list.add(MathTex(r'\textup{Negative}\times7').scale(0.7))

    slope_list.arrange_in_grid(cols=1, buff=0.8).shift(RIGHT*4)
    self.play(Create(slope_list[:2]), run_time=0.5)
    self.wait(0.5)

    lines = []
    pos_list = [[3,1], [2,1], [3,2], [1,1], [2,3], [1,2], [1,3]]
    for pos in pos_list :
      d = pos[0] + 12 - pos[1]*4
      lines.append(Line(start=dots[12].get_center(), end=dots[d].get_center()))

    self.play(AnimationGroup(
      *[Create(line) for line in lines],
      FadeIn(slope_list[2]),
      lag_ratio=0.1
    ))
    self.wait()
    self.play(FadeIn(slope_list[3]))
    self.wait()

    number_text = MathTex(r'\textup{Slopes: }2+2\times7=16').shift(UP*3)
    self.play(FadeIn(number_text))
    self.wait()

# 5x5 grid
class Scene10(Scene) :
  def construct(self) :
    dots = Dots(5, 5).scale(0.8)
    self.play(FadeIn(dots), run_time=0.5)
    self.wait(0.5)

    slopes = [[1,0], [0,1]]
    slope_list = VGroup()
    for (w, h) in slopes :
      slopegroup = SlopeGroup(w, h).scale(0.5)
      slope_list.add(slopegroup)
    slope_list.add(MathTex(r'\textup{Positive}\times11').scale(0.7))
    slope_list.add(MathTex(r'\textup{Negative}\times11').scale(0.7))

    slope_list.arrange_in_grid(cols=1, buff=0.8).shift(RIGHT*4)
    self.play(Create(slope_list[:2]), run_time=0.5)
    self.wait(0.5)

    lines = []
    pos_list = [[4,1], [3,1], [2,1], [3,2], [4,3], [1,1],
                [3,4], [2,3], [1,2], [1,3], [1,4]]
    for pos in pos_list :
      d = pos[0] + 20 - pos[1]*5
      lines.append(Line(start=dots[20].get_center(), end=dots[d].get_center()))

    self.play(AnimationGroup(
      *[Create(line) for line in lines],
      FadeIn(slope_list[2]),
      lag_ratio=0.1
    ))
    self.play(FadeIn(slope_list[3]))

    number_text = MathTex(r'\textup{Slopes: }2+2\times11=24').shift(UP*3)
    self.play(FadeIn(number_text))
    self.wait()

# 2~5 grids
class Scene11(Scene) :
  def construct(self) :
    pos_list = [[4,1], [3,1], [2,1], [3,2], [4,3], [1,1],
                [3,4], [2,3], [1,2], [1,3], [1,4]]
    
    table = []

    for y in range(2, 6) :
      row = []
      for x in range(2, 6) :
        dots = Dots(x, y).scale(0.35)
        lines = VGroup()
        for (w, h) in pos_list :
          if w < x and h < y :
            d = w + x*(y-1-h)
            lines.add(Line(start=dots[x*(y-1)].get_center(), end=dots[d].get_center()))
        if(len(lines)*2+2 < len(dots)) :
          text = MathTex(r'\textup{Slopes<Dots}').scale(0.5).next_to(dots, DOWN*0.7)
        else :
          text = MathTex(r'\textup{Slopes=Dots}').scale(0.5).next_to(dots, DOWN*0.7)
        row.append(VGroup(dots, lines, text))
      table.append(row)

    grids = MobjectTable(table,
      v_buff=0.3,
      row_labels=[Text(str(x)).scale(0.8) for x in range(2, 6)],
      col_labels=[Text(str(y)).scale(0.8) for y in range(2, 6)],
    )
    self.play(FadeIn(grids))

    badgrids = [[2,2], [2,3], [2,4], [2,5],
                [3,2], [3,4],
                [4,2], [4,3], [4,4], [4,5],
                [5,2], [5,4]]
    goodgrids = [[3,3], [3,5], [5,3], [5,5]]

    self.wait()
    self.play(AnimationGroup(
      *[grids.get_entries(pos=cell).animate.set_color(RED) for cell in badgrids]
    ))
    self.wait()
    self.play(AnimationGroup(
      *[grids.get_entries(pos=cell).animate.set_color(YELLOW) for cell in goodgrids]
    ))
    self.wait()

# 9x9 grid
class Scene12(Scene) :
  def construct(self) :
    dots = Dots(9, 9).scale(0.7)
    self.play(FadeIn(dots), run_time=0.5)

    lines = []
    pos_list = []
    for x in range(1, 9) :
      for y in range(1, 9) :
        if math.gcd(x, y) == 1 :
          pos_list.append([x, y])
    pos_list.sort(key=lambda coord : coord[1]/coord[0])

    for pos in pos_list :
      d = pos[0] + 72 - pos[1]*9
      lines.append(Line(start=dots[72].get_center(), end=dots[d].get_center(), stroke_width=2))
    
    number_text = MathTex(r'\textup{Slopes: }2+2\times43=88').shift(UP*3.5)
    
    self.play(AnimationGroup(
      FadeIn(number_text),
      *[Create(line) for line in lines],
      lag_ratio=0.05
    ), run_time=1.5)
    self.wait()

# lowerleft start
class Scene13(Scene) :
  def construct(self) :
    dots = Dots(4, 4)

    lines = []
    pos_list = [[3,1], [2,1], [3,2], [1,1], [2,3], [1,2], [1,3]]
    for pos in pos_list :
      d = pos[0] + 12 - pos[1]*4
      lines.append(Line(start=dots[12].get_center(), end=dots[d].get_center()))

    self.play(AnimationGroup(
      FadeIn(dots),
      *[Create(line) for line in lines],
      lag_ratio=0.1
    ))
    self.wait()

    self.play(AnimationGroup(
      *[FadeOut(line) for line in lines]
    ))
    line1 = Line(start=dots[5].get_center(), end=dots[3].get_center())
    line2 = Line(start=dots[12].get_center(), end=dots[10].get_center())
    self.play(FadeIn(line1), run_time=0.5)
    self.wait()
    self.play(Transform(line1, line2), run_time=0.8)
    self.wait()

# xy plane and slope
class Scene14(Scene) :
  def construct(self) :
    dots = Dots(5, 5)

    lines = VGroup()
    pos_list = [[4,1], [3,1], [2,1], [3,2], [4,3], [1,1],
                [3,4], [2,3], [1,2], [1,3], [1,4]]
    for (x, y) in pos_list :
      lines.add(Line(start=[-2,-2,0], end=[x-2, y-2, 0]))
    
    self.play(AnimationGroup(
      FadeIn(dots),
      *[Create(line) for line in lines],
    ))
    self.wait()

    axes = VGroup(
      Arrow(start=[-3,-2,0], end=[3.5,-2,0], color=GRAY, stroke_width=3),
      Arrow(start=[-2,-3,0], end=[-2,3.5,0], color=GRAY, stroke_width=3)
    )
    
    self.play(AnimationGroup(
      Create(axes[0]),
      Create(axes[1])
    ))
    self.wait()
    self.play(lines.animate.set_color(GRAY_E), run_time=0.5)
    self.play(AnimationGroup(
      dots[17].animate.set_color(RED),
      lines[2].animate.set_color(RED)
    ), run_time=0.5)
    self.wait()

    slopetext = Text('Slope: ').scale(0.7).shift(LEFT*5)
    frac = MathTex(r'\frac{1}{2}').shift(LEFT*4)
    self.play(FadeIn(slopetext, frac))
    self.wait()

    b1 = BraceBetweenPoints([-2,-2,0], [0,-2,0])
    b1text = b1.get_tex("2")
    b2 = BraceBetweenPoints([0,-2,0], [0,-1,0])
    b2text = b2.get_tex("1")
    self.play(FadeIn(b1, b1text, b2, b2text))
    self.wait()

    self.play(AnimationGroup(
      FadeOut(frac, b1, b1text, b2, b2text),
      dots[17].animate.set_color(WHITE),
      lines[2].animate.set_color(GRAY_E),
      dots[6].animate.set_color(RED),
      lines[9].animate.set_color(RED),
    ))
    self.wait()

    frac2 = MathTex(r'3').shift(LEFT*4)
    frac3 = MathTex(r'\frac{3}{1}').shift(LEFT*4)
    self.play(FadeIn(frac2))
    self.play(TransformMatchingTex(frac2, frac3))
    self.wait()

    b1 = BraceBetweenPoints([-2,-2,0], [-1,-2,0])
    b1text = b1.get_tex("1")
    b2 = BraceBetweenPoints([-1,-2,0], [-1,1,0])
    b2text = b2.get_tex("3")
    self.play(FadeIn(b1, b1text, b2, b2text), run_time=0.5)
    self.wait()
    self.play(AnimationGroup(
      FadeOut(frac3, b1, b1text, b2, b2text),
      dots[6].animate.set_color(WHITE),
      lines[9].animate.set_color(GRAY_E),
    ))
    self.wait()

    badline = Line([-2,-2,0], [2,0,0], color=RED)
    self.play(AnimationGroup(
      dots[14].animate.set_color(RED),
      FadeIn(badline)
    ))
    self.wait()
    self.play(AnimationGroup(
      lines[2].animate.set_color(RED),
      FadeOut(badline)
    ))
    self.wait()

    frac3 = MathTex(r'\frac{2}{4}').shift(LEFT*4)
    self.play(FadeIn(frac3), run_time=0.5)
    self.wait()
    self.play(AnimationGroup(
      FadeOut(frac3),
      FadeIn(frac)
    ), run_time=0.5)
    self.wait()

# coprime dots
class Scene15(Scene) :
  def construct(self) :
    dots = Dots(5, 5)

    lines = VGroup()
    pos_list = [[4,1], [3,1], [2,1], [3,2], [4,3], [1,1],
                [3,4], [2,3], [1,2], [1,3], [1,4]]
    for (x, y) in pos_list :
      lines.add(Line(start=[-2,-2,0], end=[x-2, y-2, 0], color=GRAY_E))
    
    axes = VGroup(
      Arrow(start=[-3,-2,0], end=[3.5,-2,0], color=GRAY, stroke_width=3),
      Arrow(start=[-2,-3,0], end=[-2,3.5,0], color=GRAY, stroke_width=3)
    )

    self.add(lines, dots, axes)
    self.wait()

    coprimedots = [1, 3, 6, 7, 9, 11, 13, 16, 17, 18, 19]
    texts = VGroup()
    for i in coprimedots :
      text = MathTex('({},{})'.format(i%5, 4-(i//5)), color=RED).scale(0.7).next_to(dots[i], DOWN)
      texts.add(text)
    
    self.play(AnimationGroup(
      *[dots[i].animate.set_color(RED) for i in coprimedots]
    ))
    self.play(FadeIn(texts))
    self.wait()
    
    area_square = Square(side_length=3.5, color=YELLOW).shift([0.5, 0.5, 0])
    area_text = MathTex(r'1 \leq x < 5, 1 \leq y < 5', color=YELLOW).scale(0.7).shift([0.5,2.7,0])
    self.play(FadeIn(area_text, area_square))
    self.wait()

# graphing
class Scene16(Scene) :
  def construct(self):
    plane = NumberPlane(
      x_range = (1, 17, 2),
      y_range = (0, 350, 25),
      x_length = 7,
      y_length=7,
      axis_config={
        "include_ticks": True,
        "include_tip": True,
        "tip_width": 0.05,
        "tip_height": 0.1,
        "include_numbers": True
      },
      background_line_style={"stroke_width": 0},
    )
    plane.center()
    x_label = plane.get_x_axis_label('n')

    def phi4(n) :
      lst = [4]
      for i in range(2, n) :
        prev = lst[i-2]
        curr = prev
        for j in range(1, i+1) :
          if math.gcd(i, j) == 1 :
            curr += 4
        lst.append(curr)
      return lst

    self.play(FadeIn(plane, x_label))
    self.wait()
    

    slope_graph = plane.get_graph(
      lambda n: 12*(n-1)*(n-1)/(PI*PI),
      color=RED
    )
    dot_graph = plane.get_graph(
      lambda n: n*n,
      color=BLUE
    )
    slope_label = plane.get_graph_label(
      slope_graph, r"\frac{12(n-1)^2}{\pi^2}", color=RED,
      x_val=15.5, direction=LEFT*2.5
    ).scale(0.8)
    dot_label = plane.get_graph_label(
      dot_graph, r"n^2", color=BLUE,
      x_val=16, direction=RIGHT*2
    ).scale(0.8)
    
    intersect_dot = Dot(plane.coords_to_point(10.741, 115.371))
    intersect_text = MathTex('(10.74, 115.37)').scale(0.8).next_to(intersect_dot)
    

    self.play(AnimationGroup(
      Create(slope_graph),
      Create(dot_graph),
      FadeIn(slope_label, dot_label)
    ))
    self.play(FadeIn(intersect_dot, intersect_text))
    self.wait()

    slope_dots = plane.get_line_graph(
      x_values = list(range(2, 18)),
      y_values = phi4(17),
      stroke_width=0,
      vertex_dot_radius=0.05,
      vertex_dot_style=dict(fill_color=RED),
    )
    self.play(Create(slope_dots))

# lemma 1
class Scene17(Scene) :
  def construct(self) :
    self.camera.background_color = "#ece6e2"

    numbers = MathTex(*[str(i) + r"\ " for i in range(1, 19)], r"...\ ", "N",
                      color=BLACK)
    self.add(numbers)
    self.wait()

    evens = VGroup(*[numbers[i] for i in range(1, 19, 2)]).save_state()
    evens_focus = evens.copy().shift(UP*0.5).set_color(RED)

    threes = VGroup(*[numbers[i] for i in range(2, 19, 3)]).save_state()
    threes_focus = threes.copy().shift(UP*0.5).set_color(RED)

    oddthrees = VGroup(*[numbers[i] for i in range(2, 19, 6)])
    oddthrees_focus = oddthrees.copy().shift(UP*0.5).set_color(RED)

    self.play(Transform(evens, evens_focus))
    self.wait()
    self.play(Restore(evens))
    self.wait()
    self.play(Transform(threes, threes_focus))
    self.wait()
    self.play(Restore(threes))
    self.wait()
    self.play(FadeOut(evens))
    self.wait()
    self.play(Transform(oddthrees, oddthrees_focus))
    self.wait()

# lemma 2-1
class Scene18(Scene) :
  def construct(self) :
    self.camera.background_color = "#ece6e2"

    numbers1 = MathTex(*[str(i) + r"\ " for i in range(1, 19)], color=BLACK)
    evens1 = VGroup(*[numbers1[i] for i in range(1, 18, 2)]).save_state()
    evens1_focus = evens1.copy().shift(UP*0.5).set_color(RED)

    self.add(numbers1)
    self.wait()
    self.play(Transform(evens1, evens1_focus))
    self.wait()
    self.play(Restore(evens1))
    self.wait()

    numbers2 = MathTex(*[str(i) + r"\ " for i in range(1, 20)], color=BLACK)
    evens2 = VGroup(*[numbers2[i] for i in range(1, 19, 2)]).save_state()
    evens2_focus = evens2.copy().shift(UP*0.5).set_color(RED)

    self.play(TransformMatchingTex(numbers1, numbers2))
    self.wait()
    self.play(Flash(numbers2[-1], color=BLACK, flash_radius=0.5, num_lines=8))
    self.wait()
    self.play(Transform(evens2, evens2_focus))
    self.wait()

# lemma 2-2
class Scene19(Scene) :
  def construct(self) :
    self.camera.background_color = "#ece6e2"

    numbers1 = MathTex(*[str(i) + r"\ " for i in range(1, 19)], color=BLACK)
    threes1 = VGroup(*[numbers1[i] for i in range(2, 18, 3)]).save_state()
    threes1_focus = threes1.copy().shift(UP*0.5).set_color(RED)

    self.add(numbers1)
    self.wait()
    self.play(Transform(threes1, threes1_focus))
    self.wait()
    self.play(Restore(threes1))
    self.wait()

    numbers2 = MathTex(*[str(i) + r"\ " for i in range(1, 21)], color=BLACK)
    threes2 = VGroup(*[numbers2[i] for i in range(2, 20, 3)]).save_state()
    threes2_focus = threes2.copy().shift(UP*0.5).set_color(RED)

    self.play(TransformMatchingTex(numbers1, numbers2))
    self.wait()
    self.play(Flash(numbers2[-2:], color=BLACK, flash_radius=0.9))
    self.wait()
    self.play(Transform(threes2, threes2_focus))
    self.wait()

# dots graph
class Scene20(Scene) :
  def construct(self):
    self.camera.background_color = "#ece6e2"

    m = 12
    n = 8
    plane = NumberPlane(
      x_range = (0, m-0.5, 1),
      y_range = (0, n-0.5, 1),
      x_length = m*0.5,
      y_length = n*0.5,
      axis_config={
        "include_ticks": True,
        "include_numbers": True,
        "stroke_color": BLACK,
        "decimal_number_config": {
          "color": BLACK,
          "num_decimal_places": 0
        }
      },
      background_line_style={"stroke_width": 0},
    )
    plane.center()
    plane.shift(LEFT*2+DOWN*0.5)
    
    # dots fadein
    dots = VGroup()
    for y in range(n) :
      for x in range(m) :
        dot = Dot(plane.coords_to_point(x, y), color=BLACK).scale(0.75)
        dots.add(dot)

    brace_m = BraceBetweenPoints(
      plane.coords_to_point(m-1,n-1),
      plane.coords_to_point(0,n-1),
      color=BLACK,
      buff=0.5
    )
    brace_m_tex = brace_m.get_tex('m').set_color(BLACK)
    brace_n = BraceBetweenPoints(
      plane.coords_to_point(m-1,0),
      plane.coords_to_point(m-1,n-1),
      color=BLACK,
      buff=0.5
    )
    brace_n_tex = brace_n.get_tex('n').set_color(BLACK)

    self.play(FadeIn(dots, brace_n, brace_m, brace_m_tex, brace_n_tex))
    self.wait(2)
    
    # axis fadein
    dots_axis = VGroup(*[dots[i] for i in range(0,m*n,m)], *[dots[i] for i in range(1,m)])
    self.play(FadeIn(plane))
    self.play(FadeOut(dots_axis, brace_n, brace_m, brace_n_tex, brace_m_tex))
    self.wait(2)
    
    # step 1
    tex_step1 = MathTex(r"\textup{Dots} = (m-1)(n-1)",
      color=BLACK).scale(0.8).shift(UP*3)
    self.play(FadeIn(tex_step1))
    self.wait(2)

    # step 2-1
    divide_2s = []
    for y in range(1, n) :
      for x in range(1, m) :
        if x%2 == 0 and y%2 == 0 :
          divide_2s.append(x + m*y)
    
    dots_2 = VGroup(*[dots[i] for i in divide_2s])
    self.play(dots_2.animate.set_color(RED))

    tex_dots2 = MathTex(
      r"\textup{Dots to remove}",
      r"\approx \textup{Dots} \times \frac{1}{2^2}",
      color=BLACK).scale(0.7).shift(RIGHT*4)

    tex_dots2[0].set_color(RED)
    self.play(FadeIn(tex_dots2))
    self.wait(2)

    tex_step2_1 = MathTex(r"{{\textup{Dots} \approx (m-1)(n-1) \left( 1-\frac{1}{2^2} \right)}}",
      color=BLACK).scale(0.8).move_to(tex_step1)

    self.play(AnimationGroup(
      FadeOut(dots_2),
      FadeOut(tex_step1),
      FadeIn(tex_step2_1)
    ))
    self.play(FadeOut(tex_dots2))

    # step 2-2
    divide_3s = []
    for y in range(1, n) :
      for x in range(1, m) :
        if x%3 == 0 and y%3 == 0 :
          if (x + m*y) not in divide_2s :
            divide_3s.append(x + m*y)
    
    dots_3 = VGroup(*[dots[i] for i in divide_3s])
    self.play(dots_3.animate.set_color(RED))
    self.wait(2)

    tex_dots3 = MathTex(
      r"\textup{Dots to remove}",
      r"\approx \textup{Dots} \times \frac{1}{3^2}",
      color=BLACK).scale(0.8).move_to(tex_dots2)

    tex_dots3[0].set_color(RED)
    self.play(FadeIn(tex_dots3))
    self.wait(2)

    tex_step2_2 = MathTex(
      r"\textup{Dots} \approx (m-1)(n-1) \left( 1-\frac{1}{2^2} \right)",
      r"\left( 1-\frac{1}{3^2} \right)",
      color=BLACK).scale(0.8).move_to(tex_step1)

    self.play(AnimationGroup(
      FadeOut(dots_3),
      TransformMatchingTex(tex_step2_1, tex_step2_2)
    ))
    self.play(FadeOut(tex_dots3))
    self.wait(2)

    # step 2-3
    divide_5s = [5*m + 5, 5*m + 10]
    dots_5 = VGroup(*[dots[i] for i in divide_5s])

    tex_dots5 = MathTex(
      r"\textup{Dots to remove}",
      r"\approx \textup{Dots} \times \frac{1}{5^2}",
      color=BLACK).scale(0.8).move_to(tex_dots2)

    tex_dots5[0].set_color(RED)
    self.play(AnimationGroup(
      dots_5.animate.set_color(RED),
      FadeIn(tex_dots5)
    ), run_time=0.5)
    self.wait()

    tex_step2_3 = MathTex(
      r"\textup{Dots} \approx (m-1)(n-1) \left( 1-\frac{1}{2^2} \right)",
      r"\left( 1-\frac{1}{3^2} \right)",
      r"\left( 1-\frac{1}{5^2} \right)",
      color=BLACK).scale(0.8).move_to(tex_step1)

    self.play(AnimationGroup(
      FadeOut(dots_5),
      TransformMatchingTex(tex_step2_2, tex_step2_3),
      FadeOut(tex_dots5)
    ), run_time=0.5)
    self.wait()

    # step 2-4
    dots_7 = dots[7*m + 7]

    tex_dots7 = MathTex(
      r"\textup{Dots to remove}",
      r"\approx \textup{Dots} \times \frac{1}{7^2}",
      color=BLACK).scale(0.8).move_to(tex_dots2)

    tex_dots7[0].set_color(RED)
    self.play(AnimationGroup(
      dots_7.animate.set_color(RED),
      FadeIn(tex_dots7)
    ), run_time=0.5)
    self.wait()

    tex_step2_4 = MathTex(
      r"\textup{Dots} \approx (m-1)(n-1) \left( 1-\frac{1}{2^2} \right)",
      r"\left( 1-\frac{1}{3^2} \right)",
      r"\left( 1-\frac{1}{5^2} \right)",
      r"\left( 1-\frac{1}{7^2} \right)",
      color=BLACK).scale(0.8).move_to(tex_step1)

    self.play(AnimationGroup(
      FadeOut(dots_7),
      TransformMatchingTex(tex_step2_3, tex_step2_4),
      FadeOut(tex_dots7)
    ), run_time=0.5)
    self.wait()

    tex_step2_5 = MathTex(
      r"\textup{Dots} \approx (m-1)(n-1) \left( 1-\frac{1}{2^2} \right)",
      r"\left( 1-\frac{1}{3^2} \right)",
      r"\left( 1-\frac{1}{5^2} \right)",
      r"\left( 1-\frac{1}{7^2} \right)",
      r"\left( 1-\frac{1}{11^2} \right) \ldots",
      color=BLACK).scale(0.8).move_to(tex_step1)
    
    self.play(TransformMatchingTex(tex_step2_4, tex_step2_5), run_time=0.5)
    self.wait(2)

    tex_step2_6 = MathTex(r"\textup{Dots}", r"\geq", r"(m-1)(n-1) \left( 1-\frac{1}{2^2} \right)", color=BLACK).scale(0.8).move_to(tex_step2_5[0])
    tex_step2_6[1].set_color(RED)
    self.play(FadeTransform(tex_step2_5[0], tex_step2_6))
    self.wait(2)

# 3d graph
class Scene21(ThreeDScene) :
  def func_slope(self, u, v):
    return np.array([u, v, (u-1)*(v-1)*12/(PI*PI) - 50])
  
  def func_dot(self, u, v):
    return np.array([u, v, u*v - 50])

  def construct(self):
    self.camera.background_color = "#ece6e2"

    axes = ThreeDAxes(
      x_range=[8,13],
      y_range=[8,13],
      z_range=[0,150,25],
      x_length=5,
      y_length=5,
      z_length=5,
      axis_config={
        "stroke_color": BLACK,
        "color": BLACK,
        "decimal_number_config": {
          "color": BLACK,
          "num_decimal_places": 0
        }
      },
    )
    surf_slope = ParametricSurface(
      lambda u, v: axes.c2p(*self.func_slope(u, v)),
      u_range=[8, 13],
      v_range=[8, 13],
      resolution=32,
      fill_color=RED,
      fill_opacity=0.7,
      checkerboard_colors=[RED, RED],
      stroke_color=RED
    )
    surf_dot = ParametricSurface(
      lambda u, v: axes.c2p(*self.func_dot(u, v)),
      u_range=[8, 13],
      v_range=[8, 13],
      resolution=32,
      fill_color=BLUE,
      fill_opacity=0.7,
      checkerboard_colors=[BLUE, BLUE],
      stroke_color=BLUE
    )
    self.set_camera_orientation(phi=85*DEGREES, theta=-90*DEGREES, frame_center=axes)
    self.add(axes, surf_slope, surf_dot)
    self.begin_ambient_camera_rotation(rate=0.3)
    self.wait(5)

# 5x5 grid example
class Scene22(Scene) :
  def construct(self) :
    slopes1 = [[1,1], [1,0],
              [1,3], [1,2],  
              [2,1], [1,4],  
              [4,1], [3,1],  
              [3,2], [2,3],  
              [4,3], [3,4]]
    
    slopes2 = [[0,1], [1,-1],
               [1,-2], [1,-3],
               [1,-4], [2,-1],
               [3,-1], [4,-1],
               [2,-3], [3,-2],
               [3,-4], [4,-3]]
    
    PATTERN = [1, 20, 21, 4, 25,
               2, 19, 6, 15, 7,
               5, 16, 9, 22, 3,
               10, 24, 8, 17, 14,
               18, 12, 23, 13, 11]
    
    slopes_total = slopes1 + slopes2

    pattern_slopes = []
    for s in range(24) :
      dx = ((PATTERN[s+1]-1) % 5) - ((PATTERN[s]-1) % 5)
      dy = ((PATTERN[s]-1) // 5) - ((PATTERN[s+1]-1) // 5)
      
      for (i, slope) in enumerate(slopes_total) :
        if slope[0]*dy == slope[1]*dx :
          pattern_slopes.append(i)

    dots = Dots(5, 5)
    lines = PatternLines(dots, PATTERN)

    # draw all slopes
    slope_list = VGroup(*[SlopeGroup(w, h) for (w, h) in slopes1], *[SlopeGroup(w, h) for (w, h) in slopes2])
    
    slope1_list = slope_list[:12]
    slope1_list.scale(0.25).arrange_in_grid(cols=2, buff=0.2).shift(LEFT*5)

    slope2_list = slope_list[12:]
    slope2_list.scale(0.25).arrange_in_grid(cols=2, buff=0.2).shift(RIGHT*5)

    self.add(slope_list)
    self.add(dots)
    self.wait(0.5)

    animation_list = []
    for i in range(len(lines)) :
      animation_list.append(AnimationGroup(
        Create(lines[i]),
        Flash(slope_list[pattern_slopes[i]], num_lines=8, flash_radius=0.5),
        slope_list[pattern_slopes[i]].animate.set_color(YELLOW),
        run_time=0.25
      ))
    
    self.play(AnimationGroup(*animation_list, lag_ratio=1))
    self.wait()
