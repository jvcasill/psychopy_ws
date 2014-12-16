#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.73.05), Sat Oct  4 13:53:21 2014
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui, microphone
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Store info about the experiment session
expName = u'voiceCapture'  # from the Builder filename that created this script
expInfo = {'participant':'demo', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup filename for saving
filename = u'data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/casillas/google_drive/14_fall_2014/proseminar/psychopy2_workshop/PsychoPy2 Demos/voiceCapture/voiceCapture.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation
wavDirName = filename + '_wav'
if not os.path.isdir(wavDirName):
    os.makedirs(wavDirName)  # to hold .wav files

# Setup the Window
win = visual.Window(size=[800,600], fullscr=False, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )

# Enable sound input/output:
microphone.switchOn()
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instr"
instrClock = core.Clock()
instructions = visual.TextStim(win=win, ori=0, name='instructions',
    text="Say the written word outloud in English as fast as you can. ready?\n(please turn on your microphone)\npress any key to start",    font=u'Arial',
    pos=[0, 0], height=0.07, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
stimuli = visual.TextStim(win=win, ori=0, name='stimuli',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=1.0, colorSpace=u'rgb', opacity=1,
    depth=0.0)
show_filename = visual.TextStim(win=win, ori=0, name='show_filename',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.07, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-2.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "instr"-------
t = 0
instrClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
instrComponents = []
instrComponents.append(instructions)
instrComponents.append(key_resp_2)
for thisComponent in instrComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions* updates
    if t >= 0.0 and instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions.tStart = t  # underestimates by a little under one frame
        instructions.frameNStart = frameN  # exact frame index
        instructions.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 1.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys()
        
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
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "instr"-------
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method=u'random', 
    extraInfo=expInfo, originPath=u'/Users/casillas/google_drive/14_fall_2014/proseminar/psychopy2_workshop/PsychoPy2 Demos/voiceCapture/voiceCapture.psyexp',
    trialList=data.importConditions(u'trials.xlsx'),
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
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    stimuli.setColor(letterColor, colorSpace=u'rgb')
    stimuli.setText(text)
    mic = microphone.AdvAudioCapture(name='mic', saveDir=wavDirName, stereo=False)
    any_key_cont = event.BuilderKeyResponse()  # create an object of type KeyResponse
    any_key_cont.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(stimuli)
    trialComponents.append(mic)
    trialComponents.append(show_filename)
    trialComponents.append(any_key_cont)
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
        
        # *stimuli* updates
        if t >= 0.0 and stimuli.status == NOT_STARTED:
            # keep track of start time/frame for later
            stimuli.tStart = t  # underestimates by a little under one frame
            stimuli.frameNStart = frameN  # exact frame index
            stimuli.setAutoDraw(True)
        elif stimuli.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
            stimuli.setAutoDraw(False)
        
        # *mic* updates
        if t >= 0 and mic.status == NOT_STARTED:
            # keep track of start time/frame for later
            mic.tStart = t  # underestimates by a little under one frame
            mic.frameNStart = frameN  # exact frame index
            mic.status = STARTED
            mic.record(sec=0, block=False)  # start the recording thread
        
        if mic.status == STARTED and not mic.recorder.running:
            mic.status = FINISHED
        
        # *show_filename* updates
        if t >= 03. and show_filename.status == NOT_STARTED:
            # keep track of start time/frame for later
            show_filename.tStart = t  # underestimates by a little under one frame
            show_filename.frameNStart = frameN  # exact frame index
            show_filename.setAutoDraw(True)
        if show_filename.status == STARTED:  # only update if being drawn
            show_filename.setText("saved file = %s\nhit any key to continue" % (mic.savedFile), log=False)
        
        # *any_key_cont* updates
        if t >= 0 and any_key_cont.status == NOT_STARTED:
            # keep track of start time/frame for later
            any_key_cont.tStart = t  # underestimates by a little under one frame
            any_key_cont.frameNStart = frameN  # exact frame index
            any_key_cont.status = STARTED
            # keyboard checking is just starting
            any_key_cont.clock.reset()  # now t=0
        if any_key_cont.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if any_key_cont.keys == []:  # then this was the first keypress
                    any_key_cont.keys = theseKeys[0]  # just the first key pressed
                    any_key_cont.rt = any_key_cont.clock.getTime()
                    # was this 'correct'?
                    if (any_key_cont.keys == str(corrAns)) or (any_key_cont.keys == corrAns):
                        any_key_cont.corr = 1
                    else:
                        any_key_cont.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
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
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if not mic.savedFile:
        mic.savedFile = None
    # store data for trials (TrialHandler)
    trials.addData('mic.filename', mic.savedFile)
    # check responses
    if any_key_cont.keys in ['', [], None]:  # No response was made
       any_key_cont.keys=None
       # was no response the correct answer?!
       if str(corrAns).lower() == 'none': any_key_cont.corr = 1  # correct non-response
       else: any_key_cont.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('any_key_cont.keys',any_key_cont.keys)
    trials.addData('any_key_cont.corr', any_key_cont.corr)
    if any_key_cont.keys != None:  # we had a response
        trials.addData('any_key_cont.rt', any_key_cont.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):  params = []
else:  params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
win.close()
core.quit()
