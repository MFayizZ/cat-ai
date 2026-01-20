import random
#----------state-----
trust=5
hunger=7
energy=6
emotion="neutral"
emotion_timer=0
is_sleeping=False
rule=False
#-------Helpers------
def set_emotion(e,t=3):
  global emotion,emotion_timer
  emotion = e
  emotion_timer = t

def decay_emotion():
  global emotion,emotion_timer
  if emotion_timer > 0:
    emotion_timer -= 1
  else:
    emotion = "neutral"

def has(words, text):
  return any(w in text for w in words)

def blink():
  print(random.choice(["*slow blink*","*Tail wagging in lazyness*","*Looks at you with its cute eyes*"]))
def play():
  w = True
  while w:
    pp = input("> ").lower().strip()
    if pp in ["Sit"]:
      print("*Sitting*")
    elif pp in ["Roll over"]:
      print("*Rolling over*")
    elif pp in ["Jump"]:
      print("*Jumping*")
    elif pp in ["Stop","Stop playing","No more playing"]:
      print("Stop playing")
      w = False
    else:
      print("*Looks at you in confusion*")
      
