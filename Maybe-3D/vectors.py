import math

def neg(vec):
  return [-vec[0], -vec[1], -vec[2]]

def add(veca, vecb):
  return [veca[0] + vecb[0], veca[1] + vecb[1], veca[2] + vecb[2]]
def sub(veca, vecb):
  return [veca[0] - vecb[0], veca[1] - vecb[1], veca[2] - vecb[2]]

def dot(veca, vecb):
  return veca[0] * vecb[0] + veca[1] * vecb[1] + veca[2] * vecb[2]

def cross(veca, vecb):
  return [(veca[1] * vecb[2]) - (veca[2] * vecb[1]), (veca[2] * vecb[0]) - (veca[0] * vecb[2]), (veca[0] * vecb[1]) - (veca[1] * vecb[0])]

def mag(vec):
  return math.sqrt(vec[0]**2 + vec[1]**2 + vec[2]**2)
def magsqr(vec):
  return vec[0]**2 + vec[1]**2 + vec[2]**2

def angle(veca, vecb):
  return dot(veca, vecb) / (mag(veca) * mag(vecb))

def rot(yaw=0, pitch=0):
  yaw = math.radians(yaw % 360)
  pitch = math.radians(pitch % 360)
  return [math.cos(yaw) * math.cos(pitch), math.sin(pitch), math.sin(yaw) * math.cos(pitch)]

def norm(vec):
  return div(vec, mag(vec))

def mult(veca, mult):
  return [veca[0] * mult, veca[1] * mult, veca[2] * mult]

def div(veca, div):
  return [veca[0] / div, veca[1] / div, veca[2] / div]