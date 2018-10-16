def lone_sum(a, b, c):

  if (a==b and a==c and c==b):

     a=0;
     b=0;
     c=0;

  if (a==b):

    a=0;
    b=0;

  if (a==c):

    a=0;
    c=0;

  if(c==b):

    b=0;
    c=0;

  return a+b+c;