def reverse3(nums):
 
 x = nums[0];
 
 nums[0]=nums[2]
 
 nums[2]=x;
 
 return nums;