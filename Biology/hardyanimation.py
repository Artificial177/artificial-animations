from manimlib.imports import *


class HardyIntroduction(Scene):
   def construct(self):
      hook1 = TextMobject("Darwin", " gave us the ideas of natural selection.").shift(UP).scale(1.2)
      hook1[0].set_color(GREEN)
      hook2 = TextMobject("Mendel", " provided us with the basic principles of \\\\ genetics and heredity.").scale(1.2).shift(DOWN/4)
      hook2[0].set_color(GREEN)
      hook3 = TextMobject("And yet, neither, despite living in the same time period, \\\\ were able to fit their "
                          "ideas together.")
      hook3.scale(1.1)

      afterhook1 = TextMobject("The field of ", "Population Genetics", " can explain exactly \\\\ how their "
                                                                              "ideas fit together.").shift(2.25 * UP)
      afterhook1[1].set_color(GREEN)

      thecircle = Circle().scale(2).shift(DOWN)
      incircle = TextMobject("Population").shift(DOWN)

      selectiontext = TextMobject("Selection").set_color(BLUE).shift(DOWN/3, 5*LEFT)
      selectionarrow = Arrow(selectiontext.get_right(), thecircle.get_left()).shift(UP/4)
      selection = VGroup(selectiontext, selectionarrow)
      selectiontext.shift(UP/4)

      migrationtext = TextMobject("Migration").set_color(RED).shift(7*DOWN/3, 5*LEFT)
      migrationarrow = Arrow(migrationtext.get_right(), thecircle.get_left()).shift(DOWN/4)
      migration = VGroup(migrationtext, migrationarrow)
      migrationtext.shift(UP/4)

      mutationtext = TextMobject("Mutation").set_color(YELLOW).shift(DOWN/3, 5*RIGHT)
      mutationarrow = Arrow(mutationtext.get_left(), thecircle.get_right()).shift(UP/4)
      mutation = VGroup(mutationtext, mutationarrow)


      genetictext = TextMobject("Genetic Drift").set_color(GREEN).shift(7*DOWN/3, 5*RIGHT)
      geneticarrow = Arrow(genetictext.get_left(), thecircle.get_right()).shift(DOWN/4)
      genetic = VGroup(genetictext, geneticarrow)

      evolutiontext = TextMobject("Evolution").to_edge(DOWN).shift(DOWN/3)
      evolutionarrow = Arrow(thecircle.get_bottom(), evolutiontext.get_top())
      evolution = VGroup(evolutiontext, evolutionarrow)

      afterafter1 = TextMobject("Today, we're going to be focusing on an important aspect of population genetics:").scale(0.8).shift(UP/2)

      afterafterBIG = TextMobject("The Hardy-Weinberg Theorem").scale(1).shift(0.5*DOWN)

      self.play(Write(hook1))

      self.wait(1.5)

      self.play(Write(hook2))

      self.wait(1.5)

      self.play(FadeOut(hook1), FadeOut(hook2))

      self.wait(0.5)

      self.play(Write(hook3))

      self.wait(2)

      self.play(ReplacementTransform(hook3, afterhook1))

      self.wait(1)

      self.play(ShowCreation(thecircle),
                ShowCreation(incircle),
                ShowCreation(selection),
                ShowCreation(migration),
                ShowCreation(mutation),
                ShowCreation(genetic),
                ShowCreation(evolution),
                run_time=5
                )

      self.wait(2)

      self.play(FadeOut(afterhook1),
                FadeOut(thecircle),
                FadeOut(incircle),
                FadeOut(selection),
                FadeOut(migration),
                FadeOut(mutation),
                FadeOut(genetic),
                FadeOut(evolution),
                run_time=2
                )

      self.play(Write(afterafter1))

      self.wait(0.5)

      self.play(Write(afterafterBIG))

      self.wait(1.5)

      self.play(FadeOut(afterafter1), FadeOut(afterafterBIG))

      self.wait(0.5)

class ExplainHardy(Scene):
   def construct(self):
      thisishardy = TextMobject("The Hardy-Weinberg Theorem gives a set of conditions in biology called: ").scale(0.85).shift(UP/4)
      thisishardy.scale(0.8)
      thisisactualhardy = TextMobject("Hardy-Weinberg Equilibrium").shift(DOWN/4).scale(0.8)

      explainhardybegin = TextMobject("The conditions for Hardy-Weinberg Equilibrium are:")
      explainhardynewpos = TextMobject("The conditions for Hardy-Weinberg Equilibrium are:").to_edge(UP)

      hardyconditions = TextMobject("1. Infinite Population Size",
                                    "\\\\2. Random Mating",
                                    "\\\\3. No Mutation",
                                    "\\\\4. No Gene Flow",
                                    "\\\\5. No Natural Selection"
                                    ).to_edge(UP).shift(2*DOWN/3).scale(0.8)

      holder = Ellipse().scale(3).shift(2*DOWN)
      con1text = TexMobject("\infty").scale(3).shift(2*DOWN)

      pop1 = TextMobject("o")
      pop1.set_color(RED).shift(3.15*DOWN)
      pop2 = TextMobject("O").set_color(BLUE).shift(2*DOWN, 2*LEFT)
      pop3 = TextMobject("O").set_color(BLUE).shift(2.6*DOWN, 2.25*RIGHT)
      pop4 = TextMobject("o").set_color(RED).shift(2.25*DOWN, 0.75*LEFT)
      pop5 = TextMobject("O").set_color(BLUE).shift(2.5*DOWN, 1.0*RIGHT)
      pop6 = TextMobject("o").set_color(RED).shift(1.5*DOWN, RIGHT)

      popmut = TextMobject("O'").set_color(GREEN).shift(DOWN)

      rm11 = DoubleArrow(pop1.get_left(), pop2.get_right()).scale(0.5)
      rm12 = DoubleArrow(pop6.get_left(), pop4.get_left()).scale(0.5)
      rm13 = DoubleArrow(pop5.get_right(), pop3.get_left()).scale(0.75)

      rm21 = DoubleArrow(pop1.get_right(), pop3.get_left()).scale(0.5)
      rm22 = DoubleArrow(pop2.get_right(), pop6.get_left()).scale(0.5)
      rm23 = DoubleArrow(pop5.get_right(), pop4.get_left()).scale(0.5)

      population = VGroup(pop1, pop2, pop3, pop4, pop5, pop6)

      rmfirst = VGroup(rm11, rm12, rm13)
      rmsecond = VGroup(rm21, rm22, rm23)

      geneflowyay = Circle().shift(4.5*LEFT)
      newgene1 = TextMobject("O").shift(5.75*LEFT)
      newgene2 = TextMobject("o").shift(4.25*LEFT)

      theArrow = CurvedArrow(geneflowyay.get_bottom(), holder.get_left()).shift(LEFT/2, DOWN/2)
      geneflowyay.shift(LEFT/2)
      themarker = TextMobject("Genes Cannot Enter").scale(0.5).next_to(theArrow, DOWN, LEFT)

      geneflow = VGroup(geneflowyay, newgene1, newgene2)
      nogenes = VGroup(theArrow, themarker)

      natural = TextMobject("No traits are favored").scale(0.6).shift(1.1*DOWN)






      self.play(Write(thisishardy))

      self.play(Write(thisisactualhardy))

      self.wait(1.5)

      self.play(FadeOut(thisishardy), ReplacementTransform(thisisactualhardy, explainhardybegin))

      self.wait(0.75)

      self.play(ReplacementTransform(explainhardybegin, explainhardynewpos))

      self.wait(0.5)

      self.play(Write(hardyconditions[0]), ShowCreation(holder), Write(con1text))

      self.wait(2)

      self.play(Write(hardyconditions[1]), FadeOut(con1text), ShowCreation(population), ShowCreation(popmut))

      self.wait(0.5)

      self.play(ShowCreation(rmfirst))

      self.wait(0.5)

      self.play(ReplacementTransform(rmfirst, rmsecond))

      self.wait(0.5)

      self.play(FadeOut(rmsecond))

      self.wait(0.5)

      self.play(Write(hardyconditions[2]))

      self.wait(0.5)

      self.play(FadeOut(popmut))

      self.wait(1)

      self.play(Write(hardyconditions[3]))

      self.wait(0.5)

      self.play(ShowCreation(geneflow), ShowCreation(nogenes))

      self.wait(1)

      self.play(FadeOut(geneflow), FadeOut(nogenes))

      self.wait(0.5)

      self.play(Write(hardyconditions[4]), Write(natural))

      self.wait(3)

      self.play(FadeOut(hardyconditions), FadeOut(holder), FadeOut(population), FadeOut(explainhardynewpos), FadeOut(natural))






class PunnettSquareIntroExplain(Scene):
   def construct(self):
      thisisa = TextMobject("To understand the genetics of Hardy-Weinberg Equilibrium,").to_edge(UP)
      thisisa2 = TextMobject("Let's set up a Punnett Square:").to_edge(UP)
      wowsquare1 = TextMobject("Under the conditions of simple Hardy-Weinberg Equilibrium, ").to_edge(UP)
      wowsquare11 = TextMobject("Each organism has two main alleles, ", "D", " and ", "d", ".").to_edge(UP)

      wowsquare11[1].set_color(BLUE)
      wowsquare11[3].set_color(RED)

      wowsquare2 = TextMobject("Now, we can map each gene combination to its respective location in the square.").scale(0.85)
      wowsquare2.to_edge(UP)


      sq1 = Square().shift(LEFT, UP)
      sq2 = Square().shift(RIGHT, UP)
      sq3 = Square().shift(LEFT, DOWN)
      sq4 = Square().shift(RIGHT, DOWN)

      leftup = TextMobject("D", "D").set_color(BLUE).shift(LEFT, UP)
      rightup = TextMobject("D", "d").shift(RIGHT, UP)
      downleft = TextMobject("D", "d").shift(LEFT, DOWN)
      downright = TextMobject("d", "d").set_color(RED).shift(RIGHT, DOWN)

      allD = TextMobject("D").set_color(BLUE).shift(LEFT, 5*UP/2)
      allD2 = TextMobject("D").set_color(BLUE).shift(5*LEFT/2, UP)
      alld = TextMobject("d").set_color(RED).shift(5*LEFT/2, DOWN)
      alld2 = TextMobject("d").set_color(RED).shift(RIGHT, 5*UP/2)

      rightup[0].set_color(BLUE)
      rightup[1].set_color(RED)
      downleft[0].set_color(BLUE)
      downleft[1].set_color(RED)

      squaregroup = VGroup(sq1, sq2, sq3, sq4).shift(2*DOWN/3)
      insquare = VGroup(leftup, rightup, downleft, downright).shift(2*DOWN/3)
      outsquare1 = VGroup(allD, allD2, alld, alld2).shift(2*DOWN/3)

      self.play(Write(thisisa))

      self.wait(1.5)

      self.play(FadeOut(thisisa), Write(thisisa2))

      self.wait(1)

      self.play(ShowCreation(squaregroup))

      self.wait(1)

      self.play(FadeOut(thisisa2), Write(wowsquare1))

      self.wait(1.5)

      self.play(FadeOut(wowsquare1), Write(wowsquare11))

      self.wait(0.5)

      self.play(ShowCreation(outsquare1))

      self.wait(1)

      self.play(FadeOut(wowsquare11), Write(wowsquare2))

      self.wait(0.5)

      self.play(ReplacementTransform(allD.copy(), leftup[0]),
                ReplacementTransform(allD2.copy(), leftup[1])
                )

      self.wait(0.5)

      self.play(ReplacementTransform(allD.copy(), rightup[0]),
                ReplacementTransform(alld2.copy(), rightup[1])
                )

      self.wait(0.5)

      self.play(ReplacementTransform(allD.copy(), downleft[0]),
                ReplacementTransform(alld.copy(), downleft[1])
                )

      self.wait(0.5)

      self.play(ReplacementTransform(alld.copy(), downright[0]),
                ReplacementTransform(alld2.copy(), downright[1])
                )

      self.wait(3)

      self.play(FadeOut(squaregroup), FadeOut(insquare), FadeOut(outsquare1), FadeOut(wowsquare2))

      self.wait(1)


class PQCreation(Scene):
   def construct(self):

      introduce1 = TextMobject("In Hardy-Weinberg Equilibrium, the two alleles are denoted by ", "p", " and ", "q", ".").scale(0.85)
      introduce1[1].set_color(BLUE)
      introduce1[3].set_color(RED)

      introduce2 = TextMobject("Each of ", "p", " and ", "q", " represent a percentage of their respective allele. ").scale(0.85)
      introduce2[1].set_color(BLUE)
      introduce2[3].set_color(RED)

      introduce22 = TextMobject("The total percentage adds up to 1.").next_to(introduce2, DOWN/2).scale(0.85)
      introduce222 = TextMobject("Each of ", "p", " and ", "q", " represent a percentage of their respective allele. ").scale(0.85)
      introduce222[1].set_color(BLUE)
      introduce222[3].set_color(RED)
      introduce222.shift(UP)

      equationpq = TexMobject("p", "+", "q", "=1").scale(1.5)
      equationpq[0].set_color(BLUE)
      equationpq[2].set_color(RED)

      sq1 = Square().shift(LEFT, UP)
      sq2 = Square().shift(RIGHT, UP)
      sq3 = Square().shift(LEFT, DOWN)
      sq4 = Square().shift(RIGHT, DOWN)

      leftup = TextMobject("D", "D").set_color(BLUE).shift(LEFT, UP)
      rightup = TextMobject("D", "d").shift(RIGHT, UP)
      downleft = TextMobject("D", "d").shift(LEFT, DOWN)
      downright = TextMobject("d", "d").set_color(RED).shift(RIGHT, DOWN)

      leftup2 = TexMobject("p", "^2").shift(LEFT, UP)
      leftup2[0].set_color(BLUE)
      rightup2 = TexMobject("p", "q").shift(RIGHT, UP)
      rightup2[0].set_color(BLUE)
      rightup2[1].set_color(RED)
      downleft2 = TexMobject("p", "q").shift(LEFT, DOWN)
      downleft2[0].set_color(BLUE)
      downleft2[1].set_color(RED)
      downright2 = TexMobject("q", "^2").shift(RIGHT, DOWN)
      downright2[0].set_color(RED)

      leftup3 = TexMobject("p", "\\times", "p").shift(LEFT, UP)
      leftup3[0].set_color(BLUE)
      leftup3[2].set_color(BLUE)
      rightup3 = TexMobject("2", "\\times", "p", "\\times", "q").shift(RIGHT, UP).scale(0.9)
      rightup3[2].set_color(BLUE)
      rightup3[4].set_color(RED)
      downleft3 = TexMobject("2", "\\times", "p", "\\times", "q").shift(LEFT, DOWN).scale(0.9)
      downleft3[2].set_color(BLUE)
      downleft3[4].set_color(RED)
      downright3 = TexMobject("q", "\\times", "q").shift(RIGHT, DOWN)
      downright3[0].set_color(RED)
      downright3[2].set_color(RED)

      allD = TextMobject("D").set_color(BLUE).shift(LEFT, 5 * UP / 2)
      allD2 = TextMobject("D").set_color(BLUE).shift(5 * LEFT / 2, UP)
      alld = TextMobject("d").set_color(RED).shift(5 * LEFT / 2, DOWN)
      alld2 = TextMobject("d").set_color(RED).shift(RIGHT, 5 * UP / 2)

      rightup[0].set_color(BLUE)
      rightup[1].set_color(RED)
      downleft[0].set_color(BLUE)
      downleft[1].set_color(RED)

      allp = TextMobject("p").set_color(BLUE).shift(LEFT, 5 * UP / 2)
      allp2 = TextMobject("p").set_color(BLUE).shift(5 * LEFT / 2, UP)
      allq = TextMobject("q").set_color(RED).shift(5 * LEFT / 2, DOWN)
      allq2 = TextMobject("q").set_color(RED).shift(RIGHT, 5 * UP / 2)

      squaregroup = VGroup(sq1, sq2, sq3, sq4).shift(2 * DOWN / 3)
      insquare = VGroup(leftup, rightup, downleft, downright).shift(2 * DOWN / 3)
      insquare2 = VGroup(leftup2, rightup2, downleft2, downright2).shift(2 * DOWN / 3)
      insquare3 = VGroup(leftup3, rightup3, downleft3, downright3).shift(2 * DOWN / 3)
      outsquare1 = VGroup(allD, allD2, alld, alld2).shift(2 * DOWN / 3)
      outsquare2 = VGroup(allp, allp2, allq, allq2).shift(2 * DOWN / 3)

      introduce3 = TextMobject("Now, let's look back at our Punnett Square.").to_edge(UP)

      newsquare1 = TextMobject("We can replace ", "D", " and ", "d", " with ", "p", " and ", "q", ".").to_edge(UP)
      newsquare1[1].set_color(BLUE)
      newsquare1[3].set_color(RED)
      newsquare1[5].set_color(BLUE)
      newsquare1[7].set_color(RED)

      newsquare2 = TextMobject("Then, we can similarly calculate the new phenotypes in terms of ", "p", " and ", "q", ".").scale(0.85)
      newsquare2.to_edge(UP)
      newsquare2[1].set_color(BLUE)
      newsquare2[3].set_color(RED)

      penult = TexMobject("p", #0
                          "^2", #1
                          "+", #2
                          "p", #3
                          "q", #4
                          "+", #5
                          "p", #6
                          "q", #7
                          "+", #8
                          "q", #9
                          "^2" #10
                          ).scale(1.5).shift(3.25*DOWN)

      penult[0].set_color(BLUE)
      penult[3].set_color(BLUE)
      penult[4].set_color(RED)
      penult[6].set_color(BLUE)
      penult[7].set_color(RED)
      penult[9].set_color(RED)

      final = TexMobject("p", #0
                          "^2", #1
                          "+", #2
                          "2", #3
                          "p", #4
                          "q", #5
                          "+", #6
                          "q", #7
                          "^2" #8
                          ).scale(1.5).shift(3.25*DOWN)

      final[0].set_color(BLUE)
      final[4].set_color(BLUE)
      final[5].set_color(RED)
      final[7].set_color(RED)

      finalpos = TexMobject("p", #0
                          "^2", #1
                          "+", #2
                          "2", #3
                          "p", #4
                          "q", #5
                          "+", #6
                          "q", #7
                          "^2" #8
                          ).scale(2)

      finalpos[0].set_color(BLUE)
      finalpos[4].set_color(BLUE)
      finalpos[5].set_color(RED)
      finalpos[7].set_color(RED)


      finaltext = TextMobject("We can write this out as an equation for the total percentages.").to_edge(UP).scale(0.9)

      self.play(Write(introduce1))

      self.wait(1.5)

      self.play(FadeOut(introduce1), Write(introduce2))

      self.wait(0.5)

      self.play(Write(introduce22))

      self.wait(1)

      self.play(ReplacementTransform(introduce2, introduce222))

      self.wait(0.5)

      self.play(ReplacementTransform(introduce22, equationpq))

      self.wait(1.5)

      self.play(FadeOut(introduce222), FadeOut(equationpq), Write(introduce3))

      self.wait(1.5)

      self.play(ShowCreation(squaregroup), ShowCreation(insquare), ShowCreation(outsquare1))

      self.wait(1.5)

      self.play(FadeOut(introduce3), Write(newsquare1))

      self.wait(0.5)

      self.play(ReplacementTransform(outsquare1, outsquare2))

      self.wait(1)

      self.play(FadeOut(newsquare1), Write(newsquare2))

      self.wait(1)

      self.play(FadeOut(insquare))

      self.wait(0.5)

      self.play(ReplacementTransform(allp.copy(), leftup3[0]),
                Write(leftup3[1]),
                ReplacementTransform(allp2.copy(), leftup3[2])
                )

      self.wait(0.5)

      self.play(Write(rightup3[0:2]),
                ReplacementTransform(allp2.copy(), rightup3[2]),
                Write(rightup3[3]),
                ReplacementTransform(allq2.copy(), rightup3[4])
               )

      self.wait(0.5)

      self.play(Write(downleft3[0:2]),
                ReplacementTransform(allp.copy(), downleft3[2]),
                Write(downleft3[3]),
                ReplacementTransform(allq.copy(), downleft3[4])
               )

      self.wait(0.5)

      self.play(ReplacementTransform(allq2.copy(), downright3[0]),
                Write(downright3[1]),
                ReplacementTransform(allq.copy(), downright3[2])
                )

      self.wait(1)

      self.play(ReplacementTransform(insquare3, insquare2))

      self.wait(2)


      self.play(FadeOut(newsquare2), Write(finaltext))

      self.wait(0.5)

      self.play(ReplacementTransform(insquare2.copy(), penult))

      self.wait(1.5)

      self.play(ReplacementTransform(penult, final))

      self.wait(1)

      self.play(FadeOut(insquare2), FadeOut(squaregroup), FadeOut(outsquare2), FadeOut(finaltext), ReplacementTransform(final, finalpos))

      self.wait(2)

class afterSquare(Scene):
   def construct(self):
      finalpos = TexMobject("p", #0
                          "^2", #1
                          "+", #2
                          "2", #3
                          "p", #4
                          "q", #5
                          "+", #6
                          "q", #7
                          "^2" #8
                          ).scale(2)

      finalpos[0].set_color(BLUE)
      finalpos[4].set_color(BLUE)
      finalpos[5].set_color(RED)
      finalpos[7].set_color(RED)

      newstart = TexMobject("p", #0
                          "^2", #1
                          "+", #2
                          "2", #3
                          "p", #4
                          "q", #5
                          "+", #6
                          "q", #7
                          "^2", #8
                          "=1" #9
                          ).scale(2)

      newstart[0].set_color(BLUE)
      newstart[4].set_color(BLUE)
      newstart[5].set_color(RED)
      newstart[7].set_color(RED)

      hom1 = TextMobject("A pair of similar alleles is called a ", "homozygous", " pair.").to_edge(UP)
      hom1[1].set_color(YELLOW)

      het1 = TextMobject("A pair of different alleles is called a ", "heterozygous", " pair.").to_edge(UP)
      het1[1].set_color(PURPLE)


      arrow1label = TextMobject("Homozygous", " Dominant").shift(2*DOWN, 2*LEFT).scale(0.5)
      arrowhom1 = Arrow(arrow1label.get_top(), newstart[0].get_bottom()).shift(DOWN/6)
      arrow1label[0].set_color(YELLOW)
      arrow1label.shift(DOWN/5)

      arrow1 = VGroup(arrowhom1, arrow1label)

      arrow2label = TextMobject("Homozygous", " Recessive").shift(2*DOWN, 2*RIGHT).scale(0.5)
      arrowhom2 = Arrow(arrow2label.get_top(), newstart[7].get_bottom()).shift(DOWN/6)
      arrow2label[0].set_color(YELLOW)
      arrow2label.shift(DOWN/5)

      arrow2 = VGroup(arrowhom2, arrow2label)

      arrow3label = TextMobject("Heterozygous").shift(1.5*UP, 2*RIGHT).scale(0.5)
      arrowhet2 = Arrow(arrow3label.get_left(), newstart[4:6].get_top()).shift(UP/6)
      arrow3label.set_color(PURPLE)
      arrow3label.shift(UP/5)

      arrow3 = VGroup(arrow3label, arrowhet2)

      rectangle1 = Rectangle(height=3, width=1).shift(LEFT)
      rectangle2 = Rectangle(height=1, width=3).shift(RIGHT, 2 * DOWN)
      square1 = Square().scale(0.5).shift(2*DOWN, LEFT).set_color(BLUE)
      square2 = Square().scale(1.5).shift(RIGHT).set_color(RED)
      firstgroup = VGroup(square1, rectangle1, square2, rectangle2)


      rectangle1new = Rectangle(height=1, width=3).shift(UP)
      rectangle2new = Rectangle(height=3, width=1).shift(DOWN, 2 * RIGHT)
      square1new = Square().scale(1.5).shift(DOWN).set_color(BLUE)
      square2new = Square().scale(0.5).shift(UP, 2*RIGHT).set_color(RED)
      secondgroup = VGroup(square1new, rectangle1new, square2new, rectangle2new)


      leftup2 = TexMobject("p", "q").shift(LEFT, UP)
      leftup2[0].set_color(BLUE)
      leftup2[1].set_color(RED)
      rightup2 = TexMobject("q", "^2").shift(RIGHT, UP)
      rightup2[0].set_color(RED)
      downleft2 = TexMobject("p", "^2").shift(LEFT, DOWN)
      downleft2[0].set_color(BLUE)
      downright2 = TexMobject("p", "q").shift(RIGHT, DOWN)
      downright2[0].set_color(BLUE)
      downright2[1].set_color(RED)

      sq2 = Square().shift(LEFT, UP)
      sq4 = Square().shift(RIGHT, UP).set_color(RED)
      sq1 = Square().shift(LEFT, DOWN).set_color(BLUE)
      sq3 = Square().shift(RIGHT, DOWN)

      squaregroup = VGroup(sq1, sq2, sq4, sq3).shift(DOWN/2, RIGHT/2)
      insquare2 = VGroup(downleft2, rightup2, leftup2, downright2).shift(DOWN/2, RIGHT/2)

      brace1sqf = Brace(sq1, DOWN)
      brace1rcf = Brace(sq2, LEFT)
      brace2sqf = Brace(sq1, LEFT)
      brace2rcf = Brace(sq3, DOWN)
      btext31 = brace1sqf.get_text("p").set_color(BLUE)
      btext32 = brace1rcf.get_text("q").set_color(RED)
      btext33 = brace2sqf.get_text("p").set_color(BLUE)
      btext34 = brace2rcf.get_text("q").set_color(RED)

      finalbrace= VGroup(brace1sqf, brace1rcf, brace2sqf, brace2rcf, btext31, btext32, btext33, btext34)



      brace1sq = Brace(square1, DOWN)
      brace1rc = Brace(rectangle1, LEFT)
      brace2sq = Brace(square1, LEFT)
      brace2rc = Brace(rectangle2, DOWN)
      btext11 = brace1sq.get_text("p").set_color(BLUE)
      btext12 = brace1rc.get_text("q").set_color(RED)
      btext13 = brace2sq.get_text("p").set_color(BLUE)
      btext14 = brace2rc.get_text("q").set_color(RED)

      brace1sqnew = Brace(square1new, DOWN)
      brace1rcnew = Brace(rectangle1new, LEFT)
      brace2sqnew = Brace(square1new, LEFT)
      brace2rcnew = Brace(rectangle2new, DOWN)
      btext21 = brace1sqnew.get_text("p").set_color(BLUE)
      btext22 = brace1rcnew.get_text("q").set_color(RED)
      btext23 = brace2sqnew.get_text("p").set_color(BLUE)
      btext24 = brace2rcnew.get_text("q").set_color(RED)

      firstbrace = VGroup(brace1sq, brace1rc, brace2sq, brace2rc, btext11, btext12, btext13, btext14)
      secondbrace = VGroup(brace1sqnew, brace1rcnew, brace2sqnew, brace2rcnew, btext21, btext22, btext23, btext24)

      intext11 = TexMobject("p", "^2").next_to(square1).shift(LEFT)
      intext11[0].set_color(BLUE)
      intext13 = TexMobject("q", "^2").next_to(square2).shift(2*LEFT)
      intext13[0].set_color(RED)
      intext12 = TexMobject("p", "", "q").next_to(rectangle1).shift(LEFT)
      intext12[0].set_color(BLUE)
      intext12[1].set_color(RED)
      intext14 = TexMobject("p", "", "q").next_to(rectangle2).shift(2*LEFT)
      intext14[0].set_color(BLUE)
      intext14[1].set_color(RED)

      intext21 = TexMobject("p", "^2").next_to(square1new).shift(2*LEFT)
      intext21[0].set_color(BLUE)
      intext23 = TexMobject("q", "^2").next_to(square2new).shift(LEFT)
      intext23[0].set_color(RED)
      intext22 = TexMobject("p", "", "q").next_to(rectangle1new).shift(2*LEFT)
      intext22[0].set_color(BLUE)
      intext22[1].set_color(RED)
      intext24 = TexMobject("p", "", "q").next_to(rectangle2new).shift(LEFT)
      intext24[0].set_color(BLUE)
      intext24[1].set_color(RED)


      textgroup1 = VGroup(intext11, intext13, intext12, intext14)
      textgroup2 = VGroup(intext21, intext23, intext22, intext24)

      tnear1 = TextMobject("As the frequency of each ", "allele", " changes, so does the frequency of the ", "phenotypes", ".").scale(0.7)
      tnear1.to_edge(UP)
      tnear1[1].set_color(GREEN)
      tnear1[3].set_color(GREEN)

      tnear2 = TextMobject("We can calculate the frequency of each phenotype using the formula.").to_edge(UP).scale(0.8)

      approach1 = TextMobject("Although the Hardy-Weinberg Theorem provides an ideal biological circumstance,").scale(0.8)
      approach2 = TextMobject("it has near-impossible conditions to meet in our world.").scale(0.8).shift(3*DOWN/4)

      approach11 = TextMobject("That being said, it does make problem-solving in biology quite a bit more straightforward.").scale(0.7)

      approachfinal1 = TextMobject("And it does make for an interesting thought experiment.")



      self.add(finalpos)

      self.wait(1)

      self.play(ReplacementTransform(finalpos, newstart))

      self.wait(1)

      self.play(Write(hom1))

      self.wait(1.5)

      self.play(ShowCreation(arrow1), ShowCreation(arrow2))

      self.wait(1.5)

      self.play(ReplacementTransform(hom1, het1))

      self.wait(1.5)

      self.play(ShowCreation(arrow3))

      self.wait(2)

      self.play(FadeOut(arrow3), FadeOut(arrow1), FadeOut(arrow2), FadeOut(het1), FadeOut(newstart), run_time=1.5)

      self.wait(0.5)

      self.play(Write(tnear1))

      self.play(ShowCreation(firstgroup), ShowCreation(firstbrace), ShowCreation(textgroup1))

      self.wait(2.5)

      self.play(Transform(firstgroup, secondgroup), Transform(firstbrace, secondbrace), Transform(textgroup1, textgroup2))

      self.wait(2)

      self.play(Transform(firstgroup, squaregroup), Transform(textgroup1, insquare2), Transform(firstbrace, finalbrace))

      self.wait(2)

      self.play(FadeOut(tnear1), FadeIn(tnear2), FadeOut(squaregroup), FadeOut(firstbrace), FadeOut(firstgroup), ReplacementTransform(textgroup1, newstart))

      self.wait(2)

      self.play(FadeOut(tnear2), FadeOut(newstart))

      self.wait(0.5)

      self.play(Write(approach1))

      self.wait(0.25)

      self.play(Write(approach2))

      self.wait(2.5)

      self.play(FadeOut(approach1), FadeOut(approach2), FadeIn(approach11))

      self.wait(2.5)

      self.play(ReplacementTransform(approach11, approachfinal1))

      self.wait(2.5)

      self.play(FadeOut(approachfinal1))

      self.wait(1)






class TheThumbnail(Scene):
   def construct(self):
      finalpos = TexMobject("p",  # 0
                            "^2",  # 1
                            "+",  # 2
                            "2",  # 3
                            "p",  # 4
                            "q",  # 5
                            "+",  # 6
                            "q",  # 7
                            "^2",  # 8
                            "=1" #9
                            ).scale(2).shift(DOWN)

      finalpos[0].set_color(BLUE)
      finalpos[4].set_color(BLUE)
      finalpos[5].set_color(RED)
      finalpos[7].set_color(RED)

      thumbnailtitle = TextMobject("The Hardy-Weinberg Theorem:").scale(1.7).to_edge(UP)



      thumbnaimsub = TextMobject("A Biological Thought Experiment").next_to(thumbnailtitle, DOWN).scale(1.7)

      self.add(thumbnailtitle, finalpos, thumbnaimsub)

      self.wait(2)

class Intro(Scene):
   def construct(self):
      Artificial = TextMobject("An ", "Artificial", " Animation").scale(2).shift(2.25*DOWN)
      Artificial[1].set_color(BLUE)

      circle = Circle(color=BLUE).scale(1.5).shift(UP/2)

      square1 = Square().shift(UP, LEFT).scale(0.6)
      square2 = Square().shift(UP, RIGHT).scale(0.6)
      square3 = Square().shift(DOWN, LEFT).scale(0.6)
      square4 = Square().shift(DOWN, RIGHT).scale(0.6)

      newsquare1 = Square().shift(UP, LEFT).scale(0.6).rotate(TAU/8)
      newsquare2 = Square().shift(UP, RIGHT).scale(0.6).rotate(TAU/8)
      newsquare3 = Square().shift(DOWN, LEFT).scale(0.6).rotate(TAU/8)
      newsquare4 = Square().shift(DOWN, RIGHT).scale(0.6).rotate(TAU/8)



      combsqu = VGroup(square1, square2, square3, square4).shift(UP/2)
      newcomb = VGroup(newsquare1,  newsquare2, newsquare3, newsquare4).shift(UP/2)


      self.play(Write(Artificial))
      self.wait(0.25)
      self.play(ShowCreation(circle))
      self.play(ShowCreation(combsqu))
      self.wait(0.5)
      self.play(ReplacementTransform(combsqu, newcomb))
      self.wait(0.25)
      self.play(FadeOut(Artificial), FadeOut(circle), FadeOut(newcomb))




















