# manim code used in chapters 1 to 3.

from manim import *

#############
# Functions #
#############


def Dots(width, height):
    x_offset, y_offset = (width - 1) / 2, (height - 1) / 2
    dots = VGroup()
    for y in reversed(range(height)):
        for x in range(width):
            dot = Dot([x - x_offset, y - y_offset, 0])
            dots.add(dot)
    return dots


def PatternPath(dots, pattern):
    path = VMobject()
    path.set_points_as_corners([dots[pos - 1].get_center() for pos in pattern])
    return path


def PatternLines(dots, pattern):
    lines = VGroup()
    dot_prev = dots[pattern[0] - 1]
    for pos in pattern[1:]:
        dot_curr = dots[pos - 1]
        lines.add(Line(start=dot_prev.get_center(), end=dot_curr.get_center()))
        dot_prev = dot_curr
    return lines


def Pattern(width, height, dotlist):
    pattern = VGroup()
    dots = Dots(width, height)
    lines = PatternLines(dots, dotlist)
    arrow_final = Arrow(
        start=lines[-1].get_start(),
        end=lines[-1].get_end(),
        stroke_width=4,
        buff=0,
        tip_length=0.2,
    )

    pattern.add(dots, lines[:-1], arrow_final)
    return pattern


def SlopeGroup(width, height):
    x_offset, y_offset = width / 2, abs(height) / 2
    group = VGroup()
    for y in range(abs(height) + 1):
        for x in range(width + 1):
            dot = Dot([x - x_offset, y - y_offset, 0])
            group.add(dot)

    if height > 0:
        line = Line(start=group[0].get_center(), end=group[-1].get_center())
    else:
        line = Line(
            start=group[-(width + 1)].get_center(), end=group[width].get_center()
        )

    group.add(line)
    return group


def Minigrids(width, height):
    grid_list = VGroup()
    w = width
    h = height
    while w < 3 and abs(h) < 3:
        for y in range(3 - abs(h)):
            for x in range(3 - w):
                grid = Dots(3, 3).scale(0.4)
                if h > 0:
                    start = x + 6 - 3 * y
                    end = (x + w) + 6 - 3 * (y + h)
                else:
                    start = x + 6 - 3 * (y - h)
                    end = (x + w) + 6 - 3 * y
                grid.add(
                    Line(start=grid[start].get_center(), end=grid[end].get_center())
                )
                grid_list.add(grid)
        w += width
        h += height
    if len(grid_list) > 7:
        grid_list.arrange_in_grid(rows=2, buff=0.7)
    else:
        grid_list.arrange_in_grid(buff=0.7)
    return grid_list


def GloriousList():
    patterns = VGroup()
    file = open("3x3mcp_unique.txt", "r")
    for line in file:
        dotlist = list(map(int, line.split()))
        pattern = Pattern(3, 3, dotlist)
        patterns.add(pattern)
    return patterns


def GloriousList2():
    patterns = VGroup()
    file = open("3x3mcp_unique.txt", "r")
    for line in file:
        dotlist = list(map(int, line.split()))
        pattern = Pattern(3, 3, dotlist)
        text = Text(line).scale(0.5).next_to(pattern, DOWN)
        patterns.add(VGroup(pattern, text))
    return patterns


###############
# Test Scenes #
###############


class Thumbnail(Scene):
    def construct(self):
        dots = VGroup()
        for y in reversed(range(3)):
            for x in range(3):
                dot = Dot([x - 1, y - 1, 0])
                dots.add(dot)

        self.camera.background_color = WHITE
        pattern = Pattern(3, 3, [1, 8, 3, 5, 2, 6, 7, 9, 4])
        pattern.set_color(BLACK)
        for i in range(1, 9):
            pattern[0][i].set_fill(opacity=0)
            pattern[0][i].set_stroke(color=BLACK, width=2)
        self.add(pattern)


class DrawGrid(Scene):
    def construct(self):
        GRID_W, GRID_H = 3, 3
        dots = Dots(GRID_W, GRID_H)
        self.add(dots)


class DrawPattern(Scene):
    def construct(self):
        GRID_W, GRID_H = 3, 3
        PATTERN = [1, 8, 3, 5, 2, 6, 7, 9, 4]

        dots = Dots(GRID_W, GRID_H)
        path = PatternPath(dots, PATTERN)

        self.play(FadeIn(dots))
        self.play(Create(path, lag_ratio=2, run_time=1.5), rate_func=linear)
        self.wait()


class DrawPatternSlow(Scene):
    def construct(self):
        GRID_W, GRID_H = 3, 3
        PATTERN = [1, 8, 3, 5, 2, 6, 7, 9, 4]

        dots = Dots(GRID_W, GRID_H)
        lines = PatternLines(dots, PATTERN)

        self.play(FadeIn(dots))
        self.play(
            AnimationGroup(*[Create(line, run_time=0.5) for line in lines], lag_ratio=1)
        )
        self.wait()


#################
# Actual Scenes #
#################


# android rule 3
class Pattern1(Scene):
    def construct(self):
        pattern = [1, 2, 3, 6, 9]

        dots = Dots(3, 3)
        path1 = PatternPath(dots, pattern)

        self.play(FadeIn(dots), run_time=0.3)

        self.play(Create(path1, run_time=0.8))
        self.wait(0.3)
        self.play(FadeOut(path1), run_time=0.2)
        self.wait(0.3)

        path1.reverse_direction()
        self.play(Create(path1, run_time=0.8))
        self.wait(0.3)
        self.play(FadeOut(path1), run_time=0.2)
        self.wait()


# slope number difference
class Pattern2(Scene):
    def construct(self):
        pattern1 = [1, 2, 3, 6, 5, 4, 7, 8, 9]
        pattern2 = [1, 8, 3, 6, 2, 9, 4, 5, 7]

        dots1 = Dots(3, 3).shift(LEFT * 2)
        dots2 = Dots(3, 3).shift(RIGHT * 2)
        lines1 = PatternLines(dots1, pattern1)
        lines2 = PatternLines(dots2, pattern2)

        self.play(FadeIn(dots1, dots2), run_time=0.3)
        self.wait(0.5)

        self.play(
            AnimationGroup(
                *[Create(line, run_time=0.08) for line in lines1], lag_ratio=1
            )
        )
        self.wait()

        self.play(
            AnimationGroup(
                *[Create(line, run_time=0.15) for line in lines2], lag_ratio=1
            )
        )
        self.wait()


# slope difference visualizing
class Pattern3(Scene):
    def construct(self):
        pattern1 = [1, 2, 3, 6, 5, 4, 7, 8, 9]
        pattern2 = [1, 8, 3, 6, 2, 9, 4, 5, 7]

        dots1 = Dots(3, 3).shift(LEFT * 2)
        dots2 = Dots(3, 3).shift(RIGHT * 2)
        lines1 = PatternLines(dots1, pattern1)
        lines1_copy = lines1.copy()
        lines2 = PatternLines(dots2, pattern2)
        lines2_copy = lines2.copy()
        self.add(dots1, dots2, lines1_copy, lines2_copy)
        self.wait()

        slopes1 = [[1, 0], [0, 1]]

        slopes2 = [[1, 0], [0, 1], [1, 1], [1, -1], [1, 2], [1, -2], [2, -1]]

        # draw all slopes
        slope_list1 = VGroup()
        for w, h in slopes1:
            slopegroup = Line(ORIGIN, [w, h, 0], color=GRAY).scale(0.5)
            slope_list1.add(slopegroup)
        slope_list1.arrange_in_grid(rows=1, buff=0.8).next_to(dots1, DOWN, buff=0.5)

        slope_list2 = VGroup()
        for w, h in slopes2:
            slopegroup = Line(ORIGIN, [w, h, 0], color=GRAY).scale(0.3)
            slope_list2.add(slopegroup)
        slope_list2.arrange_in_grid(rows=2, buff=0.4).next_to(dots2, DOWN, buff=0.5)

        self.play(
            AnimationGroup(
                FadeTransform(lines1[0], slope_list1[0], run_time=1.5),
                FadeTransform(lines1[1], slope_list1[0], run_time=1.5),
                FadeTransform(lines1[2], slope_list1[1], run_time=1.5),
                FadeTransform(lines1[3], slope_list1[0], run_time=1.5),
                FadeTransform(lines1[4], slope_list1[0], run_time=1.5),
                FadeTransform(lines1[5], slope_list1[1], run_time=1.5),
                FadeTransform(lines1[6], slope_list1[0], run_time=1.5),
                FadeTransform(lines1[7], slope_list1[0], run_time=1.5),
            )
        )
        self.wait(2)

        self.play(
            AnimationGroup(
                FadeTransform(lines2[0], slope_list2[5], run_time=1.5),
                FadeTransform(lines2[1], slope_list2[4], run_time=1.5),
                FadeTransform(lines2[2], slope_list2[1], run_time=1.5),
                FadeTransform(lines2[3], slope_list2[3], run_time=1.5),
                FadeTransform(lines2[4], slope_list2[5], run_time=1.5),
                FadeTransform(lines2[5], slope_list2[6], run_time=1.5),
                FadeTransform(lines2[6], slope_list2[0], run_time=1.5),
                FadeTransform(lines2[7], slope_list2[2], run_time=1.5),
            )
        )
        self.wait()


# glorious list
class AllPatterns(Scene):
    def construct(self):
        patterns = GloriousList()
        patterns.arrange_in_grid(rows=4, buff=0.5)
        self.add(patterns)
        self.play(patterns.animate.scale(0.5), run_time=10)


# glorious list animation
class AllPatterns0(MovingCameraScene):
    def construct(self):
        patterns = GloriousList2().scale(0.7)
        patterns.arrange_in_grid(cols=3, buff=(1, 0.5))
        self.add(patterns)
        self.camera.frame.move_to(patterns.get_top() + UP * 5)

        self.play(
            AnimationGroup(
                self.camera.frame.animate(run_time=10, rate_func=linear).move_to(
                    patterns.get_bottom() + UP * 3
                ),
                AnimationGroup(
                    *[
                        AnimationGroup(
                            Create(pattern[0], run_time=80 / 37), FadeIn(pattern[1])
                        )
                        for pattern in patterns
                    ],
                    lag_ratio=0.1
                ),
            )
        )
        self.wait(2)


class AllPatterns1(Scene):
    def construct(self):
        patterns = GloriousList()
        corners = patterns[:11]
        corners.scale(0.7)
        corners.arrange_in_grid(rows=3, buff=0.5)
        self.play(
            AnimationGroup(
                *[FadeIn(c[0]) for c in corners], *[Create(c[1:]) for c in corners]
            )
        )
        self.wait()


class AllPatterns2(Scene):
    def construct(self):
        patterns = GloriousList()
        edges = patterns[11:30]
        edges.scale(0.5)
        edges.arrange_in_grid(rows=3, buff=0.5)
        self.play(
            AnimationGroup(
                *[FadeIn(c[0]) for c in edges], *[Create(c[1:]) for c in edges]
            )
        )
        self.wait()


class AllPatterns3(Scene):
    def construct(self):
        patterns = GloriousList()
        middle = patterns[30:]
        middle.scale(0.8)
        middle.arrange_in_grid(rows=2, buff=0.5)
        self.play(
            AnimationGroup(
                *[FadeIn(c[0]) for c in middle], *[Create(c[1:]) for c in middle]
            )
        )
        self.wait()


# go over dots multiple times
class AllPatterns4(Scene):
    def construct(self):
        patterns = GloriousList()
        go_over_dot = {
            1: 5,
            2: 5,
            3: 5,
            6: 6,
            7: 5,
            8: 6,
            9: 6,
            13: 4,
            14: 5,
            15: 5,
            16: 5,
            19: 6,
            20: 5,
            22: 6,
            24: 5,
            25: 6,
            26: 6,
            27: 2,
            32: 6,
            33: 8,
            34: 6,
        }

        subset = VGroup()
        for key in go_over_dot:
            pattern = patterns[key]
            reddot = pattern[0][go_over_dot[key] - 1].copy().set_color(RED)
            pattern.add(reddot)
            subset.add(pattern)

        subset.scale(0.6)
        subset.arrange_in_grid(rows=3, buff=0.5)
        self.play(
            AnimationGroup(
                *[FadeIn(c[0]) for c in subset], *[Create(c[1:3]) for c in subset]
            )
        )
        for c in subset:
            c[-1].scale(1.5)

        self.play(
            AnimationGroup(
                *[FadeIn(c[-1]) for c in subset],
                *[Flash(c[-1], color=RED, num_lines=8) for c in subset]
            )
        )
        self.wait()


# star
class AllPatterns5(Scene):
    def construct(self):
        pattern = [1, 6, 2, 9, 8, 3, 4, 7, 5]
        lines = Pattern(3, 3, pattern).scale(1.5)
        self.add(lines)


class AllPatterns6(Scene):
    def construct(self):
        patterns = [
            [1, 6, 2, 9, 8, 3, 4, 7, 5],
            [8, 3, 4, 5, 7, 1, 6, 2, 9],
            [8, 3, 4, 1, 6, 2, 9, 7, 5],
            [5, 7, 4, 3, 8, 9, 2, 6, 1],
        ]
        lines = VGroup()
        for pattern in patterns:
            lines.add(Pattern(3, 3, pattern))
        lines.arrange_in_grid(rows=1, buff=0.5)
        self.play(
            AnimationGroup(
                *[FadeIn(c[0]) for c in lines], *[Create(c[1:]) for c in lines]
            )
        )
        self.wait()


# most polygons
class AllPatterns7(Scene):
    def construct(self):
        patterns = [[1, 5, 6, 7, 3, 8, 2, 9, 4], [2, 5, 7, 6, 4, 9, 1, 8, 3]]
        lines = VGroup()
        for pattern in patterns:
            lines.add(Pattern(3, 3, pattern))
        lines.scale(1.5).arrange_in_grid(rows=1, buff=1)
        self.add(lines)


# all slopes
class Scene1(Scene):
    def construct(self):
        slopes = [[1, 0], [0, 1], [1, 1], [1, -1], [1, 2], [1, -2], [2, 1], [2, -1]]

        # draw all slopes
        slope_list = VGroup()
        for w, h in slopes:
            slopegroup = SlopeGroup(w, h).scale(0.5)
            slope_list.add(slopegroup)
        slope_list.arrange_in_grid(rows=1, buff=0.8, row_alignments="d")

        self.play(Create(slope_list[0]), run_time=0.5)
        self.wait(0.5)
        self.play(Create(slope_list[1]), run_time=0.5)
        self.wait(0.5)
        self.play(Create(slope_list[2:4]), run_time=0.5)
        self.wait(0.7)
        self.play(Create(slope_list[4:]), run_time=1)
        self.wait(1)


# slope text
class Scene2(Scene):
    def construct(self):
        slopes = [[1, 0], [0, 1], [1, 1], [1, -1], [1, 2], [1, -2], [2, 1], [2, -1]]
        slope_texts = ["0", r"\infty", "1", "-1", "2", "-2", "1/2", "-1/2"]

        # slope
        slope_list = VGroup()
        for w, h in slopes:
            slopegroup = SlopeGroup(w, h).scale(0.5)
            slope_list.add(slopegroup)
        slope_list.arrange_in_grid(rows=1, buff=0.8, row_alignments="d")
        self.play(Create(slope_list))
        self.wait()

        # draw
        def slope_text(i):
            text = MathTex(slope_texts[i]).next_to(slope_list[i], DOWN)
            text.move_to([text.get_x(), -1.2, 0])
            return text

        def slope_text_group(i):
            return AnimationGroup(
                Flash(
                    slope_list[i],
                    color=WHITE,
                    run_time=0.5,
                    num_lines=8,
                    flash_radius=0.5,
                ),
                FadeIn(slope_text(i), run_time=0.5),
                lag_ratio=0.7,
            )

        self.play(slope_text_group(0))
        self.wait()
        self.play(slope_text_group(6))
        self.wait()
        self.play(AnimationGroup(*[FadeIn(slope_text(i)) for i in [2, 3, 4, 5, 7]]))
        self.wait()
        self.play(slope_text_group(1))
        self.wait()


# dot text
class Scene3(Scene):
    def construct(self):
        dots = Dots(3, 3).scale(1.3)
        self.play(FadeIn(dots), run_time=0.3)

        def dot_text(i):
            text = Text(str(i + 1)).scale(0.5).next_to(dots[i], LEFT)
            text.shift(UP * 0.2)
            return text

        self.play(
            AnimationGroup(
                *[FadeIn(dot_text(i), run_time=0.2) for i in range(9)], lag_ratio=0.5
            )
        )
        self.wait()


# try making one
class Scene4(Scene):
    def construct(self):
        GRID_W, GRID_H = 3, 3
        slopes = [[1, 0], [0, 1], [1, 1], [1, -1], [1, 2], [1, -2], [2, 1], [2, -1]]

        PATTERN = [1, 8, 3, 4, 9, 6, 2]
        PATTERN_SLOPES = [5, 4, 6, 7, 1, 3]

        dots = Dots(GRID_W, GRID_H).shift(UP)
        lines = PatternLines(dots, PATTERN)

        # draw all slopes
        slope_list = VGroup()
        for w, h in slopes:
            slopegroup = SlopeGroup(w, h).scale(0.5)
            slope_list.add(slopegroup)

        slope_list.arrange_in_grid(rows=1, buff=0.8)
        slope_list.shift(DOWN * 2)
        self.add(slope_list)

        self.add(dots)
        self.wait(2)
        self.play(Flash(dots[PATTERN[0] - 1], color=WHITE, num_lines=8))
        self.wait(0.5)

        anim_list = []
        for i in range(len(lines)):
            anim_list.append(
                AnimationGroup(
                    Create(lines[i], run_time=0.5),
                    Flash(
                        slope_list[PATTERN_SLOPES[i]],
                        run_time=0.5,
                        num_lines=8,
                        flash_radius=0.5,
                    ),
                    slope_list[PATTERN_SLOPES[i]]
                    .animate(run_time=0.5)
                    .set_color(YELLOW),
                )
            )

        self.play(AnimationGroup(*anim_list, lag_ratio=1.2))
        self.wait()

        # impossible moves
        line1 = Line(start=dots[1].get_center(), end=dots[4].get_center(), color=RED)
        line2 = Line(start=dots[1].get_center(), end=dots[6].get_center(), color=RED)

        self.play(
            AnimationGroup(
                Create(line1, run_time=0.5),
                lines[4].animate(run_time=0.5).set_color(RED),
            )
        )
        self.wait()
        self.play(
            AnimationGroup(
                FadeOut(line1, run_time=0.5),
                lines[4].animate(run_time=0.5).set_color(WHITE),
            )
        )
        self.play(
            AnimationGroup(
                Create(line2, run_time=0.5),
                lines[1].animate(run_time=0.5).set_color(RED),
            )
        )
        self.wait()
        self.play(
            AnimationGroup(
                FadeOut(line2, run_time=0.5),
                lines[1].animate(run_time=0.5).set_color(WHITE),
            )
        )


# 183526794
class Scene5(Scene):
    def construct(self):
        slopes = [[1, 0], [0, 1], [1, 1], [1, -1], [1, 2], [1, -2], [2, 1], [2, -1]]

        PATTERN = [1, 8, 3, 5, 2, 6, 7, 9, 4]
        PATTERN_SLOPES = [5, 4, 2, 1, 3, 6, 0, 7]

        dots = Dots(3, 3).shift(UP)
        lines = PatternLines(dots, PATTERN)

        # draw all slopes
        slope_list = VGroup()
        for w, h in slopes:
            slopegroup = SlopeGroup(w, h).scale(0.5)
            slope_list.add(slopegroup)

        slope_list.arrange_in_grid(rows=1, buff=0.8)
        slope_list.shift(DOWN * 2)
        self.add(slope_list)
        self.add(dots)
        self.wait(0.5)

        self.play(Flash(dots[PATTERN[0] - 1], color=WHITE, num_lines=8), run_time=0.5)
        self.wait(0.5)

        animation_list = []
        for i in range(len(lines)):
            animation_list.append(
                AnimationGroup(
                    Create(lines[i], run_time=0.5),
                    Flash(
                        slope_list[PATTERN_SLOPES[i]],
                        run_time=0.5,
                        num_lines=8,
                        flash_radius=0.5,
                    ),
                    slope_list[PATTERN_SLOPES[i]]
                    .animate(run_time=0.5)
                    .set_color(YELLOW),
                )
            )

        self.play(AnimationGroup(*animation_list, lag_ratio=1))
        self.wait()


# 129483675
class Scene6(Scene):
    def construct(self):
        slopes = [[1, 0], [0, 1], [1, 1], [1, -1], [1, 2], [1, -2], [2, 1], [2, -1]]

        pattern = [1, 2, 9, 4, 8, 3, 6, 7, 5]
        pattern_slopes = [0, 5, 7, 3, 4, 1, 6, 2]
        minigrid_ans = [None, None, 0, 0, 1, 5, 0, 0]

        dots = Dots(3, 3)
        lines = PatternLines(dots, pattern)

        # draw all slopes
        slope_list = VGroup()
        for w, h in slopes:
            slopegroup = SlopeGroup(w, h).scale(0.3)
            slope_list.add(slopegroup)

        slope_list.arrange_in_grid(cols=2, buff=0.4)
        slope_list.shift(RIGHT * 5.5)
        slope_list[0].set_color(YELLOW)

        self.play(
            AnimationGroup(
                FadeIn(dots, run_time=0.5),
                Create(lines[0]),
                FadeIn(slope_list),
                lag_ratio=1.5,
            )
        )
        self.wait(0.5)

        def step(i, time, wait):
            anim_list = []
            anim_list.append(
                AnimationGroup(
                    Indicate(slope_list[pattern_slopes[i]]),
                    Flash(slope_list[pattern_slopes[i]], flash_radius=0.5, num_lines=8),
                )
            )
            minigrid = Minigrids(*slopes[pattern_slopes[i]]).shift(DOWN * 2)
            anim_list.append(FadeIn(minigrid))
            anim_list.append(minigrid[minigrid_ans[i]].animate.set_color(YELLOW))
            anim_list.append(
                AnimationGroup(
                    Create(lines[i]),
                    slope_list[pattern_slopes[i]].animate.set_color(YELLOW),
                )
            )
            anim_list.append(FadeOut(minigrid))

            for anim in anim_list:
                self.play(anim, run_time=time)
                self.wait(wait)

        minigrids1 = Minigrids(1, -2).shift(DOWN * 2)

        lines[1:].shift(UP)

        self.play(
            AnimationGroup(
                Indicate(slope_list[pattern_slopes[1]]),
                Flash(slope_list[pattern_slopes[1]], flash_radius=0.5, num_lines=8),
            )
        )
        self.wait(0.5)
        self.play(
            AnimationGroup(
                FadeIn(minigrids1), dots.animate.shift(UP), lines[0].animate.shift(UP)
            )
        )
        self.wait(0.5)
        templine = Line(start=dots[0].get_center(), end=dots[7].get_center(), color=RED)
        self.play(
            AnimationGroup(minigrids1[0].animate.set_color(RED), FadeIn(templine))
        )
        self.wait(0.5)
        self.play(FadeOut(templine))

        self.play(
            AnimationGroup(
                minigrids1[1].animate.set_color(YELLOW),
                slope_list[pattern_slopes[1]].animate.set_color(YELLOW),
                Create(lines[1]),
            )
        )
        self.wait(0.5)
        self.play(FadeOut(minigrids1))

        step(2, 1, 0.5)
        step(3, 0.5, 0)
        step(4, 0.5, 0)
        step(5, 0.3, 0)
        step(6, 0.3, 0)
        step(7, 0.7, 0)


# rotating/flipping
class Scene7(Scene):
    def construct(self):
        slopes = [[1, 0], [0, 1], [1, 1], [1, -1], [1, 2], [1, -2], [2, 1], [2, -1]]
        pattern = [1, 8, 3, 5, 2, 6, 7, 9, 4]
        dots = Dots(3, 3)
        lines = PatternLines(dots, pattern)

        patterns = VGroup(VGroup(dots, lines))
        for i in range(3):
            patterns.add(patterns[-1].copy().rotate(-PI / 2))

        patterns.arrange_in_grid(rows=1, buff=1)

        self.add(patterns)
        self.wait(0.5)
        for i in range(3, 0, -1):
            self.play(ReplacementTransform(patterns[i], patterns[i - 1]), run_time=0.5)

        self.wait()
