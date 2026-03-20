from expyriment import design, control, stimuli, misc

control.set_develop_mode()

exp = design.Experiment("Kanizsa_rectangle", background_colour=misc.constants.C_GREY)

control.initialize(exp)


def show_kanizsa_rectangle(aspect_ratio, rect_scale, circle_scale):
    
    
    
    width, height = exp.screen.size  
    rect_width = rect_scale * width
    rect_height = rect_width / aspect_ratio

    half_w = rect_width / 2.0
    half_h = rect_height / 2.0

    rectangle = stimuli.Rectangle(size=(int(rect_width), int(rect_height)),colour=misc.constants.C_GREY,position=(0, 0))

    circle_radius = int(circle_scale * width) 

    circle_pos_1 = (-half_w,  half_h)   
    circle_pos_2 = ( half_w, -half_h)   
    circle_pos_3 = (-half_w, -half_h)   
    circle_pos_4 = ( half_w,  half_h)   

    circle_1 = stimuli.Circle(radius=circle_radius, colour="black", position=circle_pos_1)
    circle_2 = stimuli.Circle(radius=circle_radius, colour="white", position=circle_pos_2)
    circle_3 = stimuli.Circle(radius=circle_radius, colour="white", position=circle_pos_3)
    circle_4 = stimuli.Circle(radius=circle_radius, colour="black", position=circle_pos_4)

    bg_sc = stimuli.BlankScreen() 

    circle_1.plot(bg_sc)
    circle_2.plot(bg_sc)
    circle_3.plot(bg_sc)
    circle_4.plot(bg_sc)
    rectangle.plot(bg_sc)

    control.start(subject_id=1)
    bg_sc.present()
    exp.keyboard.wait()
    control.end()

if __name__ == "__main__":
    show_kanizsa_rectangle(aspect_ratio=1.5, rect_scale=0.4, circle_scale=0.08)

