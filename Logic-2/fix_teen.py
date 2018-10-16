def fix_teen(n):

   if n<13 or n>19 or n==15 or n==16 :

      return  n;
   return 0;

   
   
def no_teen_sum(a, b, c):

   x = [a,b,c];

   count=0;

   for i in range(len(x)):

     count=count+fix_teen(x[i]);

   return count;