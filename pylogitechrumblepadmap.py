#! /usr/bin/python3

#	PyDS4Map
#	Coded by Nullbyte (Warren Hood)
#	Created:	 11:00PM Fri, 9 May 2019
#	Updated:	 4:12PM Fri, 9 May 2019
import os
import sys
import pyautogui as pg
import win32api
import time
import ctypes
import threading
import pygame
pygame.init()
pygame.joystick.init()
try:
	ds4 = pygame.joystick.Joystick(0)
	ds4.init()
	os.system("cls")
except:
	print("Please insert a controller and open this again...")
	time.sleep(3)
	sys.exit(0)
print(" _______________________________________________________")
print("|                                                       |")
print("|         PyLogitechRumblepadMap Version 1.0.0          |")
print("|                  Coded by Nullbyte                    |")
print("|                                                       |")
print("|_______________________________________________________|")
print()
print("                                           Running now...")
# 1 is pressed or forward or right
# 0 is not pressed or centered
# -1 backward or left



#Key codes
VK_CODE = {'backspace':0x08,
			'lmb':0x01,
           'tab':0x09,
           'clear':0x0C,
           'enter':0x0D,
           'shift':0x10,
           'ctrl':0x11,
           'alt':0x12,
           'pause':0x13,
           'caps_lock':0x14,
           'esc':0x1B,
           'spacebar':0x20,
           'page_up':0x21,
           'page_down':0x22,
           'end':0x23,
           'home':0x24,
           'left_arrow':0x25,
           'up_arrow':0x26,
           'right_arrow':0x27,
           'down_arrow':0x28,
           'select':0x29,
           'print':0x2A,
           'execute':0x2B,
           'print_screen':0x2C,
           'ins':0x2D,
           'del':0x2E,
           'help':0x2F,
           '0':0x30,
           '1':0x31,
           '2':0x32,
           '3':0x33,
           '4':0x34,
           '5':0x35,
           '6':0x36,
           '7':0x37,
           '8':0x38,
           '9':0x39,
           'a':0x41,
           'b':0x42,
           'c':0x43,
           'd':0x44,
           'e':0x45,
           'f':0x46,
           'g':0x47,
           'h':0x48,
           'i':0x49,
           'j':0x4A,
           'k':0x4B,
           'l':0x4C,
           'm':0x4D,
           'n':0x4E,
           'o':0x4F,
           'p':0x50,
           'q':0x51,
           'r':0x52,
           's':0x53,
           't':0x54,
           'u':0x55,
           'v':0x56,
           'w':0x57,
           'x':0x58,
           'y':0x59,
           'z':0x5A,
           'numpad_0':0x60,
           'numpad_1':0x61,
           'numpad_2':0x62,
           'numpad_3':0x63,
           'numpad_4':0x64,
           'numpad_5':0x65,
           'numpad_6':0x66,
           'numpad_7':0x67,
           'numpad_8':0x68,
           'numpad_9':0x69,
           'multiply_key':0x6A,
           'add_key':0x6B,
           'separator_key':0x6C,
           'subtract_key':0x6D,
           'decimal_key':0x6E,
           'divide_key':0x6F,
           'F1':0x70,
           'F2':0x71,
           'F3':0x72,
           'F4':0x73,
           'F5':0x74,
           'F6':0x75,
           'F7':0x76,
           'F8':0x77,
           'F9':0x78,
           'F10':0x79,
           'F11':0x7A,
           'F12':0x7B,
           'F13':0x7C,
           'F14':0x7D,
           'F15':0x7E,
           'F16':0x7F,
           'F17':0x80,
           'F18':0x81,
           'F19':0x82,
           'F20':0x83,
           'F21':0x84,
           'F22':0x85,
           'F23':0x86,
           'F24':0x87,
           'num_lock':0x90,
           'scroll_lock':0x91,
           'left_shift':0xA0,
           'right_shift ':0xA1,
           'left_control':0xA2,
           'right_control':0xA3,
           'left_menu':0xA4,
           'right_menu':0xA5,
           'browser_back':0xA6,
           'browser_forward':0xA7,
           'browser_refresh':0xA8,
           'browser_stop':0xA9,
           'browser_search':0xAA,
           'browser_favorites':0xAB,
           'browser_start_and_home':0xAC,
           'volume_mute':0xAD,
           'volume_Down':0xAE,
           'volume_up':0xAF,
           'next_track':0xB0,
           'previous_track':0xB1,
           'stop_media':0xB2,
           'play/pause_media':0xB3,
           'start_mail':0xB4,
           'select_media':0xB5,
           'start_application_1':0xB6,
           'start_application_2':0xB7,
           'attn_key':0xF6,
           'crsel_key':0xF7,
           'exsel_key':0xF8,
           'play_key':0xFA,
           'zoom_key':0xFB,
           'clear_key':0xFE,
           '+':0xBB,
           ',':0xBC,
           '-':0xBD,
           '.':0xBE,
           '/':0xBF,
           '`':0xC0,
           ';':0xBA,
           '[':0xDB,
           '\\':0xDC,
           ']':0xDD,
           "'":0xDE,
           '`':0xC0}

PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def release(key):
	global VK_CODE
	ReleaseKey(VK_CODE[key])


def hold(key):
	global VK_CODE
	PressKey(VK_CODE[key])


def move(x,y):
	#pg.dragRel(x,y,0.1)
	win32api.mouse_event(0x0001, x, y)
	#time.sleep(0.05)


def is_down(key):
    key_state = win32api.GetKeyState(VK_CODE[key])
    return key_state < 0



def is_double_pressed(key,duration=0.2):
	t1 = time.time()
	#Wait for duration seconds
	while not is_down(key):
		if time.time() - t1 > duration:
			return False
	
	t1 = time.time()
	
	# Key is now down...
	# Wait for it to be released
	
	while is_down(key):
		delta_t = time.time() - t1
		if delta_t > duration:
			return False

	# Now wait for it to be pressed again

	t1 = time.time()
	while not is_down(key):
		delta_t = time.time() - t1
		if delta_t > duration:
			return False

	# Now it has been double pressed
	return True

def drag_slowly(pixels,step):
	for i in range(round(pixels/step)):
		move(step,0)
		time.sleep(0.005)

ds4_data = {
	"x":0,
	"triangle":0,
	"square":0,
	"circle":0,
	"joy_l":{
		"x":0,
		"y":0
	},
	"joy_r":{
		"x":0,
		"y":0
	},
	"dpad_up":0,
	"dpad_left":0,
	"dpad_down":0,
	"dpad_right":0,
	"share":0,
	"options":0,
	"ps":0,
	"r1":0,
	"r2":0,
	"r3":0,
	"l1":0,
	"l2":0,
	"l3":0,
	"touchpad":0
}
ds4_codes = {
	"x":1,
	"triangle":3,
	"square":0,
	"circle":2,
	"share":8,
	"options":9,
	"ps":12,
	"r1":5,
	"r2":7,
	"r3":11,
	"l1":4,
	"l2":6,
	"l3":10,
	"touchpad":13
}

key_states = {
	"w":0,
	"a":0,
	"s":0,
	"d":0,
	"scrollup":0,
	"scrolldown":0,
	"left_mouse":0,
	"right_mouse":0,
	"shift":0,
	"space":0,
	"ctrl":0,
	"options":0,
	"share":0,
	"touchpad":0
}




mouse_x = 0
mouse_y = 0
mouse_delta = 10
move_timer = 0
timer_delay = 0.005
last_time = time.time()
scroll_timer = 0
scroll_delay = 0.01

def update_ds4():
	global ds4_codes
	global ds4_data
	global ds4
	global key_states
	global mouse_x
	global mouse_y
	pg_events = pygame.event.get()
	for event in pg_events:
		if event.type == pygame.JOYAXISMOTION:
			##print("JoyAxis:",event.axis)
			if event.axis == 1:
				if event.value <= -0.5:
					if not key_states["w"]:
						#print("Holding W")
						PressKey(0x11)
					key_states["w"] = 1
				else:
					if key_states["w"]:
						#print("Releasing W")
						ReleaseKey(0x11)
					key_states["w"] = 0
				if event.value > 0.5:
					if not key_states["s"]:
						#print("Holding S")
						PressKey(0x1F)
					key_states["s"] = 1
				else:
					if key_states["s"]:
						#print("Releasing S")
						ReleaseKey(0x1F)
					key_states["s"] = 0
				##print("Axis 1:",event.value)
				#Axis 1: 1 is left down, -1 is left up
			elif event.axis == 0:
				if event.value <= -0.5:
					if not key_states["a"]:
						#print("Holding A")
						PressKey(0x1E)
					key_states["a"] = 1
				else:
					if key_states["a"]:
						#print("Releasing A")
						ReleaseKey(0x1E)
					key_states["a"] = 0
				if event.value > 0.5:
					if not key_states["d"]:
						#print("Holding D")
						PressKey(0x20)
					key_states["d"] = 1
				else:
					if key_states["d"]:
						#print("Releasing D")
						ReleaseKey(0x20)
					key_states["d"] = 0
					#Axis 1: 1 is left right, -1 is left left
			elif event.axis == 2:
				mouse_x = event.value
			elif event.axis == 3:
				mouse_y = event.value
				
			##print(event.dict, event.joy, event.axis, event.value)
			pass
		elif event.type == pygame.JOYBALLMOTION:
			##print("ball:",event.ball)
			##print(event.dict, event.joy, event.ball, event.rel)
			pass
		elif event.type == pygame.JOYBUTTONDOWN:
			for button in ds4_codes.keys():
				if ds4_codes[button] == event.button:
					if button == "r2":
						if not key_states["left_mouse"]:
							key_states["left_mouse"] = 1
							pg.mouseDown()
					if button == "r1":
						if not key_states["right_mouse"]:
							key_states["right_mouse"] = 1
							pg.mouseDown(button="right")
					if button == "l3":
						if not key_states["ctrl"]:
							key_states["ctrl"] = 1
							PressKey(0x1D)
					if button == "r3":
						if not key_states["shift"]:
							key_states["shift"] = 1
							PressKey(0x2A)
					if button == "x":
						if not key_states["space"]:
							key_states["space"] = 1
							PressKey(0x39)
					if button == "options":
						if not key_states["options"]:
							key_states["options"] = 1
							PressKey(0x01)
					if button == "share":
						if not key_states["share"]:
							key_states["share"] = 1
							PressKey(0x12)
					if button == "l2":
						if not key_states["touchpad"]:
							key_states["touchpad"] = 1
							PressKey(0x10)
					#print("Button pressed:",button)
					break
			#for button in ds4_codes.getKeys():
			##print(event.dict, event.joy, event.button, 'pressed')
		elif event.type == pygame.JOYBUTTONUP:
			for button in ds4_codes.keys():
				if ds4_codes[button] == event.button:
					if button == "r2":
						if key_states["left_mouse"]:
							key_states["left_mouse"] = 0
							pg.mouseUp()
					if button == "r1":
						if key_states["right_mouse"]:
							key_states["right_mouse"] = 0
							pg.mouseUp(button="right")
					if button == "l3":
						if key_states["ctrl"]:
							key_states["ctrl"] = 0
							ReleaseKey(0x1D)
					if button == "r3":
						if key_states["shift"]:
							key_states["shift"] = 0
							ReleaseKey(0x2A)
					if button == "x":
						if key_states["space"]:
							key_states["space"] = 0
							ReleaseKey(0x39)
					if button == "options":
						if key_states["options"]:
							key_states["options"] = 0
							ReleaseKey(0x01)
					if button == "share":
						if key_states["share"]:
							key_states["share"] = 0
							ReleaseKey(0x12)
					if button == "l2":
						if key_states["touchpad"]:
							key_states["touchpad"] = 0
							ReleaseKey(0x10)
					#print("Button released:",button)
					break
			##print(event.dict, event.joy, event.button, 'released')
		elif event.type == pygame.JOYHATMOTION:
			if event.hat == 0:
				#print("hat value:",event.value)
				if event.value[0] == 1:
					key_states["scrollup"] = 1
				else:
					key_states["scrollup"] = 0
				if event.value[0] == -1:
					key_states["scrolldown"] = 1
				else:
					key_states["scrolldown"] = 0

			##print(event.dict, event.joy, event.hat, event.value)
			#pass
# Begin the autobuild loop
def update_mouse():
	global mouse_x
	global mouse_y
	global delta_y
	global move_timer
	global last_time
	global timer_delay
	global scroll_timer
	global scroll_delay
	global key_states
	current_t = time.time()
	delta_t = current_t - last_time
	last_time = current_t
	move_timer = max(0,move_timer-delta_t)
	scroll_timer = max(0,scroll_timer-delta_t)
	if move_timer == 0:
		move(int(mouse_delta*mouse_x),int(mouse_delta*mouse_y))
		move_timer = timer_delay
	if scroll_timer == 0:
		if key_states["scrollup"]:
			#print("Scrolling down")
			pg.scroll(-50)
		if key_states["scrolldown"]:
			#print("Scrolling up")
			pg.scroll(50)
		scroll_timer = scroll_delay
try:
	while 1:
		update_ds4()
		update_mouse()
except KeyboardInterrupt:
	pygame.joystick.quit()
#print("Script terminated by user")