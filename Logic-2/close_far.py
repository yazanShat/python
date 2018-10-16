def close_far(a, b, c):
  d=abs(a-c);
  f=abs(a-b);
  g=abs(c-b);
  if (d in [0,1] or f in [0,1]) and g>=2:
    if d in [0,1] and f>=2:
     return True;
    if f in [0,1] and d>=2:
     return True;
  return False;