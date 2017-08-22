#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.00),
    on Thu Oct 13 23:48:50 2016
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'beat_2AFC'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/casillas/academia/teaching/workshops/psychopy_ws/demos/6_2AFC/beat_2AFC.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1680, 1050), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructions_text = visual.TextStim(win=win, name='instructions_text',
    text='In this experiment you are going to hear different words. Your task is to decide, as quickly as possible and without making mistakes, if what you heard sounds more like "sheep" or "ship". \n\nYou will use the arrow keys to make your decision. Let\'s do a practice round to make sure you understand. \n\nPress the spacebar to continue.',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "practice"
practiceClock = core.Clock()
crossPractice = visual.TextStim(win=win, name='crossPractice',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.5, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1,
    depth=0.0);
practice_sound = sound.Sound('A', secs=-1)
practice_sound.setVolume(1)
sheep_image = visual.ImageStim(
    win=win, name='sheep_image',
    image='sheep1.jpg', mask=None,
    ori=0, pos=[-0.5, 0.3], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
ship_image = visual.ImageStim(
    win=win, name='ship_image',
    image='ship1.jpg', mask=None,
    ori=0, pos=[0.5, 0.3], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
practice_left = visual.TextStim(win=win, name='practice_left',
    text='L',
    font='Arial',
    pos=[-0.5, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
practice_right = visual.TextStim(win=win, name='practice_right',
    text='R',
    font='Arial',
    pos=[0.5, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0);

# Initialize components for Routine "msg"
msgClock = core.Clock()
msg='0.000'
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "got_it"
got_itClock = core.Clock()
gotIT = visual.TextStim(win=win, name='gotIT',
    text='Got it? If you have any questions please ask the experimenter now. If not, press the spacebar to begin the experiment. ',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Break"
BreakClock = core.Clock()

break_text = visual.TextStim(win=win, name='break_text',
    text='You may take a short break if you like. \nPress the spacebar to continue.',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
cross_tr = visual.TextStim(win=win, name='cross_tr',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.5, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1,
    depth=0.0);
trial_sound = sound.Sound('A', secs=-1)
trial_sound.setVolume(1)
image_sheep = visual.ImageStim(
    win=win, name='image_sheep',
    image='sheep.jpg', mask=None,
    ori=0, pos=[-0.5, 0.3], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
image_ship = visual.ImageStim(
    win=win, name='image_ship',
    image='ship.jpg', mask=None,
    ori=0, pos=[0.5, 0.3], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
left = visual.TextStim(win=win, name='left',
    text='L',
    font='Arial',
    pos=[-0.5, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
right = visual.TextStim(win=win, name='right',
    text='R',
    font='Arial',
    pos=[0.5, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0);

# Initialize components for Routine "msg2"
msg2Clock = core.Clock()
msg='0.000'
text_2 = visual.TextStim(win=win, name='text_2',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "end"
endClock = core.Clock()
done = visual.TextStim(win=win, name='done',
    text="That's it. Thanks you for participating.",
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(30.000000)
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
instructionsComponents = [instructions_text, key_resp_2]
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_text* updates
    if t >= 0.0 and instructions_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions_text.tStart = t
        instructions_text.frameNStart = frameN  # exact frame index
        instructions_text.setAutoDraw(True)
    frameRemains = 0.0 + 30.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instructions_text.status == STARTED and t >= frameRemains:
        instructions_text.setAutoDraw(False)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    frameRemains = 0.0 + 30.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if key_resp_2.status == STARTED and t >= frameRemains:
        key_resp_2.status = STOPPED
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
practice_trial = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('practice_trial.xlsx'),
    seed=None, name='practice_trial')
thisExp.addLoop(practice_trial)  # add the loop to the experiment
thisPractice_trial = practice_trial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
if thisPractice_trial != None:
    for paramName in thisPractice_trial.keys():
        exec(paramName + '= thisPractice_trial.' + paramName)

for thisPractice_trial in practice_trial:
    currentLoop = practice_trial
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
    if thisPractice_trial != None:
        for paramName in thisPractice_trial.keys():
            exec(paramName + '= thisPractice_trial.' + paramName)
    
    # ------Prepare to start Routine "practice"-------
    t = 0
    practiceClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    practice_sound.setSound(stimuli, secs=3.0)
    key_resp_practice = event.BuilderKeyResponse()
    # keep track of which components have finished
    practiceComponents = [crossPractice, practice_sound, key_resp_practice, sheep_image, ship_image, practice_left, practice_right]
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "practice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practiceClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *crossPractice* updates
        if t >= 0.0 and crossPractice.status == NOT_STARTED:
            # keep track of start time/frame for later
            crossPractice.tStart = t
            crossPractice.frameNStart = frameN  # exact frame index
            crossPractice.setAutoDraw(True)
        frameRemains = 0.0 + 0.4- win.monitorFramePeriod * 0.75  # most of one frame period left
        if crossPractice.status == STARTED and t >= frameRemains:
            crossPractice.setAutoDraw(False)
        # start/stop practice_sound
        if t >= 0.5 and practice_sound.status == NOT_STARTED:
            # keep track of start time/frame for later
            practice_sound.tStart = t
            practice_sound.frameNStart = frameN  # exact frame index
            practice_sound.play()  # start the sound (it finishes automatically)
        frameRemains = 0.5 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if practice_sound.status == STARTED and t >= frameRemains:
            practice_sound.stop()  # stop the sound (if longer than duration)
        
        # *key_resp_practice* updates
        if t >= 0.5 and key_resp_practice.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_practice.tStart = t
            key_resp_practice.frameNStart = frameN  # exact frame index
            key_resp_practice.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_practice.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.5 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_practice.status == STARTED and t >= frameRemains:
            key_resp_practice.status = STOPPED
        if key_resp_practice.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_practice.keys == []:  # then this was the first keypress
                    key_resp_practice.keys = theseKeys[0]  # just the first key pressed
                    key_resp_practice.rt = key_resp_practice.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
        
        # *sheep_image* updates
        if t >= 0.5 and sheep_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            sheep_image.tStart = t
            sheep_image.frameNStart = frameN  # exact frame index
            sheep_image.setAutoDraw(True)
        frameRemains = 0.5 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if sheep_image.status == STARTED and t >= frameRemains:
            sheep_image.setAutoDraw(False)
        
        # *ship_image* updates
        if t >= 0.5 and ship_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            ship_image.tStart = t
            ship_image.frameNStart = frameN  # exact frame index
            ship_image.setAutoDraw(True)
        frameRemains = 0.5 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if ship_image.status == STARTED and t >= frameRemains:
            ship_image.setAutoDraw(False)
        
        # *practice_left* updates
        if t >= 0.5 and practice_left.status == NOT_STARTED:
            # keep track of start time/frame for later
            practice_left.tStart = t
            practice_left.frameNStart = frameN  # exact frame index
            practice_left.setAutoDraw(True)
        frameRemains = 0.5 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if practice_left.status == STARTED and t >= frameRemains:
            practice_left.setAutoDraw(False)
        
        # *practice_right* updates
        if t >= 0.5 and practice_right.status == NOT_STARTED:
            # keep track of start time/frame for later
            practice_right.tStart = t
            practice_right.frameNStart = frameN  # exact frame index
            practice_right.setAutoDraw(True)
        frameRemains = 0.5 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if practice_right.status == STARTED and t >= frameRemains:
            practice_right.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice"-------
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_sound.stop()  # ensure sound has stopped at end of routine
    # check responses
    if key_resp_practice.keys in ['', [], None]:  # No response was made
        key_resp_practice.keys=None
    practice_trial.addData('key_resp_practice.keys',key_resp_practice.keys)
    if key_resp_practice.keys != None:  # we had a response
        practice_trial.addData('key_resp_practice.rt', key_resp_practice.rt)
    
    # ------Prepare to start Routine "msg"-------
    t = 0
    msgClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    msg="%.3f ...FASTER!" %(key_resp_practice.rt)
    text.setText(msg)
    # keep track of which components have finished
    msgComponents = [text]
    for thisComponent in msgComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "msg"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = msgClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in msgComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "msg"-------
    for thisComponent in msgComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'practice_trial'

# get names of stimulus parameters
if practice_trial.trialList in ([], [None], None):
    params = []
else:
    params = practice_trial.trialList[0].keys()
# save data for this loop
practice_trial.saveAsExcel(filename + '.xlsx', sheetName='practice_trial',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
practice_trial.saveAsText(filename + 'practice_trial.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "got_it"-------
t = 0
got_itClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(11.000000)
# update component parameters for each repeat
gotResponse = event.BuilderKeyResponse()
# keep track of which components have finished
got_itComponents = [gotIT, gotResponse]
for thisComponent in got_itComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "got_it"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = got_itClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *gotIT* updates
    if t >= 0.75 and gotIT.status == NOT_STARTED:
        # keep track of start time/frame for later
        gotIT.tStart = t
        gotIT.frameNStart = frameN  # exact frame index
        gotIT.setAutoDraw(True)
    frameRemains = 0.75 + 10.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if gotIT.status == STARTED and t >= frameRemains:
        gotIT.setAutoDraw(False)
    
    # *gotResponse* updates
    if t >= 1.0 and gotResponse.status == NOT_STARTED:
        # keep track of start time/frame for later
        gotResponse.tStart = t
        gotResponse.frameNStart = frameN  # exact frame index
        gotResponse.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    frameRemains = 1.0 + 10.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if gotResponse.status == STARTED and t >= frameRemains:
        gotResponse.status = STOPPED
    if gotResponse.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in got_itComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "got_it"-------
for thisComponent in got_itComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=3, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trial.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "Break"-------
    t = 0
    BreakClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(20.500000)
    # update component parameters for each repeat
    
    key_resp_break = event.BuilderKeyResponse()
    # keep track of which components have finished
    BreakComponents = [break_text, key_resp_break]
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Break"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = BreakClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if trials.thisN not in [100,200,300,400,500,600,700,800]:
            continueRoutine=False
        
        # *break_text* updates
        if t >= 0.5 and break_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            break_text.tStart = t
            break_text.frameNStart = frameN  # exact frame index
            break_text.setAutoDraw(True)
        frameRemains = 0.5 + 20.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if break_text.status == STARTED and t >= frameRemains:
            break_text.setAutoDraw(False)
        
        # *key_resp_break* updates
        if t >= 0.5 and key_resp_break.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_break.tStart = t
            key_resp_break.frameNStart = frameN  # exact frame index
            key_resp_break.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.5 + 20.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_break.status == STARTED and t >= frameRemains:
            key_resp_break.status = STOPPED
        if key_resp_break.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BreakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Break"-------
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    trial_sound.setSound(stimuli, secs=3.0)
    key_resp_trial = event.BuilderKeyResponse()
    # keep track of which components have finished
    trialComponents = [cross_tr, trial_sound, key_resp_trial, image_sheep, image_ship, left, right]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross_tr* updates
        if t >= 0.0 and cross_tr.status == NOT_STARTED:
            # keep track of start time/frame for later
            cross_tr.tStart = t
            cross_tr.frameNStart = frameN  # exact frame index
            cross_tr.setAutoDraw(True)
        frameRemains = 0.0 + 0.4- win.monitorFramePeriod * 0.75  # most of one frame period left
        if cross_tr.status == STARTED and t >= frameRemains:
            cross_tr.setAutoDraw(False)
        # start/stop trial_sound
        if t >= 0.5 and trial_sound.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_sound.tStart = t
            trial_sound.frameNStart = frameN  # exact frame index
            trial_sound.play()  # start the sound (it finishes automatically)
        frameRemains = 0.5 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if trial_sound.status == STARTED and t >= frameRemains:
            trial_sound.stop()  # stop the sound (if longer than duration)
        
        # *key_resp_trial* updates
        if t >= 0.5 and key_resp_trial.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_trial.tStart = t
            key_resp_trial.frameNStart = frameN  # exact frame index
            key_resp_trial.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_trial.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.5 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_trial.status == STARTED and t >= frameRemains:
            key_resp_trial.status = STOPPED
        if key_resp_trial.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_trial.keys == []:  # then this was the first keypress
                    key_resp_trial.keys = theseKeys[0]  # just the first key pressed
                    key_resp_trial.rt = key_resp_trial.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
        
        # *image_sheep* updates
        if t >= 0.5 and image_sheep.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_sheep.tStart = t
            image_sheep.frameNStart = frameN  # exact frame index
            image_sheep.setAutoDraw(True)
        frameRemains = 0.5 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_sheep.status == STARTED and t >= frameRemains:
            image_sheep.setAutoDraw(False)
        
        # *image_ship* updates
        if t >= 0.5 and image_ship.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_ship.tStart = t
            image_ship.frameNStart = frameN  # exact frame index
            image_ship.setAutoDraw(True)
        frameRemains = 0.5 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_ship.status == STARTED and t >= frameRemains:
            image_ship.setAutoDraw(False)
        
        # *left* updates
        if t >= 0.5 and left.status == NOT_STARTED:
            # keep track of start time/frame for later
            left.tStart = t
            left.frameNStart = frameN  # exact frame index
            left.setAutoDraw(True)
        frameRemains = 0.5 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if left.status == STARTED and t >= frameRemains:
            left.setAutoDraw(False)
        
        # *right* updates
        if t >= 0.5 and right.status == NOT_STARTED:
            # keep track of start time/frame for later
            right.tStart = t
            right.frameNStart = frameN  # exact frame index
            right.setAutoDraw(True)
        frameRemains = 0.5 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if right.status == STARTED and t >= frameRemains:
            right.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trial_sound.stop()  # ensure sound has stopped at end of routine
    # check responses
    if key_resp_trial.keys in ['', [], None]:  # No response was made
        key_resp_trial.keys=None
    trials.addData('key_resp_trial.keys',key_resp_trial.keys)
    if key_resp_trial.keys != None:  # we had a response
        trials.addData('key_resp_trial.rt', key_resp_trial.rt)
    
    # ------Prepare to start Routine "msg2"-------
    t = 0
    msg2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    msg="%.3f" %(key_resp_trial.rt)
    text_2.setText(msg)
    # keep track of which components have finished
    msg2Components = [text_2]
    for thisComponent in msg2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "msg2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = msg2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_2.status == STARTED and t >= frameRemains:
            text_2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in msg2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "msg2"-------
    for thisComponent in msg2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
    
# completed 3 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(21.000000)
# update component parameters for each repeat
doneKey = event.BuilderKeyResponse()
# keep track of which components have finished
endComponents = [done, doneKey]
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *done* updates
    if t >= 0.0 and done.status == NOT_STARTED:
        # keep track of start time/frame for later
        done.tStart = t
        done.frameNStart = frameN  # exact frame index
        done.setAutoDraw(True)
    frameRemains = 0.0 + 20.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if done.status == STARTED and t >= frameRemains:
        done.setAutoDraw(False)
    
    # *doneKey* updates
    if t >= 1.0 and doneKey.status == NOT_STARTED:
        # keep track of start time/frame for later
        doneKey.tStart = t
        doneKey.frameNStart = frameN  # exact frame index
        doneKey.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    frameRemains = 1.0 + 20.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if doneKey.status == STARTED and t >= frameRemains:
        doneKey.status = STOPPED
    if doneKey.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)



# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
