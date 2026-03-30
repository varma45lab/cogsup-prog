from expyriment import design, control, stimuli

exp = design.Experiment(name="timing puzzle")

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
text = stimuli.TextLine("Fixation removed")
fixation.preload()
text.preload()


text = stimuli.TextLine('Fixation removed') 
t0 = exp.clock.time 
fixation.present() 
dt = exp.clock.time - t0 
exp.clock.wait(1000 - dt)

text = stimuli.TextLine('Fixation removed') 
t0 = exp.clock.time 
fixation.present() 
dt = exp.clock.time - t0 
exp.clock.wait(1000 - dt)


units = "second" if dt == 1.0 else "seconds"
duration_text = f"Fixation was present on the screen for {dt} {units}"

print(dt)

text2 = stimuli.TextLine(duration_text)
text2.present()
exp.clock.wait(2000)

control.end()




