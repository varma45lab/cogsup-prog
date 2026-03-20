from expyriment import design, control, stimuli, misc
from expyriment.misc.constants import C_GREY

control.set_develop_mode()

exp = design.Experiment("Kanizsa_square", background_colour= C_GREY)

control.initialize(exp)

width, height = exp.screen.size

square_len = int(width * 0.25)
half_len = square_len / 2

square_1 = stimuli.Rectangle(size= (square_len,square_len), colour= C_GREY, position= (0,0))

circle_radius = int(width * 0.05)

circle_pos_1 = (-half_len, half_len)
circle_pos_2 = (half_len, -half_len)
circle_pos_3 = (-half_len, -half_len)
circle_pos_4 = (half_len, half_len)

circle_1 = stimuli.Circle(radius=circle_radius, colour="black", position=circle_pos_1)
circle_2 = stimuli.Circle(radius=circle_radius, colour="white", position=circle_pos_2)
circle_3 = stimuli.Circle(radius=circle_radius, colour="white", position=circle_pos_3)
circle_4 = stimuli.Circle(radius=circle_radius, colour="black", position=circle_pos_4)


bg_sc = stimuli.BlankScreen()

circle_1.plot(bg_sc)
circle_2.plot(bg_sc)
circle_3.plot(bg_sc)
circle_4.plot(bg_sc)

square_1.plot(bg_sc)

control.start(subject_id=1)
bg_sc.present()
exp.keyboard.wait()
control.end()