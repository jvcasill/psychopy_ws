#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Fri Feb 26 10:02:30 2016
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'borrowingLykert'  # from the Builder filename that created this script
expInfo = {u'participant': u'', u'session': u'001', u'group': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/casillas/academia/teaching/workshops/psychopy_ws/demos/9_borrowingLykert/borrowingLykert.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1680, 1050), fullscr=True, screen=0, allowGUI=True, allowStencil=False,
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
    text='Instructions go here.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "practice"
practiceClock = core.Clock()
rating = visual.RatingScale(win=win, name='rating', marker='circle', size=1.0, pos=[0.0, -0.4], low=0, high=1, precision=100, showValue=False, markerExpansion=0, scale='', markerStart='50')
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='Foreign',    font='Arial',
    pos=[-0.5, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text='Native',    font='Arial',
    pos=[0.5, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
sound_1 = sound.Sound('A', secs=-1)
sound_1.setVolume(1.0)

# Initialize components for Routine "got_it"
got_itClock = core.Clock()
gotIT = visual.TextStim(win=win, ori=0, name='gotIT',
    text='Got it? If you have any questions please ask the experimenter now. If not, press the spacebar to begin the experiment. ',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Break"
BreakClock = core.Clock()

break_text = visual.TextStim(win=win, ori=0, name='break_text',
    text='You may take a short break if you like. \nPress the spacebar to continue.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
numbersTrial = visual.TextStim(win=win, ori=0, name='numbersTrial',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
trial_sound = sound.Sound('A', secs=-1)
trial_sound.setVolume(1)
FoerignTrial = visual.TextStim(win=win, ori=0, name='FoerignTrial',
    text='Foreign',    font='Arial',
    pos=[-0.5, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)
nativeTrial = visual.TextStim(win=win, ori=0, name='nativeTrial',
    text='Native',    font='Arial',
    pos=[0.5, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)

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
    if instructions_text.status == STARTED and t >= (0.0 + (30.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        instructions_text.setAutoDraw(False)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED and t >= (0.0 + (30.0-win.monitorFramePeriod*0.75)): #most of one frame period left
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

#-------Ending Routine "instructions"-------
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
    # update component parameters for each repeat
    rating.reset()
    sound_1.setSound(stimuli, secs=-1)
    sound_1.setVolume(1)
    # keep track of which components have finished
    practiceComponents = []
    practiceComponents.append(rating)
    practiceComponents.append(text_3)
    practiceComponents.append(text_4)
    practiceComponents.append(sound_1)
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "practice"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = practiceClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *rating* updates
        if t >= 0.0 and rating.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating.tStart = t  # underestimates by a little under one frame
            rating.frameNStart = frameN  # exact frame index
            rating.setAutoDraw(True)
        continueRoutine &= rating.noResponse  # a response ends the trial
        
        # *text_3* updates
        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t  # underestimates by a little under one frame
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        
        # *text_4* updates
        if t >= 0.0 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t  # underestimates by a little under one frame
            text_4.frameNStart = frameN  # exact frame index
            text_4.setAutoDraw(True)
        # start/stop sound_1
        if t >= 0.5 and sound_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_1.tStart = t  # underestimates by a little under one frame
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.play()  # start the sound (it finishes automatically)
        
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
    
    #-------Ending Routine "practice"-------
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for practice_trial (TrialHandler)
    practice_trial.addData('rating.response', rating.getRating())
    practice_trial.addData('rating.rt', rating.getRT())
    sound_1.stop() #ensure sound has stopped at end of routine
    # the Routine "practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'practice_trial'

# get names of stimulus parameters
if practice_trial.trialList in ([], [None], None):  params = []
else:  params = practice_trial.trialList[0].keys()
# save data for this loop
practice_trial.saveAsText(filename + 'practice_trial.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "got_it"-------
t = 0
got_itClock.reset()  # clock 
frameN = -1
routineTimer.add(11.000000)
# update component parameters for each repeat
gotResponse = event.BuilderKeyResponse()  # create an object of type KeyResponse
gotResponse.status = NOT_STARTED
# keep track of which components have finished
got_itComponents = []
got_itComponents.append(gotIT)
got_itComponents.append(gotResponse)
for thisComponent in got_itComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "got_it"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = got_itClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *gotIT* updates
    if t >= 0.75 and gotIT.status == NOT_STARTED:
        # keep track of start time/frame for later
        gotIT.tStart = t  # underestimates by a little under one frame
        gotIT.frameNStart = frameN  # exact frame index
        gotIT.setAutoDraw(True)
    if gotIT.status == STARTED and t >= (0.75 + (10.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        gotIT.setAutoDraw(False)
    
    # *gotResponse* updates
    if t >= 1.0 and gotResponse.status == NOT_STARTED:
        # keep track of start time/frame for later
        gotResponse.tStart = t  # underestimates by a little under one frame
        gotResponse.frameNStart = frameN  # exact frame index
        gotResponse.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if gotResponse.status == STARTED and t >= (1.0 + (10.0-win.monitorFramePeriod*0.75)): #most of one frame period left
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

#-------Ending Routine "got_it"-------
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
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "Break"-------
    t = 0
    BreakClock.reset()  # clock 
    frameN = -1
    routineTimer.add(20.500000)
    # update component parameters for each repeat
    
    key_resp_break = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_break.status = NOT_STARTED
    # keep track of which components have finished
    BreakComponents = []
    BreakComponents.append(break_text)
    BreakComponents.append(key_resp_break)
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Break"-------
    continueRoutine = True
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
            break_text.tStart = t  # underestimates by a little under one frame
            break_text.frameNStart = frameN  # exact frame index
            break_text.setAutoDraw(True)
        if break_text.status == STARTED and t >= (0.5 + (20.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            break_text.setAutoDraw(False)
        
        # *key_resp_break* updates
        if t >= 0.5 and key_resp_break.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_break.tStart = t  # underestimates by a little under one frame
            key_resp_break.frameNStart = frameN  # exact frame index
            key_resp_break.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_break.status == STARTED and t >= (0.5 + (20.0-win.monitorFramePeriod*0.75)): #most of one frame period left
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
    
    #-------Ending Routine "Break"-------
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    numbersTrial.setText('1  2  3  4  5  6')
    trial_sound.setSound(stimuli, secs=3.0)
    key_resp_trial = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_trial.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(numbersTrial)
    trialComponents.append(trial_sound)
    trialComponents.append(key_resp_trial)
    trialComponents.append(FoerignTrial)
    trialComponents.append(nativeTrial)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *numbersTrial* updates
        if t >= 0.5 and numbersTrial.status == NOT_STARTED:
            # keep track of start time/frame for later
            numbersTrial.tStart = t  # underestimates by a little under one frame
            numbersTrial.frameNStart = frameN  # exact frame index
            numbersTrial.setAutoDraw(True)
        # start/stop trial_sound
        if t >= 0.5 and trial_sound.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_sound.tStart = t  # underestimates by a little under one frame
            trial_sound.frameNStart = frameN  # exact frame index
            trial_sound.play()  # start the sound (it finishes automatically)
        if trial_sound.status == STARTED and t >= (0.5 + (3.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            trial_sound.stop()  # stop the sound (if longer than duration)
        
        # *key_resp_trial* updates
        if t >= 0.5 and key_resp_trial.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_trial.tStart = t  # underestimates by a little under one frame
            key_resp_trial.frameNStart = frameN  # exact frame index
            key_resp_trial.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_trial.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_trial.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5', '6'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_trial.keys == []:  # then this was the first keypress
                    key_resp_trial.keys = theseKeys[0]  # just the first key pressed
                    key_resp_trial.rt = key_resp_trial.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
        
        # *FoerignTrial* updates
        if t >= 0.0 and FoerignTrial.status == NOT_STARTED:
            # keep track of start time/frame for later
            FoerignTrial.tStart = t  # underestimates by a little under one frame
            FoerignTrial.frameNStart = frameN  # exact frame index
            FoerignTrial.setAutoDraw(True)
        
        # *nativeTrial* updates
        if t >= 0.0 and nativeTrial.status == NOT_STARTED:
            # keep track of start time/frame for later
            nativeTrial.tStart = t  # underestimates by a little under one frame
            nativeTrial.frameNStart = frameN  # exact frame index
            nativeTrial.setAutoDraw(True)
        
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
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trial_sound.stop() #ensure sound has stopped at end of routine
    # check responses
    if key_resp_trial.keys in ['', [], None]:  # No response was made
       key_resp_trial.keys=None
    # store data for trials (TrialHandler)
    trials.addData('key_resp_trial.keys',key_resp_trial.keys)
    if key_resp_trial.keys != None:  # we had a response
        trials.addData('key_resp_trial.rt', key_resp_trial.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):  params = []
else:  params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsText(filename + 'trials.csv', delim=',',
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
    if done.status == STARTED and t >= (0.0 + (20.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        done.setAutoDraw(False)
    
    # *doneKey* updates
    if t >= 1.0 and doneKey.status == NOT_STARTED:
        # keep track of start time/frame for later
        doneKey.tStart = t  # underestimates by a little under one frame
        doneKey.frameNStart = frameN  # exact frame index
        doneKey.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if doneKey.status == STARTED and t >= (1.0 + (20.0-win.monitorFramePeriod*0.75)): #most of one frame period left
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

#-------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
