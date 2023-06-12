def search(nums:List[int], target:int) -> int:
  l=0
  r= len(nums)-1
  while l<=r:
    mid = l + (r-l)//2
    if nums[mid] < target:
      l = mid + 1
    else:
      r = mid 
  if nums[l] != target: return -1  
  return l
