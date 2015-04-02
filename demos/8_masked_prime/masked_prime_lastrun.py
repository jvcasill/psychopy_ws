#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.80.06), Mon Dec  1 11:08:30 2014
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'masked_prime'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/phoneticslab/Dropbox/aapl_experiments/phantom_coarticulation_exp/masked_prime/masked_prime.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=[1680, 1050], fullscr=False, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructions_text = visual.TextStim(win=win, ori=0, name='instructions_text',
    text='In this experiment you are going to hear different sounds. Your task is to decide, as quickly as possible and without making mistakes, if what you heard sounds more like "ee" or "oo". \n\nYou will use the yellow and green keys to make your decision. Yellow is for \'ee\' and green is for \'oo\'. \nLet\'s do a practice round to make sure you understand. \n\nPress the spacebar to continue.',    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "practice"
practiceClock = core.Clock()
prime_practice = visual.TextStim(win=win, ori=0, name='prime_practice',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
practice_sound = sound.Sound('A', secs=0.5)
practice_sound.setVolume(1)
practice_left = visual.TextStim(win=win, ori=0, name='practice_left',
    text='ee',    font='Arial',
    pos=[-0.5, -0.3], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)
practice_right = visual.TextStim(win=win, ori=0, name='practice_right',
    text='oo',    font='Arial',
    pos=[0.5, -0.3], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)
fix = visual.TextStim(win=win, ori=0, name='fix',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-5.0)

# Initialize components for Routine "end"
endClock = core.Clock()
done = visual.TextStim(win=win, ori=0, name='done',
    text="That's it. Thanks you for participating.",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock 
frameN = -1
routineTimer.add(30.000000)
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
instructionsComponents = []
instructionsComponents.append(instructions_text)
instructionsComponents.append(key_resp_2)
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_text* updates
    if t >= 0.0 and instructions_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions_text.tStart = t  # underestimates by a little under one frame
        instructions_text.frameNStart = frameN  # exact frame index
        instructions_text.setAutoDraw(True)
    elif instructions_text.status == STARTED and t >= (0.0 + (30.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        instructions_text.setAutoDraw(False)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    elif key_resp_2.status == STARTED and t >= (0.0 + (30.0-win.monitorFramePeriod*0.75)): #most of one frame period left
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
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
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

#-------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
practice_trial = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=u'/Users/phoneticslab/Dropbox/aapl_experiments/phantom_coarticulation_exp/masked_prime/masked_prime.psyexp',
    trialList=data.importConditions('practice_trial.xlsx'),
    seed=None, name='practice_trial')
thisExp.addLoop(practice_trial)  # add the loop to the experiment
thisPractice_trial = practice_trial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisPractice_trial.rgb)
if thisPractice_trial != None:
    for paramName in thisPractice_trial.keys():
        exec(paramName + '= thisPractice_trial.' + paramName)

for thisPractice_trial in practice_trial:
    currentLoop = practice_trial
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
    if thisPractice_trial != None:
        for paramName in thisPractice_trial.keys():
            exec(paramName + '= thisPractice_trial.' + paramName)
    
    #------Prepare to start Routine "practice"-------
    t = 0
    practiceClock.reset()  # clock 
    frameN = -1
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    prime_practice.setText(words)
    practice_sound.setSound(stimuli)
    key_resp_practice = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_practice.status = NOT_STARTED
    # keep track of which components have finished
    practiceComponents = []
    practiceComponents.append(prime_practice)
    practiceComponents.append(practice_sound)
    practiceComponents.append(key_resp_practice)
    practiceComponents.append(practice_left)
    practiceComponents.append(practice_right)
    practiceComponents.append(fix)
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "practice"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practiceClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prime_practice* updates
        if t >= 0.50 and prime_practice.status == NOT_STARTED:
            # keep track of start time/frame for later
            prime_practice.tStart = t  # underestimates by a little under one frame
            prime_practice.frameNStart = frameN  # exact frame index
            prime_practice.setAutoDraw(True)
        elif prime_practice.status == STARTED and t >= (0.50 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            prime_practice.setAutoDraw(False)
        # start/stop practice_sound
        if t >= 2.5 and practice_sound.status == NOT_STARTED:
            # keep track of start time/frame for later
            practice_sound.tStart = t  # underestimates by a little under one frame
            practice_sound.frameNStart = frameN  # exact frame index
            practice_sound.play()  # start the sound (it finishes automatically)
        elif practice_sound.status == STARTED and t >= (2.5 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            practice_sound.stop()  # stop the sound (if longer than duration)
        
        # *key_resp_practice* updates
        if t >= 2.5 and key_resp_practice.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_practice.tStart = t  # underestimates by a little under one frame
            key_resp_practice.frameNStart = frameN  # exact frame index
            key_resp_practice.status = STARTED
            # keyboard checking is just starting
            key_resp_practice.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif key_resp_practice.status == STARTED and t >= (2.5 + (2.5-win.monitorFramePeriod*0.75)): #most of one frame period left
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
        
        # *practice_left* updates
        if t >= 3.0 and practice_left.status == NOT_STARTED:
            # keep track of start time/frame for later
            practice_left.tStart = t  # underestimates by a little under one frame
            practice_left.frameNStart = frameN  # exact frame index
            practice_left.setAutoDraw(True)
        elif practice_left.status == STARTED and t >= (3.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            practice_left.setAutoDraw(False)
        
        # *practice_right* updates
        if t >= 3.0 and practice_right.status == NOT_STARTED:
            # keep track of start time/frame for later
            practice_right.tStart = t  # underestimates by a little under one frame
            practice_right.frameNStart = frameN  # exact frame index
            practice_right.setAutoDraw(True)
        elif practice_right.status == STARTED and t >= (3.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            practice_right.setAutoDraw(False)
        
        # *fix* updates
        if t >= 2.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (2.0 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            fix.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
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
    
    #-------Ending Routine "practice"-------
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_practice.keys in ['', [], None]:  # No response was made
       key_resp_practice.keys=None
    # store data for practice_trial (TrialHandler)
    practice_trial.addData('key_resp_practice.keys',key_resp_practice.keys)
    if key_resp_practice.keys != None:  # we had a response
        practice_trial.addData('key_resp_practice.rt', key_resp_practice.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'practice_trial'

# get names of stimulus parameters
if practice_trial.trialList in ([], [None], None):  params = []
else:  params = practice_trial.trialList[0].keys()
# save data for this loop
practice_trial.saveAsExcel(filename + '.xlsx', sheetName='practice_trial',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
practice_trial.saveAsText(filename + 'practice_trial.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock 
frameN = -1
routineTimer.add(21.000000)
# update component parameters for each repeat
doneKey = event.BuilderKeyResponse()  # create an object of type KeyResponse
doneKey.status = NOT_STARTED
# keep track of which components have finished
endComponents = []
endComponents.append(done)
endComponents.append(doneKey)
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "end"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *done* updates
    if t >= 0.0 and done.status == NOT_STARTED:
        # keep track of start time/frame for later
        done.tStart = t  # underestimates by a little under one frame
        done.frameNStart = frameN  # exact frame index
        done.setAutoDraw(True)
    elif done.status == STARTED and t >= (0.0 + (20.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        done.setAutoDraw(False)
    
    # *doneKey* updates
    if t >= 1.0 and doneKey.status == NOT_STARTED:
        # keep track of start time/frame for later
        doneKey.tStart = t  # underestimates by a little under one frame
        doneKey.frameNStart = frameN  # exact frame index
        doneKey.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    elif doneKey.status == STARTED and t >= (1.0 + (20.0-win.monitorFramePeriod*0.75)): #most of one frame period left
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
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
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

#-------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
win.close()
core.quit()
