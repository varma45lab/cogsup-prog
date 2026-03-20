from expyriment import design, control, stimuli

control.set_develop_mode()

exp = design.Experiment(name = "Squares")

control.initialize(exp)

width, height = exp.screen.size

square_size = int(width * 0.05)
half_sq = square_size / 2

position_1 = (-width / 2 + half_sq,  height / 2 - half_sq)   
position_2 = ( width / 2 - half_sq,  height / 2 - half_sq)   
position_3 = (-width / 2 + half_sq, -height / 2 + half_sq)   
position_4 = ( width / 2 - half_sq, -height / 2 + half_sq)   



square_1 = stimuli.Rectangle(size= (square_size,square_size), colour="red", position = position_1 , line_width=1)
square_2 = stimuli.Rectangle(size= (square_size,square_size), colour="red", position = position_2 , line_width=1)
square_3 = stimuli.Rectangle(size= (square_size,square_size), colour="red", position = position_3 , line_width=1)
square_4 = stimuli.Rectangle(size= (square_size,square_size), colour="red", position = position_4 , line_width=1)


control.start(subject_id=1)

square_1.present(clear=True,  update=False)   
square_2.present(clear=False, update=False)
square_3.present(clear=False, update=False)
square_4.present(clear=False, update=True)    


square_1.present(clear=True,  update=False)  
square_2.present(clear=False, update=False)
square_3.present(clear=False, update=False)
square_4.present(clear=False, update=True)    

exp.keyboard.wait()
control.end()