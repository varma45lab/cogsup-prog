from expyriment import design, control, stimuli

control.set_develop_mode()

# Create an object of class Experimen
exp = design.Experiment(name = "Square")

# Initialize the experiment
control.initialize(exp)

# Create two 50px square of different colours
square_1 = stimuli.Rectangle(size= (50,50), colour= ("red"), position=(100,0))
square_2 = stimuli.Rectangle(size= (50,50), colour= ("green"), position=(-100,0))

# Start running the experiment
control.start(subject_id=1)

# Present the fixation cross
square_1.present(update=False)
square_2.present(clear=False)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()



