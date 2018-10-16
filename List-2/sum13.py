def sum13(nums):

   x=0;

   for i in range(len(nums)):

     if nums[i]==13 :

       if i!= len(nums)-1:

        nums[i+1]=0;

     else:

      x=x+nums[i];

      
   return x;
