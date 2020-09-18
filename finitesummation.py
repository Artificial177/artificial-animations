from manimlib.imports import *

PINK = "#f57ddd"
BBLUE = "#7dcbf5"
GGREEN = "#7df5ad"
ORANGE = "#f5aa31"

class nSummation(Scene):
   def construct(self):

      t1 = TexMobject("1").to_corner(UL)
      t2 = TexMobject("2").next_to(t1, 4*DOWN)
      t3 = TexMobject("3").next_to(t2, 4*DOWN)
      t4 = TexMobject("4").next_to(t3, 4*DOWN)
      t5 = TexMobject("5").next_to(t4, 4*DOWN)

      square1 = Square().scale(0.2).next_to(t1, RIGHT).set_color(ORANGE)
      square2 = Square().scale(0.2).next_to(t2, RIGHT)
      square21 = Square().scale(0.2).next_to(square2, RIGHT/100)
      squareset2 = VGroup(square2, square21).set_color(PINK)
      square3 = Square().scale(0.2).next_to(t3, RIGHT)
      square31 = Square().scale(0.2).next_to(square3, RIGHT/100)
      square32 = Square().scale(0.2).next_to(square31, RIGHT/100)
      squareset3 = VGroup(square3, square31, square32).set_color(BBLUE)
      square4 = Square().scale(0.2).next_to(t4, RIGHT)
      square41 = Square().scale(0.2).next_to(square4, RIGHT/100)
      square42 = Square().scale(0.2).next_to(square41, RIGHT/100)
      square43 = Square().scale(0.2).next_to(square42, RIGHT/100)
      squareset4 = VGroup(square4, square41, square42, square43).set_color(GGREEN)
      square5 = Square().scale(0.2).next_to(t5, RIGHT)
      square51 = Square().scale(0.2).next_to(square5, RIGHT/100)
      square52 = Square().scale(0.2).next_to(square51, RIGHT/100)
      square53 = Square().scale(0.2).next_to(square52, RIGHT/100)
      square54 = Square().scale(0.2).next_to(square53, RIGHT/100)
      squareset5 = VGroup(square5, square51, square52, square53, square54).set_color(YELLOW)

      square1new = Square().scale(0.3).move_to(ORIGIN).set_color(ORANGE)
      square2new = Square().scale(0.3)
      square21new = Square().scale(0.3).next_to(square2new, RIGHT/100)
      squareset2new = VGroup(square2new, square21new).set_color(PINK)
      square3new = Square().scale(0.3)
      square31new = Square().scale(0.3).next_to(square3new, RIGHT/100)
      square32new = Square().scale(0.3).next_to(square31new, RIGHT/100)
      squareset3new = VGroup(square3new, square31new, square32new).set_color(BBLUE)
      square4new = Square().scale(0.3)
      square41new = Square().scale(0.3).next_to(square4new, RIGHT/100)
      square42new = Square().scale(0.3).next_to(square41new, RIGHT/100)
      square43new = Square().scale(0.3).next_to(square42new, RIGHT/100)
      squareset4new = VGroup(square4new, square41new, square42new, square43new).set_color(GGREEN)
      square5new = Square().scale(0.3)
      square51new = Square().scale(0.3).next_to(square5new, RIGHT/100)
      square52new = Square().scale(0.3).next_to(square51new, RIGHT/100)
      square53new = Square().scale(0.3).next_to(square52new, RIGHT/100)
      square54new = Square().scale(0.3).next_to(square53new, RIGHT/100)
      squareset5new = VGroup(square5new, square51new, square52new, square53new, square54new).set_color(YELLOW)

      square1new2 = Square().scale(0.3).move_to(ORIGIN).set_color(ORANGE)
      square2new2 = Square().scale(0.3)
      square21new2 = Square().scale(0.3).next_to(square2new2, RIGHT/100)
      squareset2new2 = VGroup(square2new2, square21new2).set_color(PINK)
      square3new2 = Square().scale(0.3)
      square31new2 = Square().scale(0.3).next_to(square3new2, RIGHT/100)
      square32new2 = Square().scale(0.3).next_to(square31new2, RIGHT/100)
      squareset3new2 = VGroup(square3new2, square31new2, square32new2).set_color(BBLUE)
      square4new2 = Square().scale(0.3)
      square41new2 = Square().scale(0.3).next_to(square4new2, RIGHT/100)
      square42new2 = Square().scale(0.3).next_to(square41new2, RIGHT/100)
      square43new2 = Square().scale(0.3).next_to(square42new2, RIGHT/100)
      squareset4new2 = VGroup(square4new2, square41new2, square42new2, square43new2).set_color(GGREEN)
      square5new2 = Square().scale(0.3)
      square51new2 = Square().scale(0.3).next_to(square5new2, RIGHT/100)
      square52new2 = Square().scale(0.3).next_to(square51new2, RIGHT/100)
      square53new2 = Square().scale(0.3).next_to(square52new2, RIGHT/100)
      square54new2 = Square().scale(0.3).next_to(square53new2, RIGHT/100)
      squareset5new2 = VGroup(square5new2, square51new2, square52new2, square53new2, square54new2).set_color(YELLOW)

      texthold3 = TextMobject("1")
      texthold2 = TextMobject("1").next_to(texthold3, UP)
      texthold1 = TextMobject("1").next_to(texthold2, UP)
      texthold4 = TextMobject("1").next_to(texthold3, DOWN)
      texthold5 = TextMobject("1").next_to(texthold4, DOWN)

      textholdset1 = VGroup(texthold1, texthold2, texthold3, texthold4, texthold5).shift(LEFT*2)

      square1new = square1new.next_to(texthold1, RIGHT)
      squareset2new = squareset2new.next_to(texthold2, RIGHT)
      squareset3new = squareset3new.next_to(texthold3, RIGHT)
      squareset4new = squareset4new.next_to(texthold4, RIGHT)
      squareset5new = squareset5new.next_to(texthold5, RIGHT)

      square1new2 = square1new2.next_to(squareset5new, RIGHT/100)
      squareset2new2 = squareset2new2.next_to(squareset4new, RIGHT/100)
      squareset3new2 = squareset3new2.next_to(squareset3new, RIGHT/100)
      squareset4new2 = squareset4new2.next_to(squareset2new, RIGHT/100)
      squareset5new2 = squareset5new2.next_to(square1new, RIGHT/100)

      b6holder = Rectangle(width=12, height=1).scale(0.3).next_to(texthold5, RIGHT)
      b3holder = Rectangle(height=10, width=1).scale(0.3).next_to(texthold3, 14*RIGHT)

      b6b = Brace(b6holder, 2*DOWN)
      b6text = b6b.get_tex("6")
      b5b = Brace(b3holder, RIGHT)
      b5text = b5b.get_tex("5")

      brace6 = VGroup(b6b, b6text)
      brace5 = VGroup(b5b, b5text)

      textafter = TexMobject("2", #0
                             "(", #1
                             "1", #2
                             "+", #3
                             "2", #4
                             "+", #5
                             "3", #6
                             "+", #7
                             "4", #8
                             "+", #9
                             "5", #10
                             ")", #11
                             "=", #12
                             "5", #13
                             "\\times", #14
                             "6" #15
                             ).scale(1.5)

      textafter2 = TexMobject("1",
                              "+",
                              "2", #4
                              "+", #5
                              "3", #6
                              "+", #7
                              "4", #8
                              "+", #9
                              "5", #10
                              "=", #12
                              "\\frac{5\\times{6}}{2}"
                              ).scale(1.5)

      textafter3 = TexMobject("1", #2
                              "+", #3
                              "2", #4
                              "+", #5
                              "3", #6
                              "+", #7
                              "4", #8
                              "+", #9
                              "5", #10
                              "=", #12
                              "\\frac{5\\times{(5+1)}}{2}"
                              ).scale(1.5)

      textlater = TexMobject("1", #2
                              "+", #3
                              "2", #4
                              "+", #5
                              "3", #6
                              "+", #7
                              "4...", #8
                              "+", #9
                              "n", #10
                              "=", #12
                              "\\frac{{n\\times{(n+1)}}}{{2}}"
                              ).scale(1.5)

      textfinal = TexMobject("\\sum_{k=1}^n{\,}k=\\frac{{n(n+1)}}{2}").scale(1.5)








      self.play(ShowCreation(t1), ShowCreation(t2), ShowCreation(t3), ShowCreation(t4), ShowCreation(t5))

      self.wait(1)

      self.play(ShowCreation(square1), ShowCreation(squareset2), ShowCreation(squareset3), ShowCreation(squareset4), ShowCreation(squareset5))



      self.play(ReplacementTransform(square1.copy(), square1new),
                ReplacementTransform(squareset2.copy(), squareset2new),
                ReplacementTransform(squareset3.copy(), squareset3new),
                ReplacementTransform(squareset4.copy(), squareset4new),
                ReplacementTransform(squareset5.copy(), squareset5new))

      self.wait(1.25)

      self.play(ReplacementTransform(square1.copy(), square1new2),
                ReplacementTransform(squareset2.copy(), squareset2new2),
                ReplacementTransform(squareset3.copy(), squareset3new2),
                ReplacementTransform(squareset4.copy(), squareset4new2),
                ReplacementTransform(squareset5.copy(), squareset5new2))

      self.wait(1)

      self.play(ShowCreation(brace5), ShowCreation(brace6))

      self.wait(1.5)

      self.play(FadeOut(square1), FadeOut(squareset2), FadeOut(squareset3), FadeOut(squareset4), FadeOut(squareset5),
                FadeOut(square1new), FadeOut(squareset2new), FadeOut(squareset3new), FadeOut(squareset4new), FadeOut(squareset5new),
                FadeOut(square1new2), FadeOut(squareset2new2), FadeOut(squareset3new2), FadeOut(squareset4new2), FadeOut(squareset5new2),
                FadeOut(b6b), FadeOut(b5b))

      self.play(Write(textafter[0:2]),
                ReplacementTransform(t1, textafter[2]),
                Write(textafter[3]),
                ReplacementTransform(t2, textafter[4]),
                Write(textafter[5]),
                ReplacementTransform(t3, textafter[6]),
                Write(textafter[7]),
                ReplacementTransform(t4, textafter[8]),
                Write(textafter[9]),
                ReplacementTransform(t5, textafter[10]),
                Write(textafter[11:13]),
                ReplacementTransform(b5text, textafter[13]),
                Write(textafter[14]),
                ReplacementTransform(b6text, textafter[15]))

      self.wait(1)

      self.play(ReplacementTransform(textafter, textafter2))

      self.wait(1.25)

      self.play(ReplacementTransform(textafter2, textafter3))

      self.wait(1.25)

      self.play(ReplacementTransform(textafter3, textlater))

      self.wait(1.25)

      self.play(ReplacementTransform(textlater, textfinal))

      self.wait(1)


class InfiniteSummation(Scene):
   def construct(self):
      ins1 = TextMobject("But what about an infinite summation?").to_edge(UP).scale(1.5)

      textfinal = TexMobject("\\sum_{k=1}^n{\,}k=\\frac{{n(n+1)}}{2}").scale(1.5)

      textfinal2 = TexMobject("\\sum_{k=1}^\infty{\,}k=\\frac{{n(n+1)}}{2}").scale(1.5)

      s21 = TexMobject("S_2=")
      s11 = TexMobject("S_1=1-1+1-1+1-1...").scale(1.5).next_to(s21, UP)


      self.add(textfinal)

      self.wait(1)

      self.play(Write(ins1))

      self.wait(0.5)

      self.play(ReplacementTransform(textfinal, textfinal2))



















