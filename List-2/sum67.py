def sum67(nums):

  count =0;

  stop=0;

  for i in range(len(nums)):

    if nums[i]!=6  and stop ==0:

      count=count+nums[i];

    if nums[i]==6:

      stop=1;

    if nums[i]==7 and stop==1:
      stop=0;

  return count;