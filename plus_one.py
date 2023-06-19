# beginner level
def plusOne(self, digits: List[int]) -> List[int]:
      digit_str = ''.join([str(i) for i in digits])
      res = int(digit_str) +1
      return [int(i) for i in str(res)]
    
# advanced level    
def plusOne(self, digits):
return list(map(int, str(int(str(digits).replace("[", "").replace("]", "").replace(",", "").replace(" ", "")) + 1)))
