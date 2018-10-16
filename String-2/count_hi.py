def count_hi(str):

  cou=0;

  for i in range(len(str)-1):

    if str[i]=='h' and str[i+1]=='i':

      cou=cou+1;

  return cou;