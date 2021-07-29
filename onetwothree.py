def array123(nums):
  for i in range(len(nums)-1):
    print(i)
    if nums[i] ==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
    else:
      return False
print(array123([1]))