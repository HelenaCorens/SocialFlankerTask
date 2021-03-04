#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.2),
    on Thu Mar  4 15:25:27 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.2'
expName = 'Test2_CLEAN_rpep_Helena'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/HC/SocialFlankerRPEP/Test2_CLEAN_rpep_Helena_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 800], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
welcome_txt = visual.TextStim(win=win, name='welcome_txt',
    text='Hello and welcome.\n\nYou are taking part in a task interaction experiment with another participant. You will both do the same task which will be given in a sequence of 3 trials.\nBefore the task, instructions will be given to either respond yourself or to observe how the other particpant responded. \n\nThe goal is to keep track of the errors of the other participant. After every 3 trials, you have to point out if the other participant made a mistake or not.\n\nSince this is an online experiment, you will be interacting with a previous participant. This means that you will interact with the other person by his/hers stored data. \n\nPress the spacebar to go continue.\n',
    font='Arial',
    units='norm', pos=(0,0), height=0.063, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
welcome_key = keyboard.Keyboard()

# Initialize components for Routine "General_Instruction"
General_InstructionClock = core.Clock()
general_instruct_txt = visual.TextStim(win=win, name='general_instruct_txt',
    text='You will see a row of five arrowheads next to eachother like this: \n<<<<< \n\nFocus on the arrowhead in the middle:\n- PRESS ‘ f ‘ on the keyboard when middle arrowhead is pointed to the LEFT\n\n- PRESS ‘ j ‘ on the keyboard when middle arrowhead is pointed to the RIGHT\n\nThe arrowheads around the middle one can have another direction like this: \n<<><<\n\nOnly respond to the direction of the arrowhead in the middle \n(in this case: right —>  press ‘j’).  Ignore the arrowheads around it. \n\nAnswer as fast as possible!\nIf you understand these instructions, press the spacebar to continue. \n',
    font='Arial',
    units='norm', pos=(0, 0), height=0.063, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
general_instruct_key = keyboard.Keyboard()

# Initialize components for Routine "Practice"
PracticeClock = core.Clock()

# Initialize components for Routine "OPP_instruct"
OPP_instructClock = core.Clock()
sequence_instruct_txt = visual.TextStim(win=win, name='sequence_instruct_txt',
    text='OBSERVE\nPERFORM\nPERFORM\n\npress space bar\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
seq_instruct_key = keyboard.Keyboard()

# Initialize components for Routine "O"
OClock = core.Clock()
Rectangles = visual.ImageStim(
    win=win,
    name='Rectangles', 
    image='rectsocial/rect_neutral.jpg', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
Rectangle_O_Reaction = visual.ImageStim(
    win=win,
    name='Rectangle_O_Reaction', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
txt_O = visual.TextStim(win=win, name='txt_O',
    text='',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "RSI"
RSIClock = core.Clock()
RSI_txt = visual.TextStim(win=win, name='RSI_txt',
    text='',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "P"
PClock = core.Clock()
Rectangles_2 = visual.ImageStim(
    win=win,
    name='Rectangles_2', 
    image='rectsocial/rect_neutral.jpg', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
Key_resp_P = keyboard.Keyboard()
txt_P = visual.TextStim(win=win, name='txt_P',
    text='',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "RSI"
RSIClock = core.Clock()
RSI_txt = visual.TextStim(win=win, name='RSI_txt',
    text='',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "P"
PClock = core.Clock()
Rectangles_2 = visual.ImageStim(
    win=win,
    name='Rectangles_2', 
    image='rectsocial/rect_neutral.jpg', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
Key_resp_P = keyboard.Keyboard()
txt_P = visual.TextStim(win=win, name='txt_P',
    text='',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Error_estimation"
Error_estimationClock = core.Clock()
error_est_txt = visual.TextStim(win=win, name='error_est_txt',
    text='\nHow many errors did the other participant make?\n\n0 = press ‘a’ on keyboard\n1 = press ‘p’ on keyboard\n\n\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
error_est_key = keyboard.Keyboard()

# Initialize components for Routine "POP_instruct"
POP_instructClock = core.Clock()
pop_instruct_txt = visual.TextStim(win=win, name='pop_instruct_txt',
    text='PERFORM \nOBSERVE\nPERFORM\n\npress space bar when ready\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
pop_instruct_key = keyboard.Keyboard()

# Initialize components for Routine "P"
PClock = core.Clock()
Rectangles_2 = visual.ImageStim(
    win=win,
    name='Rectangles_2', 
    image='rectsocial/rect_neutral.jpg', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
Key_resp_P = keyboard.Keyboard()
txt_P = visual.TextStim(win=win, name='txt_P',
    text='',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "RSI"
RSIClock = core.Clock()
RSI_txt = visual.TextStim(win=win, name='RSI_txt',
    text='',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "O"
OClock = core.Clock()
Rectangles = visual.ImageStim(
    win=win,
    name='Rectangles', 
    image='rectsocial/rect_neutral.jpg', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
Rectangle_O_Reaction = visual.ImageStim(
    win=win,
    name='Rectangle_O_Reaction', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
txt_O = visual.TextStim(win=win, name='txt_O',
    text='',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "RSI"
RSIClock = core.Clock()
RSI_txt = visual.TextStim(win=win, name='RSI_txt',
    text='',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "P"
PClock = core.Clock()
Rectangles_2 = visual.ImageStim(
    win=win,
    name='Rectangles_2', 
    image='rectsocial/rect_neutral.jpg', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
Key_resp_P = keyboard.Keyboard()
txt_P = visual.TextStim(win=win, name='txt_P',
    text='',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Error_estimation"
Error_estimationClock = core.Clock()
error_est_txt = visual.TextStim(win=win, name='error_est_txt',
    text='\nHow many errors did the other participant make?\n\n0 = press ‘a’ on keyboard\n1 = press ‘p’ on keyboard\n\n\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
error_est_key = keyboard.Keyboard()

# Initialize components for Routine "Goodbye"
GoodbyeClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome"-------
continueRoutine = True
# update component parameters for each repeat
welcome_key.keys = []
welcome_key.rt = []
_welcome_key_allKeys = []
# keep track of which components have finished
WelcomeComponents = [welcome_txt, welcome_key]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome"-------
while continueRoutine:
    # get current time
    t = WelcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_txt* updates
    if welcome_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_txt.frameNStart = frameN  # exact frame index
        welcome_txt.tStart = t  # local t and not account for scr refresh
        welcome_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_txt, 'tStartRefresh')  # time at next scr refresh
        welcome_txt.setAutoDraw(True)
    
    # *welcome_key* updates
    waitOnFlip = False
    if welcome_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_key.frameNStart = frameN  # exact frame index
        welcome_key.tStart = t  # local t and not account for scr refresh
        welcome_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_key, 'tStartRefresh')  # time at next scr refresh
        welcome_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcome_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(welcome_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if welcome_key.status == STARTED and not waitOnFlip:
        theseKeys = welcome_key.getKeys(keyList=['space'], waitRelease=False)
        _welcome_key_allKeys.extend(theseKeys)
        if len(_welcome_key_allKeys):
            welcome_key.keys = _welcome_key_allKeys[-1].name  # just the last key pressed
            welcome_key.rt = _welcome_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('welcome_txt.started', welcome_txt.tStartRefresh)
thisExp.addData('welcome_txt.stopped', welcome_txt.tStopRefresh)
# check responses
if welcome_key.keys in ['', [], None]:  # No response was made
    welcome_key.keys = None
thisExp.addData('welcome_key.keys',welcome_key.keys)
if welcome_key.keys != None:  # we had a response
    thisExp.addData('welcome_key.rt', welcome_key.rt)
thisExp.addData('welcome_key.started', welcome_key.tStartRefresh)
thisExp.addData('welcome_key.stopped', welcome_key.tStopRefresh)
thisExp.nextEntry()
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "General_Instruction"-------
continueRoutine = True
# update component parameters for each repeat
general_instruct_key.keys = []
general_instruct_key.rt = []
_general_instruct_key_allKeys = []
# keep track of which components have finished
General_InstructionComponents = [general_instruct_txt, general_instruct_key]
for thisComponent in General_InstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
General_InstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "General_Instruction"-------
while continueRoutine:
    # get current time
    t = General_InstructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=General_InstructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *general_instruct_txt* updates
    if general_instruct_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        general_instruct_txt.frameNStart = frameN  # exact frame index
        general_instruct_txt.tStart = t  # local t and not account for scr refresh
        general_instruct_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(general_instruct_txt, 'tStartRefresh')  # time at next scr refresh
        general_instruct_txt.setAutoDraw(True)
    
    # *general_instruct_key* updates
    waitOnFlip = False
    if general_instruct_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        general_instruct_key.frameNStart = frameN  # exact frame index
        general_instruct_key.tStart = t  # local t and not account for scr refresh
        general_instruct_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(general_instruct_key, 'tStartRefresh')  # time at next scr refresh
        general_instruct_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(general_instruct_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(general_instruct_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if general_instruct_key.status == STARTED and not waitOnFlip:
        theseKeys = general_instruct_key.getKeys(keyList=['space'], waitRelease=False)
        _general_instruct_key_allKeys.extend(theseKeys)
        if len(_general_instruct_key_allKeys):
            general_instruct_key.keys = _general_instruct_key_allKeys[-1].name  # just the last key pressed
            general_instruct_key.rt = _general_instruct_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in General_InstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "General_Instruction"-------
for thisComponent in General_InstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('general_instruct_txt.started', general_instruct_txt.tStartRefresh)
thisExp.addData('general_instruct_txt.stopped', general_instruct_txt.tStopRefresh)
# check responses
if general_instruct_key.keys in ['', [], None]:  # No response was made
    general_instruct_key.keys = None
thisExp.addData('general_instruct_key.keys',general_instruct_key.keys)
if general_instruct_key.keys != None:  # we had a response
    thisExp.addData('general_instruct_key.rt', general_instruct_key.rt)
thisExp.addData('general_instruct_key.started', general_instruct_key.tStartRefresh)
thisExp.addData('general_instruct_key.stopped', general_instruct_key.tStopRefresh)
thisExp.nextEntry()
# the Routine "General_Instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Practice"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
PracticeComponents = []
for thisComponent in PracticeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Practice"-------
while continueRoutine:
    # get current time
    t = PracticeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PracticeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PracticeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Practice"-------
for thisComponent in PracticeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Practice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Block = data.TrialHandler(nReps=10, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Block')
thisExp.addLoop(Block)  # add the loop to the experiment
thisBlock = Block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in Block:
    currentLoop = Block
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "OPP_instruct"-------
    continueRoutine = True
    # update component parameters for each repeat
    seq_instruct_key.keys = []
    seq_instruct_key.rt = []
    _seq_instruct_key_allKeys = []
    # keep track of which components have finished
    OPP_instructComponents = [sequence_instruct_txt, seq_instruct_key]
    for thisComponent in OPP_instructComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    OPP_instructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "OPP_instruct"-------
    while continueRoutine:
        # get current time
        t = OPP_instructClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=OPP_instructClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sequence_instruct_txt* updates
        if sequence_instruct_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sequence_instruct_txt.frameNStart = frameN  # exact frame index
            sequence_instruct_txt.tStart = t  # local t and not account for scr refresh
            sequence_instruct_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sequence_instruct_txt, 'tStartRefresh')  # time at next scr refresh
            sequence_instruct_txt.setAutoDraw(True)
        
        # *seq_instruct_key* updates
        waitOnFlip = False
        if seq_instruct_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            seq_instruct_key.frameNStart = frameN  # exact frame index
            seq_instruct_key.tStart = t  # local t and not account for scr refresh
            seq_instruct_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seq_instruct_key, 'tStartRefresh')  # time at next scr refresh
            seq_instruct_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(seq_instruct_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(seq_instruct_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if seq_instruct_key.status == STARTED and not waitOnFlip:
            theseKeys = seq_instruct_key.getKeys(keyList=['space'], waitRelease=False)
            _seq_instruct_key_allKeys.extend(theseKeys)
            if len(_seq_instruct_key_allKeys):
                seq_instruct_key.keys = _seq_instruct_key_allKeys[-1].name  # just the last key pressed
                seq_instruct_key.rt = _seq_instruct_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in OPP_instructComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "OPP_instruct"-------
    for thisComponent in OPP_instructComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Block.addData('sequence_instruct_txt.started', sequence_instruct_txt.tStartRefresh)
    Block.addData('sequence_instruct_txt.stopped', sequence_instruct_txt.tStopRefresh)
    # check responses
    if seq_instruct_key.keys in ['', [], None]:  # No response was made
        seq_instruct_key.keys = None
    Block.addData('seq_instruct_key.keys',seq_instruct_key.keys)
    if seq_instruct_key.keys != None:  # we had a response
        Block.addData('seq_instruct_key.rt', seq_instruct_key.rt)
    Block.addData('seq_instruct_key.started', seq_instruct_key.tStartRefresh)
    Block.addData('seq_instruct_key.stopped', seq_instruct_key.tStopRefresh)
    # the Routine "OPP_instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    OPP = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='OPP')
    thisExp.addLoop(OPP)  # add the loop to the experiment
    thisOPP = OPP.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisOPP.rgb)
    if thisOPP != None:
        for paramName in thisOPP:
            exec('{} = thisOPP[paramName]'.format(paramName))
    
    for thisOPP in OPP:
        currentLoop = OPP
        # abbreviate parameter names if possible (e.g. rgb = thisOPP.rgb)
        if thisOPP != None:
            for paramName in thisOPP:
                exec('{} = thisOPP[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        Trials_O1 = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('var_excel.xlsx', selection=random(1)*20),
            seed=None, name='Trials_O1')
        thisExp.addLoop(Trials_O1)  # add the loop to the experiment
        thisTrials_O1 = Trials_O1.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_O1.rgb)
        if thisTrials_O1 != None:
            for paramName in thisTrials_O1:
                exec('{} = thisTrials_O1[paramName]'.format(paramName))
        
        for thisTrials_O1 in Trials_O1:
            currentLoop = Trials_O1
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_O1.rgb)
            if thisTrials_O1 != None:
                for paramName in thisTrials_O1:
                    exec('{} = thisTrials_O1[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "O"-------
            continueRoutine = True
            # update component parameters for each repeat
            Rectangle_O_Reaction.setImage(resp_other)
            txt_O.setText(stimulus)
            # keep track of which components have finished
            OComponents = [Rectangles, Rectangle_O_Reaction, txt_O]
            for thisComponent in OComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            OClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "O"-------
            while continueRoutine:
                # get current time
                t = OClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=OClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Rectangles* updates
                if Rectangles.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Rectangles.frameNStart = frameN  # exact frame index
                    Rectangles.tStart = t  # local t and not account for scr refresh
                    Rectangles.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Rectangles, 'tStartRefresh')  # time at next scr refresh
                    Rectangles.setAutoDraw(True)
                if Rectangles.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Rectangles.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        Rectangles.tStop = t  # not accounting for scr refresh
                        Rectangles.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Rectangles, 'tStopRefresh')  # time at next scr refresh
                        Rectangles.setAutoDraw(False)
                
                # *Rectangle_O_Reaction* updates
                if Rectangle_O_Reaction.status == NOT_STARTED and tThisFlip >= rt_other-frameTolerance:
                    # keep track of start time/frame for later
                    Rectangle_O_Reaction.frameNStart = frameN  # exact frame index
                    Rectangle_O_Reaction.tStart = t  # local t and not account for scr refresh
                    Rectangle_O_Reaction.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Rectangle_O_Reaction, 'tStartRefresh')  # time at next scr refresh
                    Rectangle_O_Reaction.setAutoDraw(True)
                if Rectangle_O_Reaction.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Rectangle_O_Reaction.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        Rectangle_O_Reaction.tStop = t  # not accounting for scr refresh
                        Rectangle_O_Reaction.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Rectangle_O_Reaction, 'tStopRefresh')  # time at next scr refresh
                        Rectangle_O_Reaction.setAutoDraw(False)
                
                # *txt_O* updates
                if txt_O.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    txt_O.frameNStart = frameN  # exact frame index
                    txt_O.tStart = t  # local t and not account for scr refresh
                    txt_O.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(txt_O, 'tStartRefresh')  # time at next scr refresh
                    txt_O.setAutoDraw(True)
                if txt_O.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > txt_O.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        txt_O.tStop = t  # not accounting for scr refresh
                        txt_O.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(txt_O, 'tStopRefresh')  # time at next scr refresh
                        txt_O.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in OComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "O"-------
            for thisComponent in OComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            Trials_O1.addData('Rectangles.started', Rectangles.tStartRefresh)
            Trials_O1.addData('Rectangles.stopped', Rectangles.tStopRefresh)
            Trials_O1.addData('Rectangle_O_Reaction.started', Rectangle_O_Reaction.tStartRefresh)
            Trials_O1.addData('Rectangle_O_Reaction.stopped', Rectangle_O_Reaction.tStopRefresh)
            Trials_O1.addData('txt_O.started', txt_O.tStartRefresh)
            Trials_O1.addData('txt_O.stopped', txt_O.tStopRefresh)
            # the Routine "O" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'Trials_O1'
        
        # get names of stimulus parameters
        if Trials_O1.trialList in ([], [None], None):
            params = []
        else:
            params = Trials_O1.trialList[0].keys()
        # save data for this loop
        Trials_O1.saveAsExcel(filename + '.xlsx', sheetName='Trials_O1',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        Trials_O1.saveAsText(filename + 'Trials_O1.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # ------Prepare to start Routine "RSI"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        RSI_txt.setText('+')
        # keep track of which components have finished
        RSIComponents = [RSI_txt]
        for thisComponent in RSIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        RSIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "RSI"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = RSIClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=RSIClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *RSI_txt* updates
            if RSI_txt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                RSI_txt.frameNStart = frameN  # exact frame index
                RSI_txt.tStart = t  # local t and not account for scr refresh
                RSI_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RSI_txt, 'tStartRefresh')  # time at next scr refresh
                RSI_txt.setAutoDraw(True)
            if RSI_txt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > RSI_txt.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    RSI_txt.tStop = t  # not accounting for scr refresh
                    RSI_txt.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(RSI_txt, 'tStopRefresh')  # time at next scr refresh
                    RSI_txt.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in RSIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "RSI"-------
        for thisComponent in RSIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        OPP.addData('RSI_txt.started', RSI_txt.tStartRefresh)
        OPP.addData('RSI_txt.stopped', RSI_txt.tStopRefresh)
        
        # set up handler to look after randomisation of conditions etc
        Trials_P_2 = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('var_excel.xlsx', selection=random(1)*20),
            seed=None, name='Trials_P_2')
        thisExp.addLoop(Trials_P_2)  # add the loop to the experiment
        thisTrials_P_2 = Trials_P_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_P_2.rgb)
        if thisTrials_P_2 != None:
            for paramName in thisTrials_P_2:
                exec('{} = thisTrials_P_2[paramName]'.format(paramName))
        
        for thisTrials_P_2 in Trials_P_2:
            currentLoop = Trials_P_2
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_P_2.rgb)
            if thisTrials_P_2 != None:
                for paramName in thisTrials_P_2:
                    exec('{} = thisTrials_P_2[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "P"-------
            continueRoutine = True
            routineTimer.add(2.000000)
            # update component parameters for each repeat
            Key_resp_P.keys = []
            Key_resp_P.rt = []
            _Key_resp_P_allKeys = []
            txt_P.setText(stimulus)
            # keep track of which components have finished
            PComponents = [Rectangles_2, Key_resp_P, txt_P]
            for thisComponent in PComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            PClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "P"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = PClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=PClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Rectangles_2* updates
                if Rectangles_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Rectangles_2.frameNStart = frameN  # exact frame index
                    Rectangles_2.tStart = t  # local t and not account for scr refresh
                    Rectangles_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Rectangles_2, 'tStartRefresh')  # time at next scr refresh
                    Rectangles_2.setAutoDraw(True)
                if Rectangles_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Rectangles_2.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        Rectangles_2.tStop = t  # not accounting for scr refresh
                        Rectangles_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Rectangles_2, 'tStopRefresh')  # time at next scr refresh
                        Rectangles_2.setAutoDraw(False)
                
                # *Key_resp_P* updates
                waitOnFlip = False
                if Key_resp_P.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Key_resp_P.frameNStart = frameN  # exact frame index
                    Key_resp_P.tStart = t  # local t and not account for scr refresh
                    Key_resp_P.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Key_resp_P, 'tStartRefresh')  # time at next scr refresh
                    Key_resp_P.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(Key_resp_P.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(Key_resp_P.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if Key_resp_P.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Key_resp_P.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        Key_resp_P.tStop = t  # not accounting for scr refresh
                        Key_resp_P.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Key_resp_P, 'tStopRefresh')  # time at next scr refresh
                        Key_resp_P.status = FINISHED
                if Key_resp_P.status == STARTED and not waitOnFlip:
                    theseKeys = Key_resp_P.getKeys(keyList=['f', 'j'], waitRelease=False)
                    _Key_resp_P_allKeys.extend(theseKeys)
                    if len(_Key_resp_P_allKeys):
                        Key_resp_P.keys = _Key_resp_P_allKeys[-1].name  # just the last key pressed
                        Key_resp_P.rt = _Key_resp_P_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *txt_P* updates
                if txt_P.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    txt_P.frameNStart = frameN  # exact frame index
                    txt_P.tStart = t  # local t and not account for scr refresh
                    txt_P.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(txt_P, 'tStartRefresh')  # time at next scr refresh
                    txt_P.setAutoDraw(True)
                if txt_P.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > txt_P.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        txt_P.tStop = t  # not accounting for scr refresh
                        txt_P.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(txt_P, 'tStopRefresh')  # time at next scr refresh
                        txt_P.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in PComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "P"-------
            for thisComponent in PComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            Trials_P_2.addData('Rectangles_2.started', Rectangles_2.tStartRefresh)
            Trials_P_2.addData('Rectangles_2.stopped', Rectangles_2.tStopRefresh)
            # check responses
            if Key_resp_P.keys in ['', [], None]:  # No response was made
                Key_resp_P.keys = None
            Trials_P_2.addData('Key_resp_P.keys',Key_resp_P.keys)
            if Key_resp_P.keys != None:  # we had a response
                Trials_P_2.addData('Key_resp_P.rt', Key_resp_P.rt)
            Trials_P_2.addData('Key_resp_P.started', Key_resp_P.tStartRefresh)
            Trials_P_2.addData('Key_resp_P.stopped', Key_resp_P.tStopRefresh)
            Trials_P_2.addData('txt_P.started', txt_P.tStartRefresh)
            Trials_P_2.addData('txt_P.stopped', txt_P.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'Trials_P_2'
        
        # get names of stimulus parameters
        if Trials_P_2.trialList in ([], [None], None):
            params = []
        else:
            params = Trials_P_2.trialList[0].keys()
        # save data for this loop
        Trials_P_2.saveAsExcel(filename + '.xlsx', sheetName='Trials_P_2',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        Trials_P_2.saveAsText(filename + 'Trials_P_2.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # ------Prepare to start Routine "RSI"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        RSI_txt.setText('+')
        # keep track of which components have finished
        RSIComponents = [RSI_txt]
        for thisComponent in RSIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        RSIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "RSI"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = RSIClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=RSIClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *RSI_txt* updates
            if RSI_txt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                RSI_txt.frameNStart = frameN  # exact frame index
                RSI_txt.tStart = t  # local t and not account for scr refresh
                RSI_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RSI_txt, 'tStartRefresh')  # time at next scr refresh
                RSI_txt.setAutoDraw(True)
            if RSI_txt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > RSI_txt.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    RSI_txt.tStop = t  # not accounting for scr refresh
                    RSI_txt.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(RSI_txt, 'tStopRefresh')  # time at next scr refresh
                    RSI_txt.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in RSIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "RSI"-------
        for thisComponent in RSIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        OPP.addData('RSI_txt.started', RSI_txt.tStartRefresh)
        OPP.addData('RSI_txt.stopped', RSI_txt.tStopRefresh)
        
        # set up handler to look after randomisation of conditions etc
        Trials_P_3 = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('var_excel.xlsx', selection=random(1)*20),
            seed=None, name='Trials_P_3')
        thisExp.addLoop(Trials_P_3)  # add the loop to the experiment
        thisTrials_P_3 = Trials_P_3.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_P_3.rgb)
        if thisTrials_P_3 != None:
            for paramName in thisTrials_P_3:
                exec('{} = thisTrials_P_3[paramName]'.format(paramName))
        
        for thisTrials_P_3 in Trials_P_3:
            currentLoop = Trials_P_3
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_P_3.rgb)
            if thisTrials_P_3 != None:
                for paramName in thisTrials_P_3:
                    exec('{} = thisTrials_P_3[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "P"-------
            continueRoutine = True
            routineTimer.add(2.000000)
            # update component parameters for each repeat
            Key_resp_P.keys = []
            Key_resp_P.rt = []
            _Key_resp_P_allKeys = []
            txt_P.setText(stimulus)
            # keep track of which components have finished
            PComponents = [Rectangles_2, Key_resp_P, txt_P]
            for thisComponent in PComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            PClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "P"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = PClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=PClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Rectangles_2* updates
                if Rectangles_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Rectangles_2.frameNStart = frameN  # exact frame index
                    Rectangles_2.tStart = t  # local t and not account for scr refresh
                    Rectangles_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Rectangles_2, 'tStartRefresh')  # time at next scr refresh
                    Rectangles_2.setAutoDraw(True)
                if Rectangles_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Rectangles_2.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        Rectangles_2.tStop = t  # not accounting for scr refresh
                        Rectangles_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Rectangles_2, 'tStopRefresh')  # time at next scr refresh
                        Rectangles_2.setAutoDraw(False)
                
                # *Key_resp_P* updates
                waitOnFlip = False
                if Key_resp_P.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Key_resp_P.frameNStart = frameN  # exact frame index
                    Key_resp_P.tStart = t  # local t and not account for scr refresh
                    Key_resp_P.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Key_resp_P, 'tStartRefresh')  # time at next scr refresh
                    Key_resp_P.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(Key_resp_P.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(Key_resp_P.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if Key_resp_P.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Key_resp_P.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        Key_resp_P.tStop = t  # not accounting for scr refresh
                        Key_resp_P.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Key_resp_P, 'tStopRefresh')  # time at next scr refresh
                        Key_resp_P.status = FINISHED
                if Key_resp_P.status == STARTED and not waitOnFlip:
                    theseKeys = Key_resp_P.getKeys(keyList=['f', 'j'], waitRelease=False)
                    _Key_resp_P_allKeys.extend(theseKeys)
                    if len(_Key_resp_P_allKeys):
                        Key_resp_P.keys = _Key_resp_P_allKeys[-1].name  # just the last key pressed
                        Key_resp_P.rt = _Key_resp_P_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *txt_P* updates
                if txt_P.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    txt_P.frameNStart = frameN  # exact frame index
                    txt_P.tStart = t  # local t and not account for scr refresh
                    txt_P.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(txt_P, 'tStartRefresh')  # time at next scr refresh
                    txt_P.setAutoDraw(True)
                if txt_P.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > txt_P.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        txt_P.tStop = t  # not accounting for scr refresh
                        txt_P.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(txt_P, 'tStopRefresh')  # time at next scr refresh
                        txt_P.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in PComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "P"-------
            for thisComponent in PComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            Trials_P_3.addData('Rectangles_2.started', Rectangles_2.tStartRefresh)
            Trials_P_3.addData('Rectangles_2.stopped', Rectangles_2.tStopRefresh)
            # check responses
            if Key_resp_P.keys in ['', [], None]:  # No response was made
                Key_resp_P.keys = None
            Trials_P_3.addData('Key_resp_P.keys',Key_resp_P.keys)
            if Key_resp_P.keys != None:  # we had a response
                Trials_P_3.addData('Key_resp_P.rt', Key_resp_P.rt)
            Trials_P_3.addData('Key_resp_P.started', Key_resp_P.tStartRefresh)
            Trials_P_3.addData('Key_resp_P.stopped', Key_resp_P.tStopRefresh)
            Trials_P_3.addData('txt_P.started', txt_P.tStartRefresh)
            Trials_P_3.addData('txt_P.stopped', txt_P.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'Trials_P_3'
        
        # get names of stimulus parameters
        if Trials_P_3.trialList in ([], [None], None):
            params = []
        else:
            params = Trials_P_3.trialList[0].keys()
        # save data for this loop
        Trials_P_3.saveAsExcel(filename + '.xlsx', sheetName='Trials_P_3',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        Trials_P_3.saveAsText(filename + 'Trials_P_3.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        thisExp.nextEntry()
        
    # completed 1 repeats of 'OPP'
    
    # get names of stimulus parameters
    if OPP.trialList in ([], [None], None):
        params = []
    else:
        params = OPP.trialList[0].keys()
    # save data for this loop
    OPP.saveAsExcel(filename + '.xlsx', sheetName='OPP',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    OPP.saveAsText(filename + 'OPP.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "Error_estimation"-------
    continueRoutine = True
    # update component parameters for each repeat
    error_est_key.keys = []
    error_est_key.rt = []
    _error_est_key_allKeys = []
    # keep track of which components have finished
    Error_estimationComponents = [error_est_txt, error_est_key]
    for thisComponent in Error_estimationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Error_estimationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Error_estimation"-------
    while continueRoutine:
        # get current time
        t = Error_estimationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Error_estimationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *error_est_txt* updates
        if error_est_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            error_est_txt.frameNStart = frameN  # exact frame index
            error_est_txt.tStart = t  # local t and not account for scr refresh
            error_est_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(error_est_txt, 'tStartRefresh')  # time at next scr refresh
            error_est_txt.setAutoDraw(True)
        
        # *error_est_key* updates
        waitOnFlip = False
        if error_est_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            error_est_key.frameNStart = frameN  # exact frame index
            error_est_key.tStart = t  # local t and not account for scr refresh
            error_est_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(error_est_key, 'tStartRefresh')  # time at next scr refresh
            error_est_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(error_est_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(error_est_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if error_est_key.status == STARTED and not waitOnFlip:
            theseKeys = error_est_key.getKeys(keyList=['a', 'z'], waitRelease=False)
            _error_est_key_allKeys.extend(theseKeys)
            if len(_error_est_key_allKeys):
                error_est_key.keys = _error_est_key_allKeys[-1].name  # just the last key pressed
                error_est_key.rt = _error_est_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Error_estimationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Error_estimation"-------
    for thisComponent in Error_estimationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Block.addData('error_est_txt.started', error_est_txt.tStartRefresh)
    Block.addData('error_est_txt.stopped', error_est_txt.tStopRefresh)
    # check responses
    if error_est_key.keys in ['', [], None]:  # No response was made
        error_est_key.keys = None
    Block.addData('error_est_key.keys',error_est_key.keys)
    if error_est_key.keys != None:  # we had a response
        Block.addData('error_est_key.rt', error_est_key.rt)
    Block.addData('error_est_key.started', error_est_key.tStartRefresh)
    Block.addData('error_est_key.stopped', error_est_key.tStopRefresh)
    # the Routine "Error_estimation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "POP_instruct"-------
    continueRoutine = True
    # update component parameters for each repeat
    pop_instruct_key.keys = []
    pop_instruct_key.rt = []
    _pop_instruct_key_allKeys = []
    # keep track of which components have finished
    POP_instructComponents = [pop_instruct_txt, pop_instruct_key]
    for thisComponent in POP_instructComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    POP_instructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "POP_instruct"-------
    while continueRoutine:
        # get current time
        t = POP_instructClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=POP_instructClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pop_instruct_txt* updates
        if pop_instruct_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pop_instruct_txt.frameNStart = frameN  # exact frame index
            pop_instruct_txt.tStart = t  # local t and not account for scr refresh
            pop_instruct_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pop_instruct_txt, 'tStartRefresh')  # time at next scr refresh
            pop_instruct_txt.setAutoDraw(True)
        
        # *pop_instruct_key* updates
        waitOnFlip = False
        if pop_instruct_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pop_instruct_key.frameNStart = frameN  # exact frame index
            pop_instruct_key.tStart = t  # local t and not account for scr refresh
            pop_instruct_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pop_instruct_key, 'tStartRefresh')  # time at next scr refresh
            pop_instruct_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(pop_instruct_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(pop_instruct_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if pop_instruct_key.status == STARTED and not waitOnFlip:
            theseKeys = pop_instruct_key.getKeys(keyList=['space'], waitRelease=False)
            _pop_instruct_key_allKeys.extend(theseKeys)
            if len(_pop_instruct_key_allKeys):
                pop_instruct_key.keys = _pop_instruct_key_allKeys[-1].name  # just the last key pressed
                pop_instruct_key.rt = _pop_instruct_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in POP_instructComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "POP_instruct"-------
    for thisComponent in POP_instructComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Block.addData('pop_instruct_txt.started', pop_instruct_txt.tStartRefresh)
    Block.addData('pop_instruct_txt.stopped', pop_instruct_txt.tStopRefresh)
    # check responses
    if pop_instruct_key.keys in ['', [], None]:  # No response was made
        pop_instruct_key.keys = None
    Block.addData('pop_instruct_key.keys',pop_instruct_key.keys)
    if pop_instruct_key.keys != None:  # we had a response
        Block.addData('pop_instruct_key.rt', pop_instruct_key.rt)
    Block.addData('pop_instruct_key.started', pop_instruct_key.tStartRefresh)
    Block.addData('pop_instruct_key.stopped', pop_instruct_key.tStopRefresh)
    # the Routine "POP_instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    POP = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='POP')
    thisExp.addLoop(POP)  # add the loop to the experiment
    thisPOP = POP.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPOP.rgb)
    if thisPOP != None:
        for paramName in thisPOP:
            exec('{} = thisPOP[paramName]'.format(paramName))
    
    for thisPOP in POP:
        currentLoop = POP
        # abbreviate parameter names if possible (e.g. rgb = thisPOP.rgb)
        if thisPOP != None:
            for paramName in thisPOP:
                exec('{} = thisPOP[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        Trials_P_4 = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('var_excel.xlsx', selection=random(1)*20),
            seed=None, name='Trials_P_4')
        thisExp.addLoop(Trials_P_4)  # add the loop to the experiment
        thisTrials_P_4 = Trials_P_4.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_P_4.rgb)
        if thisTrials_P_4 != None:
            for paramName in thisTrials_P_4:
                exec('{} = thisTrials_P_4[paramName]'.format(paramName))
        
        for thisTrials_P_4 in Trials_P_4:
            currentLoop = Trials_P_4
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_P_4.rgb)
            if thisTrials_P_4 != None:
                for paramName in thisTrials_P_4:
                    exec('{} = thisTrials_P_4[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "P"-------
            continueRoutine = True
            routineTimer.add(2.000000)
            # update component parameters for each repeat
            Key_resp_P.keys = []
            Key_resp_P.rt = []
            _Key_resp_P_allKeys = []
            txt_P.setText(stimulus)
            # keep track of which components have finished
            PComponents = [Rectangles_2, Key_resp_P, txt_P]
            for thisComponent in PComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            PClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "P"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = PClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=PClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Rectangles_2* updates
                if Rectangles_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Rectangles_2.frameNStart = frameN  # exact frame index
                    Rectangles_2.tStart = t  # local t and not account for scr refresh
                    Rectangles_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Rectangles_2, 'tStartRefresh')  # time at next scr refresh
                    Rectangles_2.setAutoDraw(True)
                if Rectangles_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Rectangles_2.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        Rectangles_2.tStop = t  # not accounting for scr refresh
                        Rectangles_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Rectangles_2, 'tStopRefresh')  # time at next scr refresh
                        Rectangles_2.setAutoDraw(False)
                
                # *Key_resp_P* updates
                waitOnFlip = False
                if Key_resp_P.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Key_resp_P.frameNStart = frameN  # exact frame index
                    Key_resp_P.tStart = t  # local t and not account for scr refresh
                    Key_resp_P.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Key_resp_P, 'tStartRefresh')  # time at next scr refresh
                    Key_resp_P.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(Key_resp_P.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(Key_resp_P.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if Key_resp_P.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Key_resp_P.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        Key_resp_P.tStop = t  # not accounting for scr refresh
                        Key_resp_P.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Key_resp_P, 'tStopRefresh')  # time at next scr refresh
                        Key_resp_P.status = FINISHED
                if Key_resp_P.status == STARTED and not waitOnFlip:
                    theseKeys = Key_resp_P.getKeys(keyList=['f', 'j'], waitRelease=False)
                    _Key_resp_P_allKeys.extend(theseKeys)
                    if len(_Key_resp_P_allKeys):
                        Key_resp_P.keys = _Key_resp_P_allKeys[-1].name  # just the last key pressed
                        Key_resp_P.rt = _Key_resp_P_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *txt_P* updates
                if txt_P.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    txt_P.frameNStart = frameN  # exact frame index
                    txt_P.tStart = t  # local t and not account for scr refresh
                    txt_P.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(txt_P, 'tStartRefresh')  # time at next scr refresh
                    txt_P.setAutoDraw(True)
                if txt_P.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > txt_P.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        txt_P.tStop = t  # not accounting for scr refresh
                        txt_P.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(txt_P, 'tStopRefresh')  # time at next scr refresh
                        txt_P.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in PComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "P"-------
            for thisComponent in PComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            Trials_P_4.addData('Rectangles_2.started', Rectangles_2.tStartRefresh)
            Trials_P_4.addData('Rectangles_2.stopped', Rectangles_2.tStopRefresh)
            # check responses
            if Key_resp_P.keys in ['', [], None]:  # No response was made
                Key_resp_P.keys = None
            Trials_P_4.addData('Key_resp_P.keys',Key_resp_P.keys)
            if Key_resp_P.keys != None:  # we had a response
                Trials_P_4.addData('Key_resp_P.rt', Key_resp_P.rt)
            Trials_P_4.addData('Key_resp_P.started', Key_resp_P.tStartRefresh)
            Trials_P_4.addData('Key_resp_P.stopped', Key_resp_P.tStopRefresh)
            Trials_P_4.addData('txt_P.started', txt_P.tStartRefresh)
            Trials_P_4.addData('txt_P.stopped', txt_P.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'Trials_P_4'
        
        # get names of stimulus parameters
        if Trials_P_4.trialList in ([], [None], None):
            params = []
        else:
            params = Trials_P_4.trialList[0].keys()
        # save data for this loop
        Trials_P_4.saveAsExcel(filename + '.xlsx', sheetName='Trials_P_4',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        Trials_P_4.saveAsText(filename + 'Trials_P_4.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # ------Prepare to start Routine "RSI"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        RSI_txt.setText('+')
        # keep track of which components have finished
        RSIComponents = [RSI_txt]
        for thisComponent in RSIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        RSIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "RSI"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = RSIClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=RSIClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *RSI_txt* updates
            if RSI_txt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                RSI_txt.frameNStart = frameN  # exact frame index
                RSI_txt.tStart = t  # local t and not account for scr refresh
                RSI_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RSI_txt, 'tStartRefresh')  # time at next scr refresh
                RSI_txt.setAutoDraw(True)
            if RSI_txt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > RSI_txt.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    RSI_txt.tStop = t  # not accounting for scr refresh
                    RSI_txt.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(RSI_txt, 'tStopRefresh')  # time at next scr refresh
                    RSI_txt.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in RSIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "RSI"-------
        for thisComponent in RSIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        POP.addData('RSI_txt.started', RSI_txt.tStartRefresh)
        POP.addData('RSI_txt.stopped', RSI_txt.tStopRefresh)
        
        # set up handler to look after randomisation of conditions etc
        Trials_O_5 = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('var_excel.xlsx', selection=random(1)*20),
            seed=None, name='Trials_O_5')
        thisExp.addLoop(Trials_O_5)  # add the loop to the experiment
        thisTrials_O_5 = Trials_O_5.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_O_5.rgb)
        if thisTrials_O_5 != None:
            for paramName in thisTrials_O_5:
                exec('{} = thisTrials_O_5[paramName]'.format(paramName))
        
        for thisTrials_O_5 in Trials_O_5:
            currentLoop = Trials_O_5
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_O_5.rgb)
            if thisTrials_O_5 != None:
                for paramName in thisTrials_O_5:
                    exec('{} = thisTrials_O_5[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "O"-------
            continueRoutine = True
            # update component parameters for each repeat
            Rectangle_O_Reaction.setImage(resp_other)
            txt_O.setText(stimulus)
            # keep track of which components have finished
            OComponents = [Rectangles, Rectangle_O_Reaction, txt_O]
            for thisComponent in OComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            OClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "O"-------
            while continueRoutine:
                # get current time
                t = OClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=OClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Rectangles* updates
                if Rectangles.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Rectangles.frameNStart = frameN  # exact frame index
                    Rectangles.tStart = t  # local t and not account for scr refresh
                    Rectangles.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Rectangles, 'tStartRefresh')  # time at next scr refresh
                    Rectangles.setAutoDraw(True)
                if Rectangles.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Rectangles.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        Rectangles.tStop = t  # not accounting for scr refresh
                        Rectangles.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Rectangles, 'tStopRefresh')  # time at next scr refresh
                        Rectangles.setAutoDraw(False)
                
                # *Rectangle_O_Reaction* updates
                if Rectangle_O_Reaction.status == NOT_STARTED and tThisFlip >= rt_other-frameTolerance:
                    # keep track of start time/frame for later
                    Rectangle_O_Reaction.frameNStart = frameN  # exact frame index
                    Rectangle_O_Reaction.tStart = t  # local t and not account for scr refresh
                    Rectangle_O_Reaction.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Rectangle_O_Reaction, 'tStartRefresh')  # time at next scr refresh
                    Rectangle_O_Reaction.setAutoDraw(True)
                if Rectangle_O_Reaction.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Rectangle_O_Reaction.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        Rectangle_O_Reaction.tStop = t  # not accounting for scr refresh
                        Rectangle_O_Reaction.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Rectangle_O_Reaction, 'tStopRefresh')  # time at next scr refresh
                        Rectangle_O_Reaction.setAutoDraw(False)
                
                # *txt_O* updates
                if txt_O.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    txt_O.frameNStart = frameN  # exact frame index
                    txt_O.tStart = t  # local t and not account for scr refresh
                    txt_O.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(txt_O, 'tStartRefresh')  # time at next scr refresh
                    txt_O.setAutoDraw(True)
                if txt_O.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > txt_O.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        txt_O.tStop = t  # not accounting for scr refresh
                        txt_O.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(txt_O, 'tStopRefresh')  # time at next scr refresh
                        txt_O.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in OComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "O"-------
            for thisComponent in OComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            Trials_O_5.addData('Rectangles.started', Rectangles.tStartRefresh)
            Trials_O_5.addData('Rectangles.stopped', Rectangles.tStopRefresh)
            Trials_O_5.addData('Rectangle_O_Reaction.started', Rectangle_O_Reaction.tStartRefresh)
            Trials_O_5.addData('Rectangle_O_Reaction.stopped', Rectangle_O_Reaction.tStopRefresh)
            Trials_O_5.addData('txt_O.started', txt_O.tStartRefresh)
            Trials_O_5.addData('txt_O.stopped', txt_O.tStopRefresh)
            # the Routine "O" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'Trials_O_5'
        
        # get names of stimulus parameters
        if Trials_O_5.trialList in ([], [None], None):
            params = []
        else:
            params = Trials_O_5.trialList[0].keys()
        # save data for this loop
        Trials_O_5.saveAsExcel(filename + '.xlsx', sheetName='Trials_O_5',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        Trials_O_5.saveAsText(filename + 'Trials_O_5.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # ------Prepare to start Routine "RSI"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        RSI_txt.setText('+')
        # keep track of which components have finished
        RSIComponents = [RSI_txt]
        for thisComponent in RSIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        RSIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "RSI"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = RSIClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=RSIClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *RSI_txt* updates
            if RSI_txt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                RSI_txt.frameNStart = frameN  # exact frame index
                RSI_txt.tStart = t  # local t and not account for scr refresh
                RSI_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RSI_txt, 'tStartRefresh')  # time at next scr refresh
                RSI_txt.setAutoDraw(True)
            if RSI_txt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > RSI_txt.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    RSI_txt.tStop = t  # not accounting for scr refresh
                    RSI_txt.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(RSI_txt, 'tStopRefresh')  # time at next scr refresh
                    RSI_txt.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in RSIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "RSI"-------
        for thisComponent in RSIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        POP.addData('RSI_txt.started', RSI_txt.tStartRefresh)
        POP.addData('RSI_txt.stopped', RSI_txt.tStopRefresh)
        
        # set up handler to look after randomisation of conditions etc
        Trials_P_6 = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('var_excel.xlsx', selection=random(1)*20),
            seed=None, name='Trials_P_6')
        thisExp.addLoop(Trials_P_6)  # add the loop to the experiment
        thisTrials_P_6 = Trials_P_6.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_P_6.rgb)
        if thisTrials_P_6 != None:
            for paramName in thisTrials_P_6:
                exec('{} = thisTrials_P_6[paramName]'.format(paramName))
        
        for thisTrials_P_6 in Trials_P_6:
            currentLoop = Trials_P_6
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_P_6.rgb)
            if thisTrials_P_6 != None:
                for paramName in thisTrials_P_6:
                    exec('{} = thisTrials_P_6[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "P"-------
            continueRoutine = True
            routineTimer.add(2.000000)
            # update component parameters for each repeat
            Key_resp_P.keys = []
            Key_resp_P.rt = []
            _Key_resp_P_allKeys = []
            txt_P.setText(stimulus)
            # keep track of which components have finished
            PComponents = [Rectangles_2, Key_resp_P, txt_P]
            for thisComponent in PComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            PClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "P"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = PClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=PClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Rectangles_2* updates
                if Rectangles_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Rectangles_2.frameNStart = frameN  # exact frame index
                    Rectangles_2.tStart = t  # local t and not account for scr refresh
                    Rectangles_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Rectangles_2, 'tStartRefresh')  # time at next scr refresh
                    Rectangles_2.setAutoDraw(True)
                if Rectangles_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Rectangles_2.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        Rectangles_2.tStop = t  # not accounting for scr refresh
                        Rectangles_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Rectangles_2, 'tStopRefresh')  # time at next scr refresh
                        Rectangles_2.setAutoDraw(False)
                
                # *Key_resp_P* updates
                waitOnFlip = False
                if Key_resp_P.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Key_resp_P.frameNStart = frameN  # exact frame index
                    Key_resp_P.tStart = t  # local t and not account for scr refresh
                    Key_resp_P.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Key_resp_P, 'tStartRefresh')  # time at next scr refresh
                    Key_resp_P.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(Key_resp_P.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(Key_resp_P.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if Key_resp_P.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Key_resp_P.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        Key_resp_P.tStop = t  # not accounting for scr refresh
                        Key_resp_P.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Key_resp_P, 'tStopRefresh')  # time at next scr refresh
                        Key_resp_P.status = FINISHED
                if Key_resp_P.status == STARTED and not waitOnFlip:
                    theseKeys = Key_resp_P.getKeys(keyList=['f', 'j'], waitRelease=False)
                    _Key_resp_P_allKeys.extend(theseKeys)
                    if len(_Key_resp_P_allKeys):
                        Key_resp_P.keys = _Key_resp_P_allKeys[-1].name  # just the last key pressed
                        Key_resp_P.rt = _Key_resp_P_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *txt_P* updates
                if txt_P.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    txt_P.frameNStart = frameN  # exact frame index
                    txt_P.tStart = t  # local t and not account for scr refresh
                    txt_P.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(txt_P, 'tStartRefresh')  # time at next scr refresh
                    txt_P.setAutoDraw(True)
                if txt_P.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > txt_P.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        txt_P.tStop = t  # not accounting for scr refresh
                        txt_P.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(txt_P, 'tStopRefresh')  # time at next scr refresh
                        txt_P.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in PComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "P"-------
            for thisComponent in PComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            Trials_P_6.addData('Rectangles_2.started', Rectangles_2.tStartRefresh)
            Trials_P_6.addData('Rectangles_2.stopped', Rectangles_2.tStopRefresh)
            # check responses
            if Key_resp_P.keys in ['', [], None]:  # No response was made
                Key_resp_P.keys = None
            Trials_P_6.addData('Key_resp_P.keys',Key_resp_P.keys)
            if Key_resp_P.keys != None:  # we had a response
                Trials_P_6.addData('Key_resp_P.rt', Key_resp_P.rt)
            Trials_P_6.addData('Key_resp_P.started', Key_resp_P.tStartRefresh)
            Trials_P_6.addData('Key_resp_P.stopped', Key_resp_P.tStopRefresh)
            Trials_P_6.addData('txt_P.started', txt_P.tStartRefresh)
            Trials_P_6.addData('txt_P.stopped', txt_P.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'Trials_P_6'
        
        # get names of stimulus parameters
        if Trials_P_6.trialList in ([], [None], None):
            params = []
        else:
            params = Trials_P_6.trialList[0].keys()
        # save data for this loop
        Trials_P_6.saveAsExcel(filename + '.xlsx', sheetName='Trials_P_6',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        Trials_P_6.saveAsText(filename + 'Trials_P_6.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        thisExp.nextEntry()
        
    # completed 1 repeats of 'POP'
    
    # get names of stimulus parameters
    if POP.trialList in ([], [None], None):
        params = []
    else:
        params = POP.trialList[0].keys()
    # save data for this loop
    POP.saveAsExcel(filename + '.xlsx', sheetName='POP',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    POP.saveAsText(filename + 'POP.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "Error_estimation"-------
    continueRoutine = True
    # update component parameters for each repeat
    error_est_key.keys = []
    error_est_key.rt = []
    _error_est_key_allKeys = []
    # keep track of which components have finished
    Error_estimationComponents = [error_est_txt, error_est_key]
    for thisComponent in Error_estimationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Error_estimationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Error_estimation"-------
    while continueRoutine:
        # get current time
        t = Error_estimationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Error_estimationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *error_est_txt* updates
        if error_est_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            error_est_txt.frameNStart = frameN  # exact frame index
            error_est_txt.tStart = t  # local t and not account for scr refresh
            error_est_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(error_est_txt, 'tStartRefresh')  # time at next scr refresh
            error_est_txt.setAutoDraw(True)
        
        # *error_est_key* updates
        waitOnFlip = False
        if error_est_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            error_est_key.frameNStart = frameN  # exact frame index
            error_est_key.tStart = t  # local t and not account for scr refresh
            error_est_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(error_est_key, 'tStartRefresh')  # time at next scr refresh
            error_est_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(error_est_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(error_est_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if error_est_key.status == STARTED and not waitOnFlip:
            theseKeys = error_est_key.getKeys(keyList=['a', 'z'], waitRelease=False)
            _error_est_key_allKeys.extend(theseKeys)
            if len(_error_est_key_allKeys):
                error_est_key.keys = _error_est_key_allKeys[-1].name  # just the last key pressed
                error_est_key.rt = _error_est_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Error_estimationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Error_estimation"-------
    for thisComponent in Error_estimationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Block.addData('error_est_txt.started', error_est_txt.tStartRefresh)
    Block.addData('error_est_txt.stopped', error_est_txt.tStopRefresh)
    # check responses
    if error_est_key.keys in ['', [], None]:  # No response was made
        error_est_key.keys = None
    Block.addData('error_est_key.keys',error_est_key.keys)
    if error_est_key.keys != None:  # we had a response
        Block.addData('error_est_key.rt', error_est_key.rt)
    Block.addData('error_est_key.started', error_est_key.tStartRefresh)
    Block.addData('error_est_key.stopped', error_est_key.tStopRefresh)
    # the Routine "Error_estimation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 10 repeats of 'Block'

# get names of stimulus parameters
if Block.trialList in ([], [None], None):
    params = []
else:
    params = Block.trialList[0].keys()
# save data for this loop
Block.saveAsExcel(filename + '.xlsx', sheetName='Block',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
Block.saveAsText(filename + 'Block.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Goodbye"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
GoodbyeComponents = []
for thisComponent in GoodbyeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
GoodbyeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Goodbye"-------
while continueRoutine:
    # get current time
    t = GoodbyeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=GoodbyeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GoodbyeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Goodbye"-------
for thisComponent in GoodbyeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Goodbye" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
