# manim code used in the proof by induction at the end.

from manim import *
import math
from chapter_1to3 import Dots, PatternPath, PatternLines, Pattern, SlopeGroup

def subp1(k) :
  dots = Dots(k, 3)
  lines = VGroup()
  for i in range(1, (k//2)+1) :
    lines.add(Line([-i,0,0], [i,-1,0]))
    lines.add(Line([i,0,0], [-i,-1,0]))
  return VGroup(lines, dots)

def subp2(k) :
  dots = Dots(k, 3)
  lines = VGroup()
  for i in range(k//2) :
    lines.add(Line([-i,1,0], [i+1,0,0]))
    lines.add(Line([i+1,1,0], [-i,0,0]))
  return VGroup(lines, dots)

def subp3(k) :
  dots = Dots(k, 3)
  lines = VGroup()
  for i in range(k//2) :
    lines.add(Line([-i-1,1,0], [i,-1,0]))
    lines.add(Line([i+1,1,0], [-i,-1,0]))
  return VGroup(lines, dots)

def subp4(k) :
  dots = Dots(k, 3)
  lines = VGroup()
  lines.add(Line([0,1,0],[0,0,0]))
  lines.add(Line([-(k//2),-1,0],[k//2,-1,0]))
  return VGroup(lines, dots)


# dividing 3x3
class Induct1(ThreeDScene) :
  def construct(self) :
    patterns = VGroup(subp1(3), subp2(3), subp3(3), subp4(3))
    self.play(FadeIn(patterns), run_time=2)

    self.play(AnimationGroup(
      *[patterns[i][1].animate.set_opacity(0.3) for i in range(4)],
      patterns[0][0].animate.set_color(RED),
      patterns[1][0].animate.set_color(ORANGE),
      patterns[2][0].animate.set_color(YELLOW),
      patterns[3][0].animate.set_color(GREEN),
    ), run_time=2)

    self.move_camera(phi=45*DEGREES, theta=30*DEGREES, gamma=120*DEGREES, run_time=4, added_anims=[
      patterns[0].animate(run_time=2).shift([-3,0,3]),
      patterns[1].animate(run_time=2).shift([-1,0,1]),
      patterns[2].animate(run_time=2).shift([1,0,-1]),
      patterns[3].animate(run_time=2).shift([3,0,-3])
    ])
    self.play(FadeOut(patterns))


class Induct2(Scene) :
  def construct(self) :
    patterns = VGroup(subp1(3), subp2(3), subp3(3), subp4(3))
    
    for i in range(4) :
      patterns[i].scale(0.7)
      patterns[i][1].set_opacity(0.3)
    
    patterns[0][0].set_color(RED),
    patterns[1][0].set_color(ORANGE),
    patterns[2][0].set_color(YELLOW),
    patterns[3][0].set_color(GREEN),
    
    patterns.arrange_in_grid(rows=1, buff=1.5)

    self.play(FadeIn(patterns), run_time=2)


class Induct3_3(Scene) :
  def construct(self) :
    functions = [subp1, subp2, subp3, subp4]
    colors = [RED, ORANGE, YELLOW, GREEN]
    i = 3

    patterns = VGroup(
      functions[i](3), Arrow(start=UP*0.5, end=DOWN).set_opacity(0),
      functions[i](5), Arrow(start=UP*0.5, end=DOWN).set_opacity(0),
      functions[i](7)
    ).scale(0.6)
    
    patterns[0][0].set_color(colors[i])
    patterns[2][0].set_color(colors[i]).set_opacity(0)
    patterns[4][0].set_color(colors[i]).set_opacity(0)

    self.play(AnimationGroup(
      FadeIn(patterns[0][1]),
      Create(patterns[0][0])
    ))

    self.play(FadeIn(patterns[2][1], patterns[4][1]))
    self.add(patterns[0])

    self.play(AnimationGroup(
      patterns.animate.arrange_in_grid(cols=1, buff=0.3)
    ), run_time=0.7)

    patterns[1].set_opacity(1)
    patterns[2][0].set_opacity(1)
    self.play(AnimationGroup(
      FadeIn(patterns[1]),
      Create(patterns[2][0])
    ), run_time=1.5)

    patterns[3].set_opacity(1)
    patterns[4][0].set_opacity(1)
    self.play(AnimationGroup(
      FadeIn(patterns[3]),
      Create(patterns[4][0])
    ), run_time=2)

    self.wait()


class Induct4_5(Scene) :
  def construct(self) :
    k = 5
    patterns = VGroup(subp1(k), subp2(k), subp3(k), subp4(k))
    
    for i in range(4) :
      patterns[i].scale(0.7)
      patterns[i][1].set_opacity(0.3)
    
    patterns[0][0].set_color(RED),
    patterns[1][0].set_color(ORANGE),
    patterns[2][0].set_color(YELLOW),
    patterns[3][0].set_color(GREEN),
    
    patterns.arrange_in_grid(cols=1, buff=0.5)

    self.play(FadeIn(patterns), run_time=2)
    self.play(AnimationGroup(
      *[patterns[i].animate.move_to(ORIGIN) for i in range(4)]
    ), run_time=3)

    self.play(patterns.animate.scale(1.5))
    self.play(patterns.animate.set_opacity(0.3))

    if k == 3 :
      order = [1,8,3,5,2,6,7,9,4]
    elif k == 5 :
      order = [1,14,7,5,12,
               9,3,8,4,13,
               2,10,11,15,6]
    elif k == 7 :
      order = [1,20,9,7,16,13,3,
               18,5,11,4,12,17,6,
               10,19,2,14,15,21,8]
    
    slopes1_1 = [[0,1]] + [[j, 1] for j in range(1, k)]
    slopes1_2 = [[1,0]] + [[j, -1] for j in range(1, k)]
    slopes2_1 = [[j, 2] for j in range(1,k,2)]
    slopes2_2 = [[j, -2] for j in range(1,k,2)]

    slopes_total = slopes1_1 + slopes1_2 + slopes2_1 + slopes2_2

    pattern_slopes = []
    for s in range(3*k - 1) :
      dx = ((order[s+1]-1) % k) - ((order[s]-1) % k)
      dy = ((order[s]-1) // k) - ((order[s+1]-1) // k)
      
      for (i, slope) in enumerate(slopes_total) :
        if slope[0]*dy == slope[1]*dx :
          pattern_slopes.append(i)

    # draw all slopes
    slope_list = VGroup(*[SlopeGroup(w, h) for (w, h) in slopes_total]).scale(0.25)

    slope1_1_list = slope_list[:k]
    slope1_1_list.arrange_in_grid(rows=1, buff=0.5).shift(UP*3.5)
    slope1_2_list = slope_list[k:2*k]
    slope1_2_list.arrange_in_grid(rows=1, buff=0.5).shift(DOWN*3.5)

    slope2_1_list = slope_list[2*k:(2*k + k//2)]
    slope2_1_list.arrange_in_grid(rows=1, buff=0.5).shift(UP*2.5)
    slope2_2_list = slope_list[(2*k + k//2):]
    slope2_2_list.arrange_in_grid(rows=1, buff=0.5).shift(DOWN*2.5)

    self.play(FadeIn(slope_list))

    path = PatternLines(patterns[0][1], order)

    animation_list = []
    for i in range(3*k - 1) :
      animation_list.append(AnimationGroup(
        Create(path[i]),
        Flash(slope_list[pattern_slopes[i]], num_lines=8, flash_radius=0.5),
        slope_list[pattern_slopes[i]].animate.set_color(YELLOW),
        run_time=0.4
      ))

    self.play(AnimationGroup(*animation_list, lag_ratio=1))
    self.wait()

class Induct5(Scene) :
  def construct(self) :
    patterns = VGroup(subp1(7), subp2(7), subp3(7), subp4(7)).scale(0.7)
    patterns.arrange_in_grid(rows=2, buff=(2, 1))
    patterns[0][0].set_color(RED)
    patterns[1][0].set_color(ORANGE)
    patterns[2][0].set_color(YELLOW)
    patterns[3][0].set_color(GREEN)
    self.add(patterns)

# 183526794
class Pattern0(ThreeDScene) :
  def construct(self) :

    PATTERN = [1, 8, 3, 5, 2, 6, 7, 9, 4]

    dots = Dots(3, 3)
    lines = PatternLines(dots, PATTERN)
    
    circles = VGroup()
    for y in range(-1, 2) :
      for x in range(-1, 2) :
        circles.add(Circle(radius=0.05, color=WHITE, fill_opacity=1).move_to([x, y, 0]))
    
    self.add(circles)
    self.wait(0.5)

    animation_list = []
    for i in range(len(lines)) :
      animation_list.append(AnimationGroup(
        Create(lines[i], run_time=0.3)
      ))
    
    self.play(AnimationGroup(*animation_list, lag_ratio=1))

    self.move_camera(phi=90*DEGREES, gamma=90*DEGREES, distance=1.2, run_time=2.5)
    self.wait()

class Banner(Scene) :
  def construct(self) :
    k = 9
    dots = Dots(k, 3)
    lines = VGroup()

    for i in range(1, (k//2)+1) :
      lines.add(Line([-i,0,0], [i,-1,0]))
      lines.add(Line([i,0,0], [-i,-1,0]))
    
    for i in range(k//2) :
      lines.add(Line([-i,1,0], [i+1,0,0]))
      lines.add(Line([i+1,1,0], [-i,0,0]))
    
    for i in range(k//2) :
      lines.add(Line([-i-1,1,0], [i,-1,0]))
      lines.add(Line([i+1,1,0], [-i,-1,0]))

    lines.add(Line([0,1,0],[0,0,0]))
    lines.add(Line([-(k//2),-1,0],[k//2,-1,0]))

    for line in lines :
      line.set_stroke(width=2, opacity=0.6)
    
    pattern = VGroup(lines, dots).scale(0.8)
    self.add(pattern)

class Thumbnail(Scene) :
  def construct(self) :
    pattern = Pattern(3, 3, [1,8,3,5,2,6,7,9,4])
    self.add(pattern)