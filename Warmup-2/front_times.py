def front_times(str, n):
  
  s="";
  
  if len(str) >= 3 :
 
    s=str[0]+str[1]+str[2];

  if len(str) == 2 :
  
    s=str[0]+str[1];
  
  if len(str) == 1:
   
    s=str[0];
 
  return s*n;