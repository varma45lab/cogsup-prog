from expyriment import design, control, stimuli, misc
from expyriment.misc.constants import C_WHITE, C_BLACK

control.set_develop_mode()

exp = design.Experiment("Hermann_grid", background_colour=C_WHITE)
control.initialize(exp)

screen_w, screen_h = exp.screen.size

square_size = 85   
gap_size    = 20    
n_rows      = 5
n_cols      = 5

grid_width  = n_cols * square_size + (n_cols - 1) * gap_size
grid_height = n_rows * square_size + (n_rows - 1) * gap_size

origin_x = -grid_width  / 2.0   
origin_y =  grid_height / 2.0   

# Base square
base_square = stimuli.Rectangle(size=(square_size, square_size),colour=C_BLACK,position=(0, 0))

canvas = stimuli.BlankScreen(colour=C_WHITE)

for i in range(n_rows):        
    for j in range(n_cols):    

        x = origin_x + j * (square_size + gap_size) + square_size / 2.0
        y = origin_y - i * (square_size + gap_size) - square_size / 2.0

        sq = base_square.copy()
        sq.position = (x, y)
        sq.plot(canvas)

control.start(subject_id=1)
canvas.present()
exp.keyboard.wait()
control.end()
