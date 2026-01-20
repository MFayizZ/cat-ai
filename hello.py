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
  if emotion_timer>0:
    emotion_timer-=1
  else:
    emotion="neutral"
