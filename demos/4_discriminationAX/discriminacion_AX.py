#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.74.03), Sun Sep 30 20:53:52 2012
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division #so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, gui, sound
from psychopy.constants import * #things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os #handy system and path functions

#store info about the experiment session
expName='None'#from the Builder filename that created this script
expInfo={'participant':''}
dlg=gui.DlgFromDict(dictionary=expInfo,title=expName)
if dlg.OK==False: core.quit() #user pressed cancel
expInfo['date']=data.getDateStr()#add a simple timestamp
expInfo['expName']=expName
#setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data') #if this fails (e.g. permissions) we will get error
filename='data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])
logFile=logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)#this outputs to the screen, not a file

#an ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)

#setup the Window
win = visual.Window(size=(1280, 800), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=[1.000,1.000,1.000], colorSpace=u'rgb')

#Initialise components for Routine "instrucciones"
instruccionesClock=core.Clock()
text_4=visual.TextStim(win=win, ori=0, name='text_4',
    text=u'aqu\xed van las instrucciones',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

#Initialise components for Routine "trial"
trialClock=core.Clock()
sound_1=sound.Sound('A',secs=0.25)
sound_1.setVolume(1)
sound_2=sound.Sound('A',secs=0.25)
sound_2.setVolume(1)
text=visual.TextStim(win=win, ori=0, name='text',
    text=u'iguales',
    font=u'Arial',
    pos=[-0.5, 0], height=0.1,wrapWidth=None,
    color=u'black', colorSpace=u'rgb', opacity=1,
    depth=-2.0)
text_2=visual.TextStim(win=win, ori=0, name='text_2',
    text=u'diferentes',
    font=u'Arial',
    pos=[0.5, 0], height=0.1,wrapWidth=None,
    color=u'black', colorSpace=u'rgb', opacity=1,
    depth=-3.0)
text_3=visual.TextStim(win=win, ori=0, name='text_3',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.2,wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-5.0)

#Initialise components for Routine "cierre"
cierreClock=core.Clock()
text_5=visual.TextStim(win=win, ori=0, name='text_5',
    text='gracias',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock=core.Clock() #to track the time since experiment started
routineTimer=core.CountdownTimer() #to track time remaining of each (non-slip) routine 

#------Prepare to start Routine"instrucciones"-------
t=0; instruccionesClock.reset() #clock 
frameN=-1
routineTimer.add(2.000000)
#update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse() #create an object of type KeyResponse
key_resp_2.status=NOT_STARTED
#keep track of which components have finished
instruccionesComponents=[]
instruccionesComponents.append(text_4)
instruccionesComponents.append(key_resp_2)
for thisComponent in instruccionesComponents:
    if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
#-------Start Routine "instrucciones"-------
continueRoutine=True
while continueRoutine and routineTimer.getTime()>0:
    #get current time
    t=instruccionesClock.getTime()
    frameN=frameN+1#number of completed frames (so 0 in first frame)
    #update/draw components on each frame
    
    #*text_4* updates
    if t>=0.0 and text_4.status==NOT_STARTED:
        #keep track of start time/frame for later
        text_4.tStart=t#underestimates by a little under one frame
        text_4.frameNStart=frameN#exact frame index
        text_4.setAutoDraw(True)
    elif text_4.status==STARTED and t>=(0.0+2.0):
        text_4.setAutoDraw(False)
    
    #*key_resp_2* updates
    if t>=0.0 and key_resp_2.status==NOT_STARTED:
        #keep track of start time/frame for later
        key_resp_2.tStart=t#underestimates by a little under one frame
        key_resp_2.frameNStart=frameN#exact frame index
        key_resp_2.status=STARTED
        #keyboard checking is just starting
        key_resp_2.clock.reset() # now t=0
    elif key_resp_2.status==STARTED and t>=(0.0+2.0):
        key_resp_2.status=STOPPED
    if key_resp_2.status==STARTED:#only update if being drawn
        theseKeys = event.getKeys(keyList=['z', 'm'])
        if len(theseKeys)>0:#at least one key was pressed
            key_resp_2.keys=theseKeys[-1]#just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
    
    #check if all components have finished
    if not continueRoutine: #a component has requested that we end
        routineTimer.reset() #this is the new t0 for non-slip Routines
        break
    continueRoutine=False#will revert to True if at least one component still running
    for thisComponent in instruccionesComponents:
        if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
            continueRoutine=True; break#at least one component has not yet finished
    
    #check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    #refresh the screen
    if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
        win.flip()

#End of Routine "instrucciones"
for thisComponent in instruccionesComponents:
    if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)

#set up handler to look after randomisation of conditions etc
trials=data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('condiciones_bda_discriminacion_AX.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)#add the loop to the experiment
thisTrial=trials.trialList[0]#so we can initialise stimuli with some values
#abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial!=None:
    for paramName in thisTrial.keys():
        exec(paramName+'=thisTrial.'+paramName)

for thisTrial in trials:
    currentLoop = trials
    #abbrieviate parameter names if possible (e.g. rgb=thisTrial.rgb)
    if thisTrial!=None:
        for paramName in thisTrial.keys():
            exec(paramName+'=thisTrial.'+paramName)
    
    #------Prepare to start Routine"trial"-------
    t=0; trialClock.reset() #clock 
    frameN=-1
    routineTimer.add(3.000000)
    #update component parameters for each repeat
    sound_1.setSound(sonido1)
    sound_2.setSound(sonido2)
    key_resp = event.BuilderKeyResponse() #create an object of type KeyResponse
    key_resp.status=NOT_STARTED
    #keep track of which components have finished
    trialComponents=[]
    trialComponents.append(sound_1)
    trialComponents.append(sound_2)
    trialComponents.append(text)
    trialComponents.append(text_2)
    trialComponents.append(key_resp)
    trialComponents.append(text_3)
    for thisComponent in trialComponents:
        if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
    #-------Start Routine "trial"-------
    continueRoutine=True
    while continueRoutine and routineTimer.getTime()>0:
        #get current time
        t=trialClock.getTime()
        frameN=frameN+1#number of completed frames (so 0 in first frame)
        #update/draw components on each frame
        #start/stop sound_1
        if t>=0.25 and sound_1.status==NOT_STARTED:
            #keep track of start time/frame for later
            sound_1.tStart=t#underestimates by a little under one frame
            sound_1.frameNStart=frameN#exact frame index
            sound_1.play()#start the sound (it finishes automatically)
        elif sound_1.status==STARTED and t>=(0.25+0.25):
            sound_1.stop()#stop the sound (if longer than duration)
        #start/stop sound_2
        if t>=1 and sound_2.status==NOT_STARTED:
            #keep track of start time/frame for later
            sound_2.tStart=t#underestimates by a little under one frame
            sound_2.frameNStart=frameN#exact frame index
            sound_2.play()#start the sound (it finishes automatically)
        elif sound_2.status==STARTED and t>=(1+0.25):
            sound_2.stop()#stop the sound (if longer than duration)
        
        #*text* updates
        if t>=0.25 and text.status==NOT_STARTED:
            #keep track of start time/frame for later
            text.tStart=t#underestimates by a little under one frame
            text.frameNStart=frameN#exact frame index
            text.setAutoDraw(True)
        elif text.status==STARTED and t>=(0.25+2.75):
            text.setAutoDraw(False)
        
        #*text_2* updates
        if t>=0.25 and text_2.status==NOT_STARTED:
            #keep track of start time/frame for later
            text_2.tStart=t#underestimates by a little under one frame
            text_2.frameNStart=frameN#exact frame index
            text_2.setAutoDraw(True)
        elif text_2.status==STARTED and t>=(0.25+2.75):
            text_2.setAutoDraw(False)
        
        #*key_resp* updates
        if t>=1.0 and key_resp.status==NOT_STARTED:
            #keep track of start time/frame for later
            key_resp.tStart=t#underestimates by a little under one frame
            key_resp.frameNStart=frameN#exact frame index
            key_resp.status=STARTED
            #keyboard checking is just starting
            key_resp.clock.reset() # now t=0
        elif key_resp.status==STARTED and t>=(1.0+2.0):
            key_resp.status=STOPPED
        if key_resp.status==STARTED:#only update if being drawn
            theseKeys = event.getKeys(keyList=['z', 'm'])
            if len(theseKeys)>0:#at least one key was pressed
                if key_resp.keys==[]:#then this was the first keypress
                    key_resp.keys=theseKeys[0]#just the first key pressed
                    key_resp.rt = key_resp.clock.getTime()
                    #was this 'correct'?
                    if (key_resp.keys==str(correcto)): key_resp.corr=1
                    else: key_resp.corr=0
        
        #*text_3* updates
        if t>=0.0 and text_3.status==NOT_STARTED:
            #keep track of start time/frame for later
            text_3.tStart=t#underestimates by a little under one frame
            text_3.frameNStart=frameN#exact frame index
            text_3.setAutoDraw(True)
        elif text_3.status==STARTED and t>=(0.0+0.2):
            text_3.setAutoDraw(False)
        
        #check if all components have finished
        if not continueRoutine: #a component has requested that we end
            routineTimer.reset() #this is the new t0 for non-slip Routines
            break
        continueRoutine=False#will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
                continueRoutine=True; break#at least one component has not yet finished
        
        #check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        #refresh the screen
        if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #End of Routine "trial"
    for thisComponent in trialComponents:
        if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)
    #check responses
    if len(key_resp.keys)==0: #No response was made
       key_resp.keys=None
       #was no response the correct answer?!
       if str(correcto).lower()=='none':key_resp.corr=1 #correct non-response
       else: key_resp.corr=0 #failed to respond (incorrectly)
    #store data for trials (TrialHandler)
    trials.addData('key_resp.keys',key_resp.keys)
    trials.addData('key_resp.corr',key_resp.corr)
    if key_resp.keys != None:#we had a response
        trials.addData('key_resp.rt',key_resp.rt)
    thisExp.nextEntry()

#completed 2 repeats of 'trials'

#get names of stimulus parameters
if trials.trialList in ([], [None], None):  params=[]
else:  params = trials.trialList[0].keys()
#save data for this loop
trials.saveAsPickle(filename+'trials', fileCollisionMethod='rename')
trials.saveAsExcel(filename+'.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine"cierre"-------
t=0; cierreClock.reset() #clock 
frameN=-1
routineTimer.add(2.000000)
#update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse() #create an object of type KeyResponse
key_resp_3.status=NOT_STARTED
#keep track of which components have finished
cierreComponents=[]
cierreComponents.append(text_5)
cierreComponents.append(key_resp_3)
for thisComponent in cierreComponents:
    if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
#-------Start Routine "cierre"-------
continueRoutine=True
while continueRoutine and routineTimer.getTime()>0:
    #get current time
    t=cierreClock.getTime()
    frameN=frameN+1#number of completed frames (so 0 in first frame)
    #update/draw components on each frame
    
    #*text_5* updates
    if t>=0.0 and text_5.status==NOT_STARTED:
        #keep track of start time/frame for later
        text_5.tStart=t#underestimates by a little under one frame
        text_5.frameNStart=frameN#exact frame index
        text_5.setAutoDraw(True)
    elif text_5.status==STARTED and t>=(0.0+2.0):
        text_5.setAutoDraw(False)
    
    #*key_resp_3* updates
    if t>=0.0 and key_resp_3.status==NOT_STARTED:
        #keep track of start time/frame for later
        key_resp_3.tStart=t#underestimates by a little under one frame
        key_resp_3.frameNStart=frameN#exact frame index
        key_resp_3.status=STARTED
        #keyboard checking is just starting
        key_resp_3.clock.reset() # now t=0
    elif key_resp_3.status==STARTED and t>=(0.0+2.0):
        key_resp_3.status=STOPPED
    if key_resp_3.status==STARTED:#only update if being drawn
        theseKeys = event.getKeys(keyList=['space'])
        if len(theseKeys)>0:#at least one key was pressed
            key_resp_3.keys=theseKeys[-1]#just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
    
    #check if all components have finished
    if not continueRoutine: #a component has requested that we end
        routineTimer.reset() #this is the new t0 for non-slip Routines
        break
    continueRoutine=False#will revert to True if at least one component still running
    for thisComponent in cierreComponents:
        if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
            continueRoutine=True; break#at least one component has not yet finished
    
    #check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    #refresh the screen
    if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
        win.flip()

#End of Routine "cierre"
for thisComponent in cierreComponents:
    if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)

#Shutting down:
win.close()
core.quit()
