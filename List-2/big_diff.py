def big_diff(nums):

   mi=nums[0];

   ma=nums[0];

   for i in range(len(nums)-1):

      min(nums[i],nums[i+1]);
 
      if  min(nums[i],nums[i+1])<mi:

        mi= min(nums[i],nums[i+1]);

      max(nums[i],nums[i+1]);

      if  max(nums[i],nums[i+1])>ma:

        ma= max(nums[i],nums[i+1]);

   return abs(ma-mi);