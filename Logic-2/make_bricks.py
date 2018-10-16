def make_bricks(small, big, goal):

  x=0;

  while big != 0 :

    if x<goal:

      x=x+5;

      big=big-1;

    if(x>goal):

      x=x-5;

      big=0;
    if x==goal :

      return True;
  while x!=goal and small!=0 :

    x=x+1;

    small=small-1;

  if  x == goal :

     return True;

     
  return False;