class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        i,j=0,n-1
        while i<j:
            sum_num=numbers[i]+numbers[j]
            if sum_num>target:
                j-=1
            elif sum_num<target:
                i+=1
            else:
                return [i+1,j+1]