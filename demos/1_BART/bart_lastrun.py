#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.74.00), vie 24 oct 11:17:04 2014
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
expName = u'bart'  # from the Builder filename that created this script
expInfo = {u'participant': u'', u'age': u'', u'session': u'004', u'gender (m/f)': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/casillas/google_drive/14_fall_2014/proseminar/psychopy2_workshop/demos/1_BART/bart.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.WARNING)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(800, 600), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=[0,0,0], colorSpace='rgb',
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
instrMessage = visual.TextStim(win=win, ori=0, name='instrMessage',
    text="This is a game where you have to optimise your earnings in a balloon pumping competition.\n\nYou get prize money for each balloon you pump up, according to its size. But if you pump it too far it will pop and you'll get nothing for that balloon.\n\nBalloons differ in their maximum size - they can occasionally reach to almost the size of the screen but most will pop well before that.\n\nPress;\n    SPACE to pump the balloon\n    RETURN to bank the cash for this balloon and move onto the next\n",    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
bankedEarnings=0.0
lastBalloonEarnings=0.0
thisBalloonEarnings=0.0
balloonSize=0.08
balloonMsgHeight=0.01
balloonBody = visual.ImageStim(win=win, name='balloonBody',
    image='redBalloon.png', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
reminderMsg = visual.TextStim(win=win, ori=0, name='reminderMsg',
    text='Press SPACE to pump the balloon\nPress RETURN to bank this sum',    font='Arial',
    pos=[0, -0.8], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)
balloonValMsg = visual.TextStim(win=win, ori=0, name='balloonValMsg',
    text='default text',    font='Arial',
    pos=[0,0.05], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)
bankedMsg = visual.TextStim(win=win, ori=0, name='bankedMsg',
    text='default text',    font='Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)


# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedbackText=""
from psychopy import sound
bang = sound.Sound("bang.wav")

feedbackMsg = visual.TextStim(win=win, ori=0, name='feedbackMsg',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "finalScore"
finalScoreClock = core.Clock()
finalScore_2 = visual.TextStim(win=win, ori=0, name='finalScore_2',
    text='default text',    font='Arial',
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
# update component parameters for each repeat
resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
resp.status = NOT_STARTED
# keep track of which components have finished
instructionsComponents = []
instructionsComponents.append(instrMessage)
instructionsComponents.append(resp)
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrMessage* updates
    if t >= 0.0 and instrMessage.status == NOT_STARTED:
        # keep track of start time/frame for later
        instrMessage.tStart = t  # underestimates by a little under one frame
        instrMessage.frameNStart = frameN  # exact frame index
        instrMessage.setAutoDraw(True)
    
    # *resp* updates
    if t >= 0.0 and resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        resp.tStart = t  # underestimates by a little under one frame
        resp.frameNStart = frameN  # exact frame index
        resp.status = STARTED
        # keyboard checking is just starting
        resp.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if resp.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            resp.keys = theseKeys[-1]  # just the last key pressed
            resp.rt = resp.clock.getTime()
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
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if resp.keys in ['', [], None]:  # No response was made
   resp.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('resp.keys',resp.keys)
if resp.keys != None:  # we had a response
    thisExp.addData('resp.rt', resp.rt)
thisExp.nextEntry()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=u'/Users/casillas/google_drive/14_fall_2014/proseminar/psychopy2_workshop/demos/1_BART/bart.psyexp',
    trialList=data.importConditions('trialTypes.xlsx'),
    seed=1832, name='trials')
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
    
    balloonSize=0.08
    popped=False
    nPumps=0
    
    bankButton = event.BuilderKeyResponse()  # create an object of type KeyResponse
    bankButton.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(balloonBody)
    trialComponents.append(reminderMsg)
    trialComponents.append(balloonValMsg)
    trialComponents.append(bankedMsg)
    trialComponents.append(bankButton)
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
        thisBalloonEarnings=nPumps*0.05
        balloonSize=0.1+nPumps*0.015
        
        # *balloonBody* updates
        if t >= 0.0 and balloonBody.status == NOT_STARTED:
            # keep track of start time/frame for later
            balloonBody.tStart = t  # underestimates by a little under one frame
            balloonBody.frameNStart = frameN  # exact frame index
            balloonBody.setAutoDraw(True)
        if balloonBody.status == STARTED:  # only update if being drawn
            balloonBody.setPos([-1+balloonSize/2, 0], log=False)
            balloonBody.setSize(balloonSize, log=False)
        
        # *reminderMsg* updates
        if t >= 0.0 and reminderMsg.status == NOT_STARTED:
            # keep track of start time/frame for later
            reminderMsg.tStart = t  # underestimates by a little under one frame
            reminderMsg.frameNStart = frameN  # exact frame index
            reminderMsg.setAutoDraw(True)
        
        # *balloonValMsg* updates
        if t >= 0.0 and balloonValMsg.status == NOT_STARTED:
            # keep track of start time/frame for later
            balloonValMsg.tStart = t  # underestimates by a little under one frame
            balloonValMsg.frameNStart = frameN  # exact frame index
            balloonValMsg.setAutoDraw(True)
        if balloonValMsg.status == STARTED:  # only update if being drawn
            balloonValMsg.setText(u"This balloon value:\n£%.2f" %thisBalloonEarnings, log=False)
        
        # *bankedMsg* updates
        if t >= 0.0 and bankedMsg.status == NOT_STARTED:
            # keep track of start time/frame for later
            bankedMsg.tStart = t  # underestimates by a little under one frame
            bankedMsg.frameNStart = frameN  # exact frame index
            bankedMsg.setAutoDraw(True)
        if bankedMsg.status == STARTED:  # only update if being drawn
            bankedMsg.setText(u"You have banked:\n£%.2f" %bankedEarnings, log=False)
        if event.getKeys(['space']):
          nPumps=nPumps+1
          if nPumps>maxPumps:
            popped=True
            continueRoutine=False
        
        # *bankButton* updates
        if t >= 0.0 and bankButton.status == NOT_STARTED:
            # keep track of start time/frame for later
            bankButton.tStart = t  # underestimates by a little under one frame
            bankButton.frameNStart = frameN  # exact frame index
            bankButton.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if bankButton.status == STARTED:
            theseKeys = event.getKeys(keyList=['return'])
            
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
    #calculate cash 'earned'
    if popped:
      thisBalloonEarnings=0.0
      lastBalloonEarnings=0.0
    else:   lastBalloonEarnings=thisBalloonEarnings
    bankedEarnings = bankedEarnings+lastBalloonEarnings
    #save data
    trials.addData('nPumps', nPumps)
    trials.addData('size', balloonSize)
    trials.addData('earnings', thisBalloonEarnings)
    trials.addData('popped', popped)
    
    
    
    
    #------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    if popped==True:
      feedbackText="Oops! Lost that one!"
      bang.play()
    else:
      feedbackText=u"You banked £%.2f" %lastBalloonEarnings
    
    feedbackMsg.setText(feedbackText)
    # keep track of which components have finished
    feedbackComponents = []
    feedbackComponents.append(feedbackMsg)
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "feedback"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *feedbackMsg* updates
        if t >= 0.0 and feedbackMsg.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedbackMsg.tStart = t  # underestimates by a little under one frame
            feedbackMsg.frameNStart = frameN  # exact frame index
            feedbackMsg.setAutoDraw(True)
        elif feedbackMsg.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            feedbackMsg.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):  params = []
else:  params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "finalScore"-------
t = 0
finalScoreClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
finalScore_2.setText(u"Well done! You banked a total of\n£%2.f" %bankedEarnings)
doneKey = event.BuilderKeyResponse()  # create an object of type KeyResponse
doneKey.status = NOT_STARTED
# keep track of which components have finished
finalScoreComponents = []
finalScoreComponents.append(finalScore_2)
finalScoreComponents.append(doneKey)
for thisComponent in finalScoreComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "finalScore"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = finalScoreClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *finalScore_2* updates
    if t >= 0.0 and finalScore_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        finalScore_2.tStart = t  # underestimates by a little under one frame
        finalScore_2.frameNStart = frameN  # exact frame index
        finalScore_2.setAutoDraw(True)
    
    # *doneKey* updates
    if t >= 0.0 and doneKey.status == NOT_STARTED:
        # keep track of start time/frame for later
        doneKey.tStart = t  # underestimates by a little under one frame
        doneKey.frameNStart = frameN  # exact frame index
        doneKey.status = STARTED
        # keyboard checking is just starting
        doneKey.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if doneKey.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            doneKey.keys = theseKeys[-1]  # just the last key pressed
            doneKey.rt = doneKey.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finalScoreComponents:
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

#-------Ending Routine "finalScore"-------
for thisComponent in finalScoreComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if doneKey.keys in ['', [], None]:  # No response was made
   doneKey.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('doneKey.keys',doneKey.keys)
if doneKey.keys != None:  # we had a response
    thisExp.addData('doneKey.rt', doneKey.rt)
thisExp.nextEntry()




win.close()
core.quit()
