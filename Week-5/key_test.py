import random
from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY, C_BLACK, K_LEFT, K_RIGHT, K_SPACE

control.set_develop_mode(True)

# Experiment

exp = design.Experiment(name="Circle Test")
exp.add_data_variable_names(["Subject", "Blocks", "Circle Condition", "Reaction Time", "Key Press", "Accuracy"])


control.initialize(exp)

# Instructions
instructions = stimuli.TextScreen(
    heading="Instructions",
    text=("You will see a circle and a square.\n"
        "Press the LEFT or RIGHT arrow key to indicate where the circle is on the screen.\n\n"
        "Press SPACE to begin." ),text_size=30,heading_size=36,)

instructions.preload()

# Stimuli
left_side= (-200,0)
right_side= (200,0)
circle = stimuli.Circle(radius=40, position= left_side,  colour=C_GREY)
square = stimuli.Rectangle(size=(50, 50), position=right_side, colour=C_GREY)
fixation = stimuli.FixCross()

circle.preload()
square.preload()
fixation.preload()

def run_trial(side):
    if side == "left":
        circle.position = left_side
        square.position = right_side
        correct_key = K_LEFT
    elif side == "right":
        circle.position = right_side
        square.position = left_side
        correct_key = K_RIGHT
    else:
        raise ValueError()

    # Fixation
    fixation.present()
    exp.clock.wait(500)

    # Present shapes
    square.present(clear=True, update=False)
    circle.present(clear=False, update=True)

    # Response
    key, rt = exp.keyboard.wait([K_LEFT, K_RIGHT])
    correct = (key == correct_key)

    # Feedback
    feedback_text = "CORRECT" if correct else "INCORRECT"
    feedback_colour = (0, 180, 0) if correct else (220, 0, 0)
    feedback = stimuli.TextLine(
        text=f"{feedback_text}   RT: {rt} ms",
        text_size=32,
        text_colour=feedback_colour)
    
    feedback.present()
    exp.clock.wait(1000)

    return key, rt, correct


# Run experiment
control.start()
subject = exp.subject

instructions.present()
exp.keyboard.wait(K_SPACE)

blocks = ["deterministic","stochastic"]
random.shuffle(blocks)

for block_trial in blocks:
    block_screen= stimuli.TextLine(text="Block")
    block_screen.present()
    exp.keyboard.wait(K_SPACE)
    
    for trial in range(10):
        if block_trial == "stochastic":
            side = random.choice(["left", "right"])
        elif block_trial == "deterministic":
            side = "right"
        key, rt, correct = run_trial(side)
        exp.data.add([block_trial, side, rt, key, correct])

  

end_screen = stimuli.TextScreen(
    heading="Done",
    text="The task is now complete. Please press SPACE to exit.",
    text_size=30,
    heading_size=36,
)
end_screen.present()
exp.keyboard.wait(K_SPACE)

control.end()

