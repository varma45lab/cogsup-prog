from expyriment import design, control, stimuli

control.set_develop_mode()

# Create an object of class Experiment
exp = design.Experiment(name = "Square")

# Initialize the experiment
control.initialize(exp)

# Create two 50px square of different colours and positions
square_1 = stimuli.Rectangle(size= (50,50), colour= ("red"), position=(-400,0))
square_2 = stimuli.Rectangle(size= (50,50), colour= ("green"), position=(0,0))

# Start running the experiment
control.start(subject_id=1)

# Present the squares
square_1.present(update=False)
square_2.present(clear=False)

# Leave it on-screen for 1 second
exp.clock.wait(1000)

# Moving the red square towards green

speed = 5
collission = -50

while square_1.position[0] < collission:
    square_1.move((speed, 0))
    
    square_1.present(update=False)
    square_2.present(clear=False)
    
    exp.clock.wait(10)
    

# Moving the green sqaure after collision

distance = 375
frames = int(distance / speed)

for i in range(frames):
    square_2.move((speed, 0))
    
    square_1.present(update=False)
    square_2.present(clear=False)
    
    exp.clock.wait(10)
                  
# Present the final display and wait time

square_1.present(update=False)
square_2.present(clear=False)
exp.clock.wait(1000)

# End the current session and quit expyriment
control.end()



