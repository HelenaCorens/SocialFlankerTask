/******************************** 
 * Test2_Clean_Rpep_Helena Test *
 ********************************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'Test2_CLEAN_rpep_Helena';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(WelcomeRoutineBegin());
flowScheduler.add(WelcomeRoutineEachFrame());
flowScheduler.add(WelcomeRoutineEnd());
flowScheduler.add(General_InstructionRoutineBegin());
flowScheduler.add(General_InstructionRoutineEachFrame());
flowScheduler.add(General_InstructionRoutineEnd());
flowScheduler.add(PracticeRoutineBegin());
flowScheduler.add(PracticeRoutineEachFrame());
flowScheduler.add(PracticeRoutineEnd());
const BlockLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(BlockLoopBegin, BlockLoopScheduler);
flowScheduler.add(BlockLoopScheduler);
flowScheduler.add(BlockLoopEnd);
flowScheduler.add(GoodbyeRoutineBegin());
flowScheduler.add(GoodbyeRoutineEachFrame());
flowScheduler.add(GoodbyeRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.DEBUG);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.1.2';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls('completedURL', 'incompleteURL');

  return Scheduler.Event.NEXT;
}


var WelcomeClock;
var welcome_txt;
var welcome_key;
var General_InstructionClock;
var general_instruct_txt;
var general_instruct_key;
var PracticeClock;
var OPP_instructClock;
var sequence_instruct_txt;
var seq_instruct_key;
var OClock;
var Rectangles;
var Rectangle_O_Reaction;
var txt_O;
var RSIClock;
var RSI_txt;
var PClock;
var Rectangles_2;
var Key_resp_P;
var txt_P;
var Error_estimationClock;
var error_est_txt;
var error_est_key;
var POP_instructClock;
var pop_instruct_txt;
var pop_instruct_key;
var GoodbyeClock;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "Welcome"
  WelcomeClock = new util.Clock();
  welcome_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcome_txt',
    text: 'Hello and welcome.\n\nYou are taking part in a task interaction experiment with another participant. You will both do the same task which will be given in a sequence of 3 trials.\nBefore the task, instructions will be given to either respond yourself or to observe how the other particpant responded. \n\nThe goal is to keep track of the errors of the other participant. After every 3 trials, you have to point out if the other participant made a mistake or not.\n\nSince this is an online experiment, you will be interacting with a previous participant. This means that you will interact with the other person by his/hers stored data. \n\nPress the spacebar to go continue.\n',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.064,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  welcome_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "General_Instruction"
  General_InstructionClock = new util.Clock();
  general_instruct_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'general_instruct_txt',
    text: 'You will see a row of five arrowheads next to eachother like this: \n<<<<< \n\nFocus on the arrowhead in the middle:\n- PRESS ‘ f ‘ on the keyboard when middle arrowhead is pointed to the LEFT\n\n- PRESS ‘ j ‘ on the keyboard when middle arrowhead is pointed to the RIGHT\n\nThe arrowheads around the middle one can have another direction like this: \n<<><<\n\nOnly respond to the direction of the arrowhead in the middle \n(in this case: right —>  press ‘j’).  Ignore the arrowheads around it. \n\nAnswer as fast as possible!\nIf you understand these instructions, press the spacebar to continue. \n',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.064,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  general_instruct_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Practice"
  PracticeClock = new util.Clock();
  // Initialize components for Routine "OPP_instruct"
  OPP_instructClock = new util.Clock();
  sequence_instruct_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'sequence_instruct_txt',
    text: 'OBSERVE\nPERFORM\nPERFORM\n\npress space bar\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  seq_instruct_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "O"
  OClock = new util.Clock();
  Rectangles = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Rectangles', units : undefined, 
    image : 'rectsocial/rect_neutral.jpg', mask : undefined,
    ori : 0, pos : [0, 0], size : [2, 2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  Rectangle_O_Reaction = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Rectangle_O_Reaction', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [2, 2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  txt_O = new visual.TextStim({
    win: psychoJS.window,
    name: 'txt_O',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "RSI"
  RSIClock = new util.Clock();
  RSI_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'RSI_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "P"
  PClock = new util.Clock();
  Rectangles_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Rectangles_2', units : undefined, 
    image : 'rectsocial/rect_neutral.jpg', mask : undefined,
    ori : 0, pos : [0, 0], size : [2, 2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  Key_resp_P = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  txt_P = new visual.TextStim({
    win: psychoJS.window,
    name: 'txt_P',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "RSI"
  RSIClock = new util.Clock();
  RSI_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'RSI_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "P"
  PClock = new util.Clock();
  Rectangles_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Rectangles_2', units : undefined, 
    image : 'rectsocial/rect_neutral.jpg', mask : undefined,
    ori : 0, pos : [0, 0], size : [2, 2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  Key_resp_P = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  txt_P = new visual.TextStim({
    win: psychoJS.window,
    name: 'txt_P',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "Error_estimation"
  Error_estimationClock = new util.Clock();
  error_est_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'error_est_txt',
    text: '\nHow many errors did the other participant make?\n\n0 = press ‘a’ on keyboard\n1 = press ‘p’ on keyboard\n\n\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  error_est_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "POP_instruct"
  POP_instructClock = new util.Clock();
  pop_instruct_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'pop_instruct_txt',
    text: 'PERFORM \nOBSERVE\nPERFORM\n\npress space bar when ready\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  pop_instruct_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "P"
  PClock = new util.Clock();
  Rectangles_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Rectangles_2', units : undefined, 
    image : 'rectsocial/rect_neutral.jpg', mask : undefined,
    ori : 0, pos : [0, 0], size : [2, 2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  Key_resp_P = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  txt_P = new visual.TextStim({
    win: psychoJS.window,
    name: 'txt_P',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "RSI"
  RSIClock = new util.Clock();
  RSI_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'RSI_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "O"
  OClock = new util.Clock();
  Rectangles = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Rectangles', units : undefined, 
    image : 'rectsocial/rect_neutral.jpg', mask : undefined,
    ori : 0, pos : [0, 0], size : [2, 2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  Rectangle_O_Reaction = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Rectangle_O_Reaction', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [2, 2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  txt_O = new visual.TextStim({
    win: psychoJS.window,
    name: 'txt_O',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "RSI"
  RSIClock = new util.Clock();
  RSI_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'RSI_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "P"
  PClock = new util.Clock();
  Rectangles_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Rectangles_2', units : undefined, 
    image : 'rectsocial/rect_neutral.jpg', mask : undefined,
    ori : 0, pos : [0, 0], size : [2, 2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  Key_resp_P = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  txt_P = new visual.TextStim({
    win: psychoJS.window,
    name: 'txt_P',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "Error_estimation"
  Error_estimationClock = new util.Clock();
  error_est_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'error_est_txt',
    text: '\nHow many errors did the other participant make?\n\n0 = press ‘a’ on keyboard\n1 = press ‘p’ on keyboard\n\n\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  error_est_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Goodbye"
  GoodbyeClock = new util.Clock();
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _welcome_key_allKeys;
var WelcomeComponents;
function WelcomeRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Welcome'-------
    t = 0;
    WelcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    welcome_key.keys = undefined;
    welcome_key.rt = undefined;
    _welcome_key_allKeys = [];
    // keep track of which components have finished
    WelcomeComponents = [];
    WelcomeComponents.push(welcome_txt);
    WelcomeComponents.push(welcome_key);
    
    WelcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function WelcomeRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Welcome'-------
    // get current time
    t = WelcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *welcome_txt* updates
    if (t >= 0.0 && welcome_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome_txt.tStart = t;  // (not accounting for frame time here)
      welcome_txt.frameNStart = frameN;  // exact frame index
      
      welcome_txt.setAutoDraw(true);
    }

    
    // *welcome_key* updates
    if (t >= 0.0 && welcome_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome_key.tStart = t;  // (not accounting for frame time here)
      welcome_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { welcome_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { welcome_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { welcome_key.clearEvents(); });
    }

    if (welcome_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = welcome_key.getKeys({keyList: ['space'], waitRelease: false});
      _welcome_key_allKeys = _welcome_key_allKeys.concat(theseKeys);
      if (_welcome_key_allKeys.length > 0) {
        welcome_key.keys = _welcome_key_allKeys[_welcome_key_allKeys.length - 1].name;  // just the last key pressed
        welcome_key.rt = _welcome_key_allKeys[_welcome_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    WelcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function WelcomeRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Welcome'-------
    WelcomeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('welcome_key.keys', welcome_key.keys);
    if (typeof welcome_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('welcome_key.rt', welcome_key.rt);
        routineTimer.reset();
        }
    
    welcome_key.stop();
    // the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _general_instruct_key_allKeys;
var General_InstructionComponents;
function General_InstructionRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'General_Instruction'-------
    t = 0;
    General_InstructionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    general_instruct_key.keys = undefined;
    general_instruct_key.rt = undefined;
    _general_instruct_key_allKeys = [];
    // keep track of which components have finished
    General_InstructionComponents = [];
    General_InstructionComponents.push(general_instruct_txt);
    General_InstructionComponents.push(general_instruct_key);
    
    General_InstructionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function General_InstructionRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'General_Instruction'-------
    // get current time
    t = General_InstructionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *general_instruct_txt* updates
    if (t >= 0.0 && general_instruct_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      general_instruct_txt.tStart = t;  // (not accounting for frame time here)
      general_instruct_txt.frameNStart = frameN;  // exact frame index
      
      general_instruct_txt.setAutoDraw(true);
    }

    
    // *general_instruct_key* updates
    if (t >= 0.0 && general_instruct_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      general_instruct_key.tStart = t;  // (not accounting for frame time here)
      general_instruct_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { general_instruct_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { general_instruct_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { general_instruct_key.clearEvents(); });
    }

    if (general_instruct_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = general_instruct_key.getKeys({keyList: ['space'], waitRelease: false});
      _general_instruct_key_allKeys = _general_instruct_key_allKeys.concat(theseKeys);
      if (_general_instruct_key_allKeys.length > 0) {
        general_instruct_key.keys = _general_instruct_key_allKeys[_general_instruct_key_allKeys.length - 1].name;  // just the last key pressed
        general_instruct_key.rt = _general_instruct_key_allKeys[_general_instruct_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    General_InstructionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function General_InstructionRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'General_Instruction'-------
    General_InstructionComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('general_instruct_key.keys', general_instruct_key.keys);
    if (typeof general_instruct_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('general_instruct_key.rt', general_instruct_key.rt);
        routineTimer.reset();
        }
    
    general_instruct_key.stop();
    // the Routine "General_Instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var PracticeComponents;
function PracticeRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Practice'-------
    t = 0;
    PracticeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    PracticeComponents = [];
    
    PracticeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function PracticeRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Practice'-------
    // get current time
    t = PracticeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    PracticeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PracticeRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Practice'-------
    PracticeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "Practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var Block;
var currentLoop;
function BlockLoopBegin(BlockLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  Block = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 10, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'Block'
  });
  psychoJS.experiment.addLoop(Block); // add the loop to the experiment
  currentLoop = Block;  // we're now the current loop

  // Schedule all the trials in the trialList:
  Block.forEach(function() {
    const snapshot = Block.getSnapshot();

    BlockLoopScheduler.add(importConditions(snapshot));
    BlockLoopScheduler.add(OPP_instructRoutineBegin(snapshot));
    BlockLoopScheduler.add(OPP_instructRoutineEachFrame(snapshot));
    BlockLoopScheduler.add(OPP_instructRoutineEnd(snapshot));
    const OPPLoopScheduler = new Scheduler(psychoJS);
    BlockLoopScheduler.add(OPPLoopBegin, OPPLoopScheduler);
    BlockLoopScheduler.add(OPPLoopScheduler);
    BlockLoopScheduler.add(OPPLoopEnd);
    BlockLoopScheduler.add(Error_estimationRoutineBegin(snapshot));
    BlockLoopScheduler.add(Error_estimationRoutineEachFrame(snapshot));
    BlockLoopScheduler.add(Error_estimationRoutineEnd(snapshot));
    BlockLoopScheduler.add(POP_instructRoutineBegin(snapshot));
    BlockLoopScheduler.add(POP_instructRoutineEachFrame(snapshot));
    BlockLoopScheduler.add(POP_instructRoutineEnd(snapshot));
    const POPLoopScheduler = new Scheduler(psychoJS);
    BlockLoopScheduler.add(POPLoopBegin, POPLoopScheduler);
    BlockLoopScheduler.add(POPLoopScheduler);
    BlockLoopScheduler.add(POPLoopEnd);
    BlockLoopScheduler.add(Error_estimationRoutineBegin(snapshot));
    BlockLoopScheduler.add(Error_estimationRoutineEachFrame(snapshot));
    BlockLoopScheduler.add(Error_estimationRoutineEnd(snapshot));
    BlockLoopScheduler.add(endLoopIteration(BlockLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var OPP;
function OPPLoopBegin(OPPLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  OPP = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'OPP'
  });
  psychoJS.experiment.addLoop(OPP); // add the loop to the experiment
  currentLoop = OPP;  // we're now the current loop

  // Schedule all the trials in the trialList:
  OPP.forEach(function() {
    const snapshot = OPP.getSnapshot();

    OPPLoopScheduler.add(importConditions(snapshot));
    const Trials_O1LoopScheduler = new Scheduler(psychoJS);
    OPPLoopScheduler.add(Trials_O1LoopBegin, Trials_O1LoopScheduler);
    OPPLoopScheduler.add(Trials_O1LoopScheduler);
    OPPLoopScheduler.add(Trials_O1LoopEnd);
    OPPLoopScheduler.add(RSIRoutineBegin(snapshot));
    OPPLoopScheduler.add(RSIRoutineEachFrame(snapshot));
    OPPLoopScheduler.add(RSIRoutineEnd(snapshot));
    const Trials_P_2LoopScheduler = new Scheduler(psychoJS);
    OPPLoopScheduler.add(Trials_P_2LoopBegin, Trials_P_2LoopScheduler);
    OPPLoopScheduler.add(Trials_P_2LoopScheduler);
    OPPLoopScheduler.add(Trials_P_2LoopEnd);
    OPPLoopScheduler.add(RSIRoutineBegin(snapshot));
    OPPLoopScheduler.add(RSIRoutineEachFrame(snapshot));
    OPPLoopScheduler.add(RSIRoutineEnd(snapshot));
    const Trials_P_3LoopScheduler = new Scheduler(psychoJS);
    OPPLoopScheduler.add(Trials_P_3LoopBegin, Trials_P_3LoopScheduler);
    OPPLoopScheduler.add(Trials_P_3LoopScheduler);
    OPPLoopScheduler.add(Trials_P_3LoopEnd);
    OPPLoopScheduler.add(endLoopIteration(OPPLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var Trials_O1;
function Trials_O1LoopBegin(Trials_O1LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  Trials_O1 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'var_excel.xlsx', (Math.random(1) * 20)),
    seed: undefined, name: 'Trials_O1'
  });
  psychoJS.experiment.addLoop(Trials_O1); // add the loop to the experiment
  currentLoop = Trials_O1;  // we're now the current loop

  // Schedule all the trials in the trialList:
  Trials_O1.forEach(function() {
    const snapshot = Trials_O1.getSnapshot();

    Trials_O1LoopScheduler.add(importConditions(snapshot));
    Trials_O1LoopScheduler.add(ORoutineBegin(snapshot));
    Trials_O1LoopScheduler.add(ORoutineEachFrame(snapshot));
    Trials_O1LoopScheduler.add(ORoutineEnd(snapshot));
    Trials_O1LoopScheduler.add(endLoopIteration(Trials_O1LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function Trials_O1LoopEnd() {
  psychoJS.experiment.removeLoop(Trials_O1);

  return Scheduler.Event.NEXT;
}


var Trials_P_2;
function Trials_P_2LoopBegin(Trials_P_2LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  Trials_P_2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'var_excel.xlsx', (Math.random(1) * 20)),
    seed: undefined, name: 'Trials_P_2'
  });
  psychoJS.experiment.addLoop(Trials_P_2); // add the loop to the experiment
  currentLoop = Trials_P_2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  Trials_P_2.forEach(function() {
    const snapshot = Trials_P_2.getSnapshot();

    Trials_P_2LoopScheduler.add(importConditions(snapshot));
    Trials_P_2LoopScheduler.add(PRoutineBegin(snapshot));
    Trials_P_2LoopScheduler.add(PRoutineEachFrame(snapshot));
    Trials_P_2LoopScheduler.add(PRoutineEnd(snapshot));
    Trials_P_2LoopScheduler.add(endLoopIteration(Trials_P_2LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function Trials_P_2LoopEnd() {
  psychoJS.experiment.removeLoop(Trials_P_2);

  return Scheduler.Event.NEXT;
}


var Trials_P_3;
function Trials_P_3LoopBegin(Trials_P_3LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  Trials_P_3 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'var_excel.xlsx', (Math.random(1) * 20)),
    seed: undefined, name: 'Trials_P_3'
  });
  psychoJS.experiment.addLoop(Trials_P_3); // add the loop to the experiment
  currentLoop = Trials_P_3;  // we're now the current loop

  // Schedule all the trials in the trialList:
  Trials_P_3.forEach(function() {
    const snapshot = Trials_P_3.getSnapshot();

    Trials_P_3LoopScheduler.add(importConditions(snapshot));
    Trials_P_3LoopScheduler.add(PRoutineBegin(snapshot));
    Trials_P_3LoopScheduler.add(PRoutineEachFrame(snapshot));
    Trials_P_3LoopScheduler.add(PRoutineEnd(snapshot));
    Trials_P_3LoopScheduler.add(endLoopIteration(Trials_P_3LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function Trials_P_3LoopEnd() {
  psychoJS.experiment.removeLoop(Trials_P_3);

  return Scheduler.Event.NEXT;
}


function OPPLoopEnd() {
  psychoJS.experiment.removeLoop(OPP);

  return Scheduler.Event.NEXT;
}


var POP;
function POPLoopBegin(POPLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  POP = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'POP'
  });
  psychoJS.experiment.addLoop(POP); // add the loop to the experiment
  currentLoop = POP;  // we're now the current loop

  // Schedule all the trials in the trialList:
  POP.forEach(function() {
    const snapshot = POP.getSnapshot();

    POPLoopScheduler.add(importConditions(snapshot));
    const Trials_P_4LoopScheduler = new Scheduler(psychoJS);
    POPLoopScheduler.add(Trials_P_4LoopBegin, Trials_P_4LoopScheduler);
    POPLoopScheduler.add(Trials_P_4LoopScheduler);
    POPLoopScheduler.add(Trials_P_4LoopEnd);
    POPLoopScheduler.add(RSIRoutineBegin(snapshot));
    POPLoopScheduler.add(RSIRoutineEachFrame(snapshot));
    POPLoopScheduler.add(RSIRoutineEnd(snapshot));
    const Trials_O_5LoopScheduler = new Scheduler(psychoJS);
    POPLoopScheduler.add(Trials_O_5LoopBegin, Trials_O_5LoopScheduler);
    POPLoopScheduler.add(Trials_O_5LoopScheduler);
    POPLoopScheduler.add(Trials_O_5LoopEnd);
    POPLoopScheduler.add(RSIRoutineBegin(snapshot));
    POPLoopScheduler.add(RSIRoutineEachFrame(snapshot));
    POPLoopScheduler.add(RSIRoutineEnd(snapshot));
    const Trials_P_6LoopScheduler = new Scheduler(psychoJS);
    POPLoopScheduler.add(Trials_P_6LoopBegin, Trials_P_6LoopScheduler);
    POPLoopScheduler.add(Trials_P_6LoopScheduler);
    POPLoopScheduler.add(Trials_P_6LoopEnd);
    POPLoopScheduler.add(endLoopIteration(POPLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var Trials_P_4;
function Trials_P_4LoopBegin(Trials_P_4LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  Trials_P_4 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'var_excel.xlsx', (Math.random(1) * 20)),
    seed: undefined, name: 'Trials_P_4'
  });
  psychoJS.experiment.addLoop(Trials_P_4); // add the loop to the experiment
  currentLoop = Trials_P_4;  // we're now the current loop

  // Schedule all the trials in the trialList:
  Trials_P_4.forEach(function() {
    const snapshot = Trials_P_4.getSnapshot();

    Trials_P_4LoopScheduler.add(importConditions(snapshot));
    Trials_P_4LoopScheduler.add(PRoutineBegin(snapshot));
    Trials_P_4LoopScheduler.add(PRoutineEachFrame(snapshot));
    Trials_P_4LoopScheduler.add(PRoutineEnd(snapshot));
    Trials_P_4LoopScheduler.add(endLoopIteration(Trials_P_4LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function Trials_P_4LoopEnd() {
  psychoJS.experiment.removeLoop(Trials_P_4);

  return Scheduler.Event.NEXT;
}


var Trials_O_5;
function Trials_O_5LoopBegin(Trials_O_5LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  Trials_O_5 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'var_excel.xlsx', (Math.random(1) * 20)),
    seed: undefined, name: 'Trials_O_5'
  });
  psychoJS.experiment.addLoop(Trials_O_5); // add the loop to the experiment
  currentLoop = Trials_O_5;  // we're now the current loop

  // Schedule all the trials in the trialList:
  Trials_O_5.forEach(function() {
    const snapshot = Trials_O_5.getSnapshot();

    Trials_O_5LoopScheduler.add(importConditions(snapshot));
    Trials_O_5LoopScheduler.add(ORoutineBegin(snapshot));
    Trials_O_5LoopScheduler.add(ORoutineEachFrame(snapshot));
    Trials_O_5LoopScheduler.add(ORoutineEnd(snapshot));
    Trials_O_5LoopScheduler.add(endLoopIteration(Trials_O_5LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function Trials_O_5LoopEnd() {
  psychoJS.experiment.removeLoop(Trials_O_5);

  return Scheduler.Event.NEXT;
}


var Trials_P_6;
function Trials_P_6LoopBegin(Trials_P_6LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  Trials_P_6 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'var_excel.xlsx', (Math.random(1) * 20)),
    seed: undefined, name: 'Trials_P_6'
  });
  psychoJS.experiment.addLoop(Trials_P_6); // add the loop to the experiment
  currentLoop = Trials_P_6;  // we're now the current loop

  // Schedule all the trials in the trialList:
  Trials_P_6.forEach(function() {
    const snapshot = Trials_P_6.getSnapshot();

    Trials_P_6LoopScheduler.add(importConditions(snapshot));
    Trials_P_6LoopScheduler.add(PRoutineBegin(snapshot));
    Trials_P_6LoopScheduler.add(PRoutineEachFrame(snapshot));
    Trials_P_6LoopScheduler.add(PRoutineEnd(snapshot));
    Trials_P_6LoopScheduler.add(endLoopIteration(Trials_P_6LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function Trials_P_6LoopEnd() {
  psychoJS.experiment.removeLoop(Trials_P_6);

  return Scheduler.Event.NEXT;
}


function POPLoopEnd() {
  psychoJS.experiment.removeLoop(POP);

  return Scheduler.Event.NEXT;
}


function BlockLoopEnd() {
  psychoJS.experiment.removeLoop(Block);

  return Scheduler.Event.NEXT;
}


var _seq_instruct_key_allKeys;
var OPP_instructComponents;
function OPP_instructRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'OPP_instruct'-------
    t = 0;
    OPP_instructClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    seq_instruct_key.keys = undefined;
    seq_instruct_key.rt = undefined;
    _seq_instruct_key_allKeys = [];
    // keep track of which components have finished
    OPP_instructComponents = [];
    OPP_instructComponents.push(sequence_instruct_txt);
    OPP_instructComponents.push(seq_instruct_key);
    
    OPP_instructComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function OPP_instructRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'OPP_instruct'-------
    // get current time
    t = OPP_instructClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *sequence_instruct_txt* updates
    if (t >= 0.0 && sequence_instruct_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sequence_instruct_txt.tStart = t;  // (not accounting for frame time here)
      sequence_instruct_txt.frameNStart = frameN;  // exact frame index
      
      sequence_instruct_txt.setAutoDraw(true);
    }

    
    // *seq_instruct_key* updates
    if (t >= 0.0 && seq_instruct_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      seq_instruct_key.tStart = t;  // (not accounting for frame time here)
      seq_instruct_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { seq_instruct_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { seq_instruct_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { seq_instruct_key.clearEvents(); });
    }

    if (seq_instruct_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = seq_instruct_key.getKeys({keyList: ['space'], waitRelease: false});
      _seq_instruct_key_allKeys = _seq_instruct_key_allKeys.concat(theseKeys);
      if (_seq_instruct_key_allKeys.length > 0) {
        seq_instruct_key.keys = _seq_instruct_key_allKeys[_seq_instruct_key_allKeys.length - 1].name;  // just the last key pressed
        seq_instruct_key.rt = _seq_instruct_key_allKeys[_seq_instruct_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    OPP_instructComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function OPP_instructRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'OPP_instruct'-------
    OPP_instructComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('seq_instruct_key.keys', seq_instruct_key.keys);
    if (typeof seq_instruct_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('seq_instruct_key.rt', seq_instruct_key.rt);
        routineTimer.reset();
        }
    
    seq_instruct_key.stop();
    // the Routine "OPP_instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var OComponents;
function ORoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'O'-------
    t = 0;
    OClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Rectangle_O_Reaction.setImage(resp_other);
    txt_O.setText(stimulus);
    // keep track of which components have finished
    OComponents = [];
    OComponents.push(Rectangles);
    OComponents.push(Rectangle_O_Reaction);
    OComponents.push(txt_O);
    
    OComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function ORoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'O'-------
    // get current time
    t = OClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Rectangles* updates
    if (t >= 0.0 && Rectangles.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Rectangles.tStart = t;  // (not accounting for frame time here)
      Rectangles.frameNStart = frameN;  // exact frame index
      
      Rectangles.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Rectangles.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Rectangles.setAutoDraw(false);
    }
    
    // *Rectangle_O_Reaction* updates
    if (t >= rt_other && Rectangle_O_Reaction.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Rectangle_O_Reaction.tStart = t;  // (not accounting for frame time here)
      Rectangle_O_Reaction.frameNStart = frameN;  // exact frame index
      
      Rectangle_O_Reaction.setAutoDraw(true);
    }

    frameRemains = rt_other + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Rectangle_O_Reaction.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Rectangle_O_Reaction.setAutoDraw(false);
    }
    
    // *txt_O* updates
    if (t >= 0.0 && txt_O.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      txt_O.tStart = t;  // (not accounting for frame time here)
      txt_O.frameNStart = frameN;  // exact frame index
      
      txt_O.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (txt_O.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      txt_O.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    OComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ORoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'O'-------
    OComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "O" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var RSIComponents;
function RSIRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'RSI'-------
    t = 0;
    RSIClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    RSI_txt.setText('+');
    // keep track of which components have finished
    RSIComponents = [];
    RSIComponents.push(RSI_txt);
    
    RSIComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function RSIRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'RSI'-------
    // get current time
    t = RSIClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *RSI_txt* updates
    if (t >= 0 && RSI_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RSI_txt.tStart = t;  // (not accounting for frame time here)
      RSI_txt.frameNStart = frameN;  // exact frame index
      
      RSI_txt.setAutoDraw(true);
    }

    frameRemains = 0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (RSI_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      RSI_txt.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    RSIComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function RSIRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'RSI'-------
    RSIComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _Key_resp_P_allKeys;
var PComponents;
function PRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'P'-------
    t = 0;
    PClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    Key_resp_P.keys = undefined;
    Key_resp_P.rt = undefined;
    _Key_resp_P_allKeys = [];
    txt_P.setText(stimulus);
    // keep track of which components have finished
    PComponents = [];
    PComponents.push(Rectangles_2);
    PComponents.push(Key_resp_P);
    PComponents.push(txt_P);
    
    PComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function PRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'P'-------
    // get current time
    t = PClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Rectangles_2* updates
    if (t >= 0.0 && Rectangles_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Rectangles_2.tStart = t;  // (not accounting for frame time here)
      Rectangles_2.frameNStart = frameN;  // exact frame index
      
      Rectangles_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Rectangles_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Rectangles_2.setAutoDraw(false);
    }
    
    // *Key_resp_P* updates
    if (t >= 0.0 && Key_resp_P.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Key_resp_P.tStart = t;  // (not accounting for frame time here)
      Key_resp_P.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Key_resp_P.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Key_resp_P.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Key_resp_P.clearEvents(); });
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Key_resp_P.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Key_resp_P.status = PsychoJS.Status.FINISHED;
  }

    if (Key_resp_P.status === PsychoJS.Status.STARTED) {
      let theseKeys = Key_resp_P.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _Key_resp_P_allKeys = _Key_resp_P_allKeys.concat(theseKeys);
      if (_Key_resp_P_allKeys.length > 0) {
        Key_resp_P.keys = _Key_resp_P_allKeys[_Key_resp_P_allKeys.length - 1].name;  // just the last key pressed
        Key_resp_P.rt = _Key_resp_P_allKeys[_Key_resp_P_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *txt_P* updates
    if (t >= 0.0 && txt_P.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      txt_P.tStart = t;  // (not accounting for frame time here)
      txt_P.frameNStart = frameN;  // exact frame index
      
      txt_P.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (txt_P.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      txt_P.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    PComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'P'-------
    PComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Key_resp_P.keys', Key_resp_P.keys);
    if (typeof Key_resp_P.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Key_resp_P.rt', Key_resp_P.rt);
        routineTimer.reset();
        }
    
    Key_resp_P.stop();
    return Scheduler.Event.NEXT;
  };
}


var _error_est_key_allKeys;
var Error_estimationComponents;
function Error_estimationRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Error_estimation'-------
    t = 0;
    Error_estimationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    error_est_key.keys = undefined;
    error_est_key.rt = undefined;
    _error_est_key_allKeys = [];
    // keep track of which components have finished
    Error_estimationComponents = [];
    Error_estimationComponents.push(error_est_txt);
    Error_estimationComponents.push(error_est_key);
    
    Error_estimationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Error_estimationRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Error_estimation'-------
    // get current time
    t = Error_estimationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *error_est_txt* updates
    if (t >= 0.0 && error_est_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      error_est_txt.tStart = t;  // (not accounting for frame time here)
      error_est_txt.frameNStart = frameN;  // exact frame index
      
      error_est_txt.setAutoDraw(true);
    }

    
    // *error_est_key* updates
    if (t >= 0.0 && error_est_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      error_est_key.tStart = t;  // (not accounting for frame time here)
      error_est_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { error_est_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { error_est_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { error_est_key.clearEvents(); });
    }

    if (error_est_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = error_est_key.getKeys({keyList: ['a', 'z'], waitRelease: false});
      _error_est_key_allKeys = _error_est_key_allKeys.concat(theseKeys);
      if (_error_est_key_allKeys.length > 0) {
        error_est_key.keys = _error_est_key_allKeys[_error_est_key_allKeys.length - 1].name;  // just the last key pressed
        error_est_key.rt = _error_est_key_allKeys[_error_est_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Error_estimationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Error_estimationRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Error_estimation'-------
    Error_estimationComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('error_est_key.keys', error_est_key.keys);
    if (typeof error_est_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('error_est_key.rt', error_est_key.rt);
        routineTimer.reset();
        }
    
    error_est_key.stop();
    // the Routine "Error_estimation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _pop_instruct_key_allKeys;
var POP_instructComponents;
function POP_instructRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'POP_instruct'-------
    t = 0;
    POP_instructClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    pop_instruct_key.keys = undefined;
    pop_instruct_key.rt = undefined;
    _pop_instruct_key_allKeys = [];
    // keep track of which components have finished
    POP_instructComponents = [];
    POP_instructComponents.push(pop_instruct_txt);
    POP_instructComponents.push(pop_instruct_key);
    
    POP_instructComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function POP_instructRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'POP_instruct'-------
    // get current time
    t = POP_instructClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *pop_instruct_txt* updates
    if (t >= 0.0 && pop_instruct_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pop_instruct_txt.tStart = t;  // (not accounting for frame time here)
      pop_instruct_txt.frameNStart = frameN;  // exact frame index
      
      pop_instruct_txt.setAutoDraw(true);
    }

    
    // *pop_instruct_key* updates
    if (t >= 0.0 && pop_instruct_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pop_instruct_key.tStart = t;  // (not accounting for frame time here)
      pop_instruct_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { pop_instruct_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { pop_instruct_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { pop_instruct_key.clearEvents(); });
    }

    if (pop_instruct_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = pop_instruct_key.getKeys({keyList: ['space'], waitRelease: false});
      _pop_instruct_key_allKeys = _pop_instruct_key_allKeys.concat(theseKeys);
      if (_pop_instruct_key_allKeys.length > 0) {
        pop_instruct_key.keys = _pop_instruct_key_allKeys[_pop_instruct_key_allKeys.length - 1].name;  // just the last key pressed
        pop_instruct_key.rt = _pop_instruct_key_allKeys[_pop_instruct_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    POP_instructComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function POP_instructRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'POP_instruct'-------
    POP_instructComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('pop_instruct_key.keys', pop_instruct_key.keys);
    if (typeof pop_instruct_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('pop_instruct_key.rt', pop_instruct_key.rt);
        routineTimer.reset();
        }
    
    pop_instruct_key.stop();
    // the Routine "POP_instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var GoodbyeComponents;
function GoodbyeRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Goodbye'-------
    t = 0;
    GoodbyeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    GoodbyeComponents = [];
    
    GoodbyeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function GoodbyeRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Goodbye'-------
    // get current time
    t = GoodbyeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    GoodbyeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function GoodbyeRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Goodbye'-------
    GoodbyeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "Goodbye" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
