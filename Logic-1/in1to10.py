def in1to10(n, outside_mode):

  if n==9 and outside_mode:return False;

  if n>=1 and n<=10 :

    return True;

  elif (n<1 or n>10) and outside_mode:

     return True;

  return False;